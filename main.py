from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/<int:port>")
def hello(port):
    return "%d ^ 2 = %d" % (port, port ** 2)


@app.route("/<string:username>")
def introduction(username):
    return "我是%s，自己代言。" % username


@app.route("/path/<path:home>")
def your_home(home):
    return "你的家目录： %s" % home


@app.route("/http", methods=["POST", "GET"])
def http_type():
    if request.method == "POST":
        return "pppppppp"
    elif request.method == "GET":
        return "gggggggg"


@app.route("/tpl/<string:args>")
def templates_test(args=None):
    return render_template("hello.html")

