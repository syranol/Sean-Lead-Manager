module.exports = {
    module: {
        // Rules is an array
        rules: [
            {
                //One object, look at all js 
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}