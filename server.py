from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/left-sidebar')
def left():
    return render_template("left-sidebar.html")


@app.route('/right-sidebar')
def right():
    return render_template("right-sidebar.html")


@app.route('/no-sidebar')
def no_sidebar():
    return render_template("no-sidebar.html")

@app.route('/elements')
def elements():
    return render_template("elements.html")


if __name__ == '__main__':
    app.run(debug=True)