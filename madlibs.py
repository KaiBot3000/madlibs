from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    want_game = request.args.get("game_yesno")

    if want_game == "yes":
        # go to game
        return render_template("game.html")
    else:
        # go to goodbye page
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    person_input = request.args.get("person")
    color_input = request.args.get("color")
    city_input = request.args.get("city")
    adjective_input = request.args.get("adjective")

    animals_list = []

    if request.args.get("elephant"):
        animals_list.append('an elephant')
    if request.args.get("penguin"):
        animals_list.append('a penguin')
    if request.args.get("jellyfish"):
        animals_list.append('a jellyfish')
    if request.args.get("octopus"):
        animals_list.append('an octopus')

    animals_text = ", ".join(animals_list)

    return render_template("madlib.html", person=person_input, color=color_input, city=city_input, adjective=adjective_input, animals=animals_text)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
