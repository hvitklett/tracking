from flask import Flask, redirect, render_template, request #Makes it posible to use templates
from cs50 import SQL

app = Flask (__name__) #serving app from this file
db = SQL("sqlite:///database.db") #Give access to database

@app.route("/") #routes are what you type at the end op url, fx. search, maps. / is default when you visit the web page, and it calles the index function (landingpage)
def landingpage(): #Function called index, when you run it it renders a template called landingpage (when the user visits a specific route, the function returns to them some html content)
    return render_template("landingpage.html")

@app.route("/seizures")
def seizures ():
    return render_template("seizures.html") #return the template html file

@app.route("/symptoms")
def symptoms ():
    return render_template("symptoms.html") 

@app.route("/medicin")
def medicin ():
    return render_template("medicin.html")

@app.route("/kalender")
def kalender():
    return render_template("kalender.html")

@app.route("/navnmedicin", methods=["GET", "POST"]) #Database prøve medicin
def navnmedicin():
    medicin_list = db.execute("SELECT * FROM medication") #select all the data in the medicin table and save in a py variable called medicin_list
    if request.method == "GET":
        return render_template("navnmedicin.html", medicin_list=medicin_list) #navnmedicin will have access to the variable medicin_list
    else:
        name = request.form.get("name")
        db.execute("INSERT INTO medication (name) VALUES (:name)", name=name)
        return ("/navnmedicin")

#You run the web application by first going into the right directory, and then type flask run (not the folder name, but just flask everytime)
#The render template function can also pass in variables to our html files
