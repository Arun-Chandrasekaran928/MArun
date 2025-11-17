from flask import Flask, send_from_directory, render_template
import subprocess

# Correct: import the module, NOT a variable called "copyright"
import Launch.Python.copyright as cr

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("launch-main-menu.html")

@app.route("/run")
def run_python():
    # Correct: run the python file directly using its path
    python_file = "/home/arun/Minecraft/Launch/Python/copyright.py"
    subprocess.Popen(["python3", python_file])
    return "OK"

@app.route("/html-launch.html")
def html_page():
    return send_from_directory("templates", "html-launch.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
