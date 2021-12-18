from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    
@app.route("/projects")
def a():
    return render_template('project.html')
    
@app.route("/about")
def b():
    return render_template('about.html')