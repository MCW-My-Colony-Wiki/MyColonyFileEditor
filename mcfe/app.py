from flask import Flask, render_template

from mcfp.mcfp.libs.request import get_valid_version

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html", versions=get_valid_version())

if __name__ == "__main__":
	app.run()
