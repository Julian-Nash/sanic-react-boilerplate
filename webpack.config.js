const path = require('path')

module.exports = {
  // Setup watcher
  watch: true,
  watchOptions: {
    ignored: /node_modules/,
  },
  // Setup entrypoint
  entry: './app/static/src/index.jsx',
  // Where files should be sent once they are bundled
  output: {
   path: path.join(__dirname, '/app/static/dist'),
   filename: 'index.bundle.js'
  },
  // Rules of how webpack will take our files, compile & bundle them for the browser
  module: {
   rules: [
     {
       test: /\.(js|jsx)$/,
       exclude: /nodeModules/,
       use: {
         loader: 'babel-loader'
       }
     },
     {
       test: /\.css$/,
       use: ['style-loader', 'css-loader']
     }
   ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx'],
  }
}