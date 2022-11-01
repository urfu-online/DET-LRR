////////////////////////////////
// Setup
////////////////////////////////
// noinspection JSCheckFunctionSignatures

// Gulp and package

const {src, dest, parallel, series, watch} = require('gulp')
const pjson = require('./package.json')

// Plugins
const autoprefixer = require('autoprefixer')
const browserSync = require('browser-sync').create()
const concat = require('gulp-concat')
const cssnano = require('cssnano')
const imagemin = require('gulp-imagemin')
const pixrem = require('pixrem')
const plumber = require('gulp-plumber')
const postcss = require('gulp-postcss')
const reload = browserSync.reload
const rename = require('gulp-rename')
const sass = require('gulp-sass')(require('sass'))
// const spawn = require('child_process').spawn
const uglify = require('gulp-uglify-es').default

// Relative paths function
function pathsConfig() {
    this.app = `./${pjson.name}`
    const vendorsRoot = 'node_modules'

    return {
        bootstrapSass: `${vendorsRoot}/bootstrap/scss`,
        vendorsJS: [`${vendorsRoot}/jquery/dist/jquery.js`, `${vendorsRoot}/popper.js/dist/umd/popper.js`, `${vendorsRoot}/bootstrap/dist/js/bootstrap.js`,],
        gridstackJS: [`${vendorsRoot}/gridstack/dist/gridstack-all.js`,],
        gridstackSCSS: `${vendorsRoot}/gridstack/dist/src/`,
        app: this.app,
        templates: `${this.app}/templates`,
        css: `${this.app}/static/css`,
        sass: `${this.app}/static/sass`,
        fonts: `${this.app}/static/fonts`,
        images: `${this.app}/static/images`,
        js: `${this.app}/static/js`,
    }
}

let paths = pathsConfig()

////////////////////////////////
// Tasks
////////////////////////////////

// Styles auto prefixing and minification
function styles() {
    let processCss = [autoprefixer(), // adds vendor prefixes
        pixrem(),       // add fallbacks for rem units
    ]

    let minifyCss = [cssnano({
        preset: ['default', {
            discardComments: {
                removeAll: true,
            }
        }]
    })   // minify result
    ]

    return src(`${paths.sass}/project.scss`)
        .pipe(sass({
            includePaths: [paths.bootstrapSass, paths.sass]
        }).on('error', sass.logError))
        .pipe(plumber()) // Checks for errors
        .pipe(postcss(processCss))
        .pipe(dest(paths.css))
        .pipe(rename({suffix: '.min'}))
        .pipe(postcss(minifyCss)) // Minifies the result
        .pipe(dest(paths.css))
}

function admin_extra_styles() {
    let processCss = [autoprefixer(), // adds vendor prefixes
        pixrem(),       // add fallbacks for rem units
    ]

    let minifyCss = [cssnano({
        preset: ['default', {
            discardComments: {
                removeAll: true,
            }
        }]
    })   // minify result
    ]

    return src(`${paths.sass}/admin_extra.scss`)
        .pipe(sass().on('error', sass.logError))
        .pipe(plumber()) // Checks for errors
        .pipe(postcss(processCss))
        .pipe(dest(paths.css))
        .pipe(rename({suffix: '.min'}))
        .pipe(postcss(minifyCss)) // Minifies the result
        .pipe(dest(paths.css))
}

function gridstackStyles() {
    let processCss = [autoprefixer(), // adds vendor prefixes
        pixrem(),       // add fallbacks for rem units
    ]

    let minifyCss = [cssnano({
        preset: ['default', {
            discardComments: {
                removeAll: true,
            }
        }]
    })   // minify result
    ]

    return src(`${paths.gridstackSCSS}/gridstack.scss`)
        .pipe(sass().on('error', sass.logError))
        .pipe(plumber()) // Checks for errors
        .pipe(postcss(processCss))
        .pipe(dest(paths.css))
        .pipe(rename({suffix: '.min'}))
        .pipe(postcss(minifyCss)) // Minifies the result
        .pipe(dest(paths.css))
}

// Javascript minification
function scripts() {
    return src(`${paths.js}/project.js`)
        .pipe(plumber()) // Checks for errors
        .pipe(uglify()) // Minifies the js
        .pipe(rename({suffix: '.min'}))
        .pipe(dest(paths.js))
}

// Vendor Javascript minification
function vendorScripts() {
    return src(paths.vendorsJS)
        .pipe(concat('vendors.js'))
        .pipe(dest(paths.js))
        .pipe(plumber()) // Checks for errors
        .pipe(uglify()) // Minifies the js
        .pipe(rename({suffix: '.min'}))
        .pipe(dest(paths.js))
}

// Gridstack Javascript minification
function gridstackScripts() {
    return src(paths.gridstackJS)
        .pipe(concat('gridstack.js'))
        .pipe(dest(paths.js))
        .pipe(plumber()) // Checks for errors
        .pipe(uglify()) // Minifies the js
        .pipe(rename({suffix: '.min'}))
        .pipe(dest(paths.js))
}

// Image compression
function imgCompression() {
    return src(`${paths.images}/*`)
        .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
        .pipe(dest(paths.images))
}

// Run django server
// function runServer(cb) {
//     let cmd = spawn('python', ['manage.py', 'runserver'], {stdio: 'inherit'})
//
//     cmd.on('close', (code) => {
//         console.log(`runServer exited with code ${code}`)
//         cb(code)
//     })
// }

// Browser sync server for live reload
function initBrowserSync() {
    browserSync.init([`${paths.css}/*.css`, `${paths.js}/*.js`, `${paths.templates}/*.html`], {
        // https://www.browsersync.io/docs/options/#option-proxy

        proxy: 'localhost:8000', // https://www.browsersync.io/docs/options/#option-open
        // Disable as it doesn't work from inside a container
        open: false
    })
}

// Watch
function watchPaths() {
    watch(`${paths.sass}/*.scss`, styles)
    watch(`${paths.sass}/*.scss`, admin_extra_styles)
    watch(`${paths.templates}/**/*.html`).on("change", reload)
    watch([`${paths.js}/*.js`, `!${paths.js}/*.min.js`], scripts).on("change", reload)
}

// Generate all assets
const generateAssets = parallel(admin_extra_styles, styles, scripts, vendorScripts, gridstackScripts, gridstackStyles, imgCompression)

// Set up dev environment
const dev = parallel(initBrowserSync, watchPaths)

exports.default = series(generateAssets, dev)
exports["generate-assets"] = generateAssets
exports.dev = dev
