from flask import Flask, render_template, request
from scanner import crawl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    results = crawl(url)
    return render_template("result.html", url=url, results=results)

if __name__ == '__main__':
    app.run(debug=True)