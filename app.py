from flask import Flask,render_template, request

# 객체생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # 여기에 연락처 폼 처리 로직을 추가할 수 있습니다.
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

    

if __name__ == '__main__':
    app.run(debug=True)