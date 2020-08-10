from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.
## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')
## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    bookReview_receive = request.form['bookReview_give']
    print(title_receive)
    test = {
        'title': title_receive,
        'author': author_receive,
        'bookReview_give': bookReview_receive,
    }
    db.bookReview.insert_one(test)
    return jsonify({'result': 'success', 'massage': '리뷰를 잘 저장했다'})
@app.route('/review', methods=['GET'])
def read_reviews():
    return jsonify({'result': 'success', 'massage': '생성한 리뷰를 저장했다!'})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
