import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_APIKEY', 'default_value')




@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.8,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

 
def generate_prompt(animal):
    return """ Generate five cool superhero names based on the characteristic that I have below.
                    
                    Characteristic: Big teeth
                    Names: Big Bite, The Fang, Chomp Champion

                    Characteristic: I love watching movies
                    Names: Screen Savvy, Movie Marvel, The Cinematic Sage

                    Characteristic: White teeth
                    Names: Pearl Punch, The Snowbite, Smile Savior

                    Characteristic: I enjoy rap music
                    Names: Rhythm Renegade, Rap Rager, MC Marvel

                    Characteristic: I am happy
                    Names: The Joyful Juggernaut, The Ecstatic Warrior, The Thrilled Thunderer, The Elated Guardian

                    Characteristic: Fast runner
                    Names: The Sprinting Sentinel, Blaze Bolt, Rapid Ranger

                    Characteristic: Loves to cook
                    Names: The Culinary Crusader, Spice Sorcerer, Flavor Fighter

                    Characteristic: I am Tech-savvy
                    Names: Cyber Crusader, The Binary Bandit, The Digital Defender

                    Characteristic: I dont sleep early
                    Names: The Midnight Marauder, The Nocturnal Ninja, The Dark Defender

                    Characteristic: Loves to travel
                    Names: The Global Guardian, The Wander Warrior, The Jet-Set Sentinel

                    Characteristic: Likes to dance
                    Names: The Dancing Dynamo, The Groove Guardian, The Beat Blaster

                    Characteristic: Enjoys puzzles
                    Names: The Puzzle Protector, The Riddle Ranger, The Brainteaser Battler

                    Characteristic: Loves animals
                    Names: The Beast Battler, The Critter Crusader, The Furry Fighter

                    Characteristic: Enjoys gardening
                    Names: The Green Guardian, The Garden Gladiator, The Floral Fighter

                    Characteristic: Loves the ocean
                    Names: The Aqua Avenger, The Oceanic Oracle, The Wave Warrior
                        

                    Characteristic: {}
                    Names:""".format(animal.capitalize()
    )
