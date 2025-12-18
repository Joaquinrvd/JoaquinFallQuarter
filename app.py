from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template("index.html")

# About Me page route
@app.route('/about-me')
def about_me():
    return render_template("about_me.html")

if __name__ == '__main__':
    app.run(debug=True)
