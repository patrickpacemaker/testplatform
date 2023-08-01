from flask import Flask, jsonify
import os



app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

# Your list of strings
string_list = ["Date", "PriceInUSD", "moving_average", "rolling_stddev", "lag_1_PriceInUSD", "lag_2_PriceInUSD", "lag_3_PriceInUSD", "percent_deviation", "is_peak", "trend", "cluster", "ROC", "RSI", "Open", "High", "Low", "Close", "ExchangeRate_LogReturns", "OilPrice_LogReturns", "Close_MA_7", "OilPrice_MA_7", "Close_MA_14", "OilPrice_MA_14", "Close_MA_30", "OilPrice_MA_30", "Close_Lag_1", "OilPrice_Lag_1", "Close_Lag_7", "OilPrice_Lag_7", "Close_Lag_14", "OilPrice_Lag_14", "Interaction_Feature", "Close_LogReturns", "url1", "url2", "url3", "header1", "header2", "header3", "body1", "body2", "body3" ], 

@app.route('/api/strings', methods=['GET'])
def get_strings():
    return jsonify(string_list)

if __name__ == '__main__':
    app.run()
