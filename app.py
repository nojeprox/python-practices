from flask import Flask
app = Flask(__name__)
@app.route("/")

def main():
	return "This is my own web server!"


if __name__ == "__main__":
		app.run(debug = True, host = "0.0.0.0", port = 1024)
