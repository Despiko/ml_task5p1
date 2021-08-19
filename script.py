import sys
import traceback
from flask import Flask, request, jsonify
import despik_package.despik_package as dp
import ast


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['POST'])
def index():
    try:
        dic = request.get_data()
        dic = dic.decode('utf8')
        dic = ast.literal_eval(dic)
        print('input:\n', dic)
        for k, v in dic.items():
            if k == 'get_info':
                return dp.get_info(v)
            elif k == 'get_all_price':
                return dp.get_all_price(v)
            elif k == 'get_close_price':
                return dp.get_close_price(v)
            elif k == 'close_price_percent':
                return dp.close_price_percent(v)
            elif k == 'plot_ticker':
                return dp.plot_ticker(v)
            elif k == 'simple_regression':
                return dp.simple_regression(v)
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()})


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80
    app.run(host='0.0.0.0', port=port, debug=True)
