from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__) 

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    #in the following line: the orange user_list is the one that the html can read, and the white user_list is the python variable that we're manipulating in our route.
    return render_template("user_list.html", user_list=user_list)

@app.route("/user/<int:id>")
def user_or_something(id):
    #do some stuff

if __name__== "__main__":
    app.run(debug = True)
