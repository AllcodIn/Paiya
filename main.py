from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('Page de Bienvenue.html')

@app.route("/templates/login")
def login():
    return render_template('login.html')

@app.route("/templates/AccountValidated'")
def AccountValidated():
    return render_template('AccountValidated.html')


@app.route("/templates/index")
def index():
    return render_template('index.html')


@app.route("/templates/CreateAccount")
def CreateAccount():
    return render_template('CreateAccount.html')

@app.route("/templates/profile")
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)





# @app.route("/templates/pageDeBienvenue")
# def pageDeBienvenue():
#     return render_template('pageDeBienvenue.html')

# @app.route("/templates/login")
# def login():
#     return render_template('login.html')

# @app.route("/templates/connection")
# def connection():
#     return render_template('connection.html')

# @app.route('/')
# def index(name=None):
#     return render_template('index.html', person=name)
# app.route("/")
# def index():
#     return "index.html"