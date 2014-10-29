from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__) 

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(10).all()
    #in the following line: the orange user_list is the one that the html can read, and the white user_list is the python variable that we're manipulating in our route.
    return render_template("user_list.html", user_list=user_list)

@app.route("/user/<int:user_id>")
def get_ratings_list(user_id):
    ratings_list = model.session.query(model.Rating).filter_by(user_id = user_id).all()
    #^this returns a list of rating objects, each of which has the associated columns
    return render_template("movie_rating_list.html", user_id=user_id, ratings_list=ratings_list)

if __name__== "__main__":
    app.run(debug = True)
