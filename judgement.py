from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__) 

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    #in the following line: the orange user_list is the one that the html can read, and the white user_list is the python variable that we're manipulating in our route.
    return render_template("user_list.html", user_list=user_list)

@app.route("/user/<int:id>")
def movie_ratings_by_user(id):

    #write a line that gets all movie ratings rated by single user
    #model like line below:

    ratings_list = model.session.query(model.Rating).WTF_DO_I_PUT_HERE

    # it makes sense to put something like SELECT * FROM Ratings WHERE id = id 
    # maybe it is filter_by()  <-search this in hackbright exercise page AND/OR SQL Alchemy documentation

    return render_template("movie_rating_list.html", id=id, ratings_list=ratings_list)

    pass 

if __name__== "__main__":
    app.run(debug = True)
