from flask import Flask, render_template

app = Flask(__name__)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/transalate')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)
# you can add inboound rule in networking
