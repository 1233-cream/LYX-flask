from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import jsonify

app = Flask(__name__)


@app.route('/index/list',methods=['Get'])
def index():

    url_str = 'www.baidu.com'

    my_dict = {
        'name': '狗崽子',
        'age': 19
    }

    my_list = [1, 3, 5, 7, 9]
    return render_template('index.html',
                           url_str=url_str,
                           my_list=my_list,
                           my_dict=my_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
