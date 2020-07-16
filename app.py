# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/results', methods=['GET', 'POST'])
def results():
    user_character = request.form["character"]
    
    quote=""
    if user_character == "Yoda":
        # picture = "/static/images/micropig.jpg"
        quote = "Do or do not there is no try - The Empire Strikes Back"
    elif user_character == "Anakin Skywalker":
        quote = "I don't like sand. - Attack of the clones"
    elif user_character == "Obi wan":
        quote = "Hello there. - Revenge of the Sith"
    elif user_character == "Darth Vader":
        quote = "I find your lack of faith disturbing. - A New Hope"
    elif user_character == "Luke Skywalker":
        quote = "Amazing every word of what you just said was wrong. - The last Jedi"    
    elif user_character == "Han Solo":
        quote = "Never tell me the odds! - The Empire Strikes Back" 
    elif user_character == "Princess Leia":
        quote = "Help me, Obi Wan Kenobi you're my only hope. -A New Hope" 
    elif user_character == "Sheev Palpatine":
        quote = "Did you ever hear the Tragedy of Darth Plagueis the Wise? No. I thought not. It’s not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. He could actually save save people from death? The dark side of the Force is a pathway to many abilities some consider to be unnatural. What happened to him? He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself. - Revenge of the Sith" 
    elif user_character == "Chewbacca":
        quote = "AAARARRRGWWWH! - Return of the Jedi" 
    elif user_character == "Boba Fett":
        quote = "You are foolish to waste your kindness on this dumb creature. No lower life form is worth going hungry for! - Return of the Jedi" 
    elif user_character == "Kylo Ren":
        quote = "I'm sure you are! The Resistance is dead, the war is over, and when I kill you, I will have killed the last Jedi! - The last Jedi" 
    elif user_character == "Chewbacca":
        quote = "AAARARRRGWWWH! - Return of the Jedi" 
    elif user_character == "Rey":
        quote = "My name is Rey Skywalker - Rise of Skywalker" 
    else: 
        return "type a Star Wars character"
    
    return render_template("results.html", user_character=user_character, quote=quote)
