from flask import Flask, render_template #Makes it posible to use templates

app = Flask (__name__) #serving app from this file

@app.route("/") #routes are what you type at the end op url, fx. search, maps. / is default when you visit the web page, and it calles the index function (landingpage)
def index(): 
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

#You run the web applicatiom by first going into the right directory, and then type flask run (not the folder name, but just flask everytime)

#push