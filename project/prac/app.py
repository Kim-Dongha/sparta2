from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/webtoon')
def hello_webtoon():
    return render_template('index.html')

@app.route('/mypage')
def my_page():
    return  'this is my page'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)