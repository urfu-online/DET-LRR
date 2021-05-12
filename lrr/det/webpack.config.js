const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

const isProduction = process.env.NODE_ENV == "production";


const config = {
    entry: {
        "det.admin": ["./src/index.js", "./src/det.scss"]
    },
    output: {
        path: path.resolve(__dirname, "static/det-admin"),
    },
    devServer: {
        open: true,
        host: "localhost",
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '[name].css'
        }),
        new CssMinimizerPlugin(),
    ],
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/i,
                loader: "babel-loader",
            },
            {
                test: /\.(scss|css)$/,
                use: [
                    isProduction ? MiniCssExtractPlugin.loader : 'style-loader',
                    'css-loader', {
                        loader: 'postcss-loader', options: {
                            postcssOptions: {
                                plugins: function () {
                                    return [require('autoprefixer')];
                                }
                            }
                        }
                    }, 'sass-loader']


            },
            {
                test: /\.css$/i,
                use: [{loader: CssMinimizerPlugin.loader}, "css-loader", "postcss-loader"],
            },
            {
                test: /\.(eot|svg|ttf|woff|woff2|png|jpg|gif)$/i,
                type: "asset",
            },

        ],
    },
    optimization: {
        mangleExports: 'size',
        removeEmptyChunks: true,
        removeAvailableModules: true,
        mangleWasmImports: true,
        moduleIds: "size",
        minimize: true,
        minimizer: [
            new TerserPlugin({
                extractComments: "all",
                parallel: true,
                terserOptions: {
                    ecma: undefined,
                    parse: {},
                    compress: {},
                    mangle: true, // Note `mangle.properties` is `false` by default.
                    module: false,
                    // Deprecated
                    output: null,
                    format: null,
                    toplevel: false,
                    nameCache: null,
                    ie8: false,
                    keep_classnames: undefined,
                    keep_fnames: false,
                    safari10: false,
                },
            }),
            new CssMinimizerPlugin(),
        ]
    }
};

module.exports = () => {
    if (isProduction) {
        config.mode = "production";
    } else {
        config.mode = "development";
    }
    return config;

};
