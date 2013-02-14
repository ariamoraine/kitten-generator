from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
	return render_template("hello.html", name=name)

@app.route("/aria")
def aria():
	return "My name is Aria."

if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 0))
	port = sock.getsockname()[1]
	sock.close()
	app.run(port=port)