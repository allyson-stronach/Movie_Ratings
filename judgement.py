from flask import Flask, render_template, redirect, request, session, flash
import model

app = Flask(__name__) 
app.secret_key = "blah"

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(10).all()
    #in the following line: the orange user_list is the one that the html can read, and the white user_list is the python variable that we're manipulating in our route.
    
    return render_template("user_list.html", user_list=user_list)

@app.route("/user/<int:user_id>")
def get_ratings_list(user_id):
    ratings_list = model.session.query(model.Rating).filter_by(user_id = user_id).all()
    #this returns a list of rating objects, each of which has the associated db columns
    return render_template("movie_rating_list.html", user_id=user_id, ratings_list=ratings_list)

@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    
    email = request.form.get("email")
    password = request.form.get("password")
    age = request.form.get("age")
    zip_code = request.form.get("zip_code")

    #create new instance of User and assign input values
    #add/commit new user to database
    u = model.User()
    u.email = email
    u.password = password
    u.age = age
    u.zip_code = zip_code
    model.session.add(u)
    model.session.commit()

    # please explain this syntax- [ ??? ] and why print session
    # session["user_email"] = u.email
    # session["user_id"] = str(u.id)
    # print session
    flash("You successfully signed up!")

    return redirect("/")

@app.route("/signup_form")
def signup_form():
    return render_template("signup_form.html")

@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    flash("You are now logged out.")
    return redirect("/")

if __name__== "__main__":
    app.run(debug = True)
