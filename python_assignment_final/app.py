# A00279670

from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.secret_key = "abcdef1234567890"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(32), unique=True, nullable=False)
    password = db.Column("password", db.String(32), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

def get_date():
    """
        The getdate function does not take in a parameter and returs the current date as a formatted string

        Returns
        -------
        String - The function returns a formatted string of the current Date

    """

    today = date.today()
    dt = today.strftime("%d/%m/%Y")
    return dt

def check_logged_in():
    """
        The check_logged_in() function uses the session to find out if a user is currently logged in

        Returns
        -------
        String - The Return string outputs a line of text on the browser depending if a user is currently in the session

    """

    if "user" in session:
        return f"Welcome {session['user']}"
    else:
        return "You are not logged in"


@app.route("/")
def home():
    """
        the home() function sends the user to the home page of the website

        Returns
        -------
        Returns the user to the page - index.html

    """

    return render_template('index.html', welcome=check_logged_in())


@app.route("/sandbox.html")
def sandbox():
    """
        The sandbox() function computes the current date/time and returns the user to the page sandbox.html with the
        data and time

        Returns
        -------
        Returns the user to the page - sandbox.html

    """

    dt = get_date()
    return render_template('sandbox.html', current_date_time=dt, welcome=check_logged_in())


@app.route("/register.html", methods=["POST", "GET"])
def register():
    """
        The register() function allows a user to submit a Username and Password to the database and register an account
        on the site

        Returns
        -------
        If a user is logged in (in the session) - Returns the user to the page Secure.html
        If a user has registered successfully - Returns the user to the page Login.html
        If a user is not logged in - Returns the user to the page Register.html
        If a user attempts to register incorrectly - Returns the user to the page Register.html with error message

    """

    if "user" in session:
        return redirect(url_for('secure'))

    if request.method == "POST":

        username = request.form["nm"]
        password = request.form["pw"]

        found_user = users.query.filter_by(username=username).first();

        if found_user : # user already exists in the database
            return render_template('login.html', err_msg="Username already exists")

        # validate and add new user
        else:

            if len(username) < 5:
                return render_template('register.html', err_msg="Username must be 5 characters or more")
            if len(password) < 5:
                return render_template('register.html', err_msg="Password must be 5 characters or more")

            # add the login details to the database
            usr = users(username, password)
            db.session.add(usr)
            db.session.commit()

            return redirect(url_for('login'))
    else:
        return render_template('register.html', err_msg="")


@app.route("/login.html", methods=["POST", "GET"])
def login():
    """
        The login() function allows a user to submit a Username and Password, the input data is matched to the database
        and the user is redirected to the appropriate page

        Returns
        -------
        If a user is not logged in - Returns the user to the page Login.html
        If a user is logged in (in the session) - Returns the user to the page Secure.html
        If a user has logged in successfully - Returns the user to the page Secure.html
        If a user attempts to Login incorrectly - Returns the user to the page login.html with error message
    """

    if request.method == "POST":

        usr_username = request.form["nm"]
        usr_password = request.form["pw"]

        if len(usr_username) < 5:
            return render_template('login.html', err_msg="Username must be 5 characters or more")
        if len(usr_password) < 5:
            return render_template('login.html', err_msg="Password must be 5 characters or more")

        # Check the database for the login details
        user = users.query.filter_by(username=usr_username).first()

        if user == None:
            return render_template('login.html', err_msg="Username not found")

        if user.password != usr_password:
            return render_template('login.html', err_msg="Incorrect Password")

        session["user"] = usr_username
        return redirect(url_for('secure'))

    else:
        if "user" in session:
            return redirect(url_for('secure'))
        else:
            return render_template('login.html')


@app.route("/secure.html")
def secure():
    """
        The secure() function checks if a user is logged in (by checking the session variable) and redirects the user
        to the login page or the secure page depending on the result

        Returns
        -------
        If a user is not logged in - Returns the user to the page Login.html
        If a user is logged in (in the session) - Returns the user to the page Secure.html
    """
    if "user" in session:
        return render_template('secure.html', welcome=check_logged_in())
    else:
        return redirect(url_for("login"))


@app.route("/logout.html")
def logout():
    """
        The logout() function clears the session of the current user and returns the user to the login page

        Returns
        -------
        If a user is not logged in - Returns the user to the page Login.html
        If a user is logged in (in the session) - clears the session and returns the user to the login page
    """

    if "user" in session:
        session.pop('user')
        return render_template('index.html', welcome=check_logged_in())
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
