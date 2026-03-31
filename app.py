import threading
import webbrowser

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    import os
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        threading.Timer(1.0, webbrowser.open, args=("http://localhost:6578",)).start()
    app.run(debug=True, port=6578)
