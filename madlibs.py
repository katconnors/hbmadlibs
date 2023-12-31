"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request
#collab with 
# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Playing Mad libs"""
    
    choice = request.args.get("yeah")
    
    if choice == "yes":
       return render_template("game.html") 
    else: 
        return render_template("goodbye.html")
    
@app.route("/madlib")
def show_madlib():
    
    """Showing mad libs sentence"""

    color = request.args.get("color")
    person= request.args.get("person")
    noun= request.args.get("noun")
    adjective = request.args.get("adjective")
    verb1 = request.args.get("verb1")
    verb2 = request.args.get("verb2")
    # print(verb1)
    # print(verb2)



    return render_template("madlibs.html", color=color, person=person, adjective=adjective, noun=noun, verb1=verb1, verb2=verb2)

    #can't return multiple here
    #conditional to either load the goodbye html or the game html


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
