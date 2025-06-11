from flask import Flask,render_template, request, redirect, url_for

# 객체 생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)