import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, render_template, request, send_from_directory
from scanner.core import Scanner

app = Flask(__name__)

REPORT_FOLDER = os.path.abspath("reports")


@app.route("/", methods=["GET", "POST"])
def home():
    results = None

    if request.method == "POST":
        target = request.form["target"]
        results = Scanner([target]).run()[0]

    return render_template("index.html", results=results)


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(REPORT_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)