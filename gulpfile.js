////////////////////////////////
// Setup
////////////////////////////////
// noinspection JSCheckFunctionSignatures

// Gulp and package

const {src, dest, parallel, series, watch} = require('gulp')
const pjson = require('./package.json')

// Plugins
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

const processCss = [
    require("postcss-merge-rules"),
    require("pixrem"),       // add fallbacks for rem units
]

// Relative paths function
function pathsConfig() {
    this.app = `./${pjson.name}`
    const vendorsRoot = 'node_modules'

    return {
        bootstrapSass: `${vendorsRoot}/bootstrap/scss`,
        vendorsJS: [
            `${vendorsRoot}/jquery/dist/jquery.js`,
            `${vendorsRoot}/popper.js/dist/umd/popper.js`,
            `${vendorsRoot}/bootstrap/dist/js/bootstrap.js`,
            `${vendorsRoot}/datatables.net/js/jquery.dataTables.js`,
            `${vendorsRoot}/datatables.net-bs4/js/dataTables.bootstrap4.js`,
            `${vendorsRoot}/datatables.net-buttons/js/dataTables.buttons.js`,
            `${vendorsRoot}/datatables.net-buttons-bs4/js/buttons.bootstrap4.js`,
            `${vendorsRoot}/datatables.net-responsive/js/dataTables.responsive.js`,
            `${vendorsRoot}/datatables.net-responsive-bs4/js/responsive.bootstrap4.js`,
            `${vendorsRoot}/datatables.net-searchpanes/js/dataTables.searchPanes.js`,
            `${vendorsRoot}/datatables.net-searchpanes-bs4/js/searchPanes.bootstrap4.js`,
        ],
        bundleCSS: [
            `${vendorsRoot}/datatables.net-bs4/css/dataTables.bootstrap4.css`,
            `${vendorsRoot}/datatables.net-buttons-bs4/css/buttons.bootstrap4.css`,
            `${vendorsRoot}/datatables.net-responsive-bs4/css/responsive.bootstrap4.css`,
            `${vendorsRoot}/datatables.net-searchpanes-bs4/css/searchPanes.bootstrap4.min.css`,
        ],
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

function bundle_styles() {
    let minifyCss = [cssnano({
        preset: ['default', {
            discardComments: {
                removeAll: true,
            }
        }]
    })
    ]

    return src(paths.bundleCSS)
        .pipe(concat('vendor.css'))
        .pipe(postcss(processCss))
        .pipe(dest(paths.css))
        .pipe(rename({suffix: '.min'}))
        .pipe(postcss(minifyCss)) // Minifies the result
        .pipe(dest(paths.css))
}

function gridstackStyles() {
    let processCss = [ // adds vendor prefixes
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
        .pipe(concat('gridstack-all.js'))
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
const generateAssets = parallel(admin_extra_styles, styles, bundle_styles, scripts, vendorScripts, gridstackScripts, gridstackStyles, imgCompression)

// Set up dev environment
const dev = parallel(initBrowserSync, watchPaths)

exports.default = series(generateAssets, dev)
exports["generate-assets"] = generateAssets
exports.dev = dev
