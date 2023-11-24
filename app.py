from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

FLAG = "INCO{SECRET}"

@app.after_request
def csp(res):
    res.headers['Content-Security-Policy'] = f"default-src http://{request.host}/xss 'unsafe-inline';"
    return res

@app.route('/')
def index():
    return 'Try <a href="/xss">xss</a> gogo~~<br><a href="/report">report</a>'

@app.route('/xss', methods=["GET"])
def xss():
    payload = request.args.get('payload')
    if payload:
        return payload
    return "hi"

@app.route('/report', methods=["GET", "POST"])
def report():
    if request.method == "GET":
        return '<form action="/report" method="post">payload : <input type="text" name="payload"><input type="submit" value="Report"></form>'
    payload = request.form["payload"]
    return subprocess.check_output(["python3", "bot.py", payload])

@app.route('/flag', methods=["POST"])
def flag():
    if request.remote_addr == "127.0.0.1":
        admin = request.form['admin']
        if admin == "zzlol":
            return FLAG
    return "nono zzlol"

app.run(host="0.0.0.0", port=8000)