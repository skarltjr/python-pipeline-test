from flask import Flask
app = Flask(__name__)

# 일반적인 라우트 방식입니다.
@app.route('/hello')
def board():
    return "hello"

app.run(host = '0.0.0.0',port = 5001,debug=True)