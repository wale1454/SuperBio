import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "OPEN-AI API KEY"


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
                    Names: Screen Savvy, Movie Marvel, 

                    Characteristic: White teeth
                    Names: Pearl Punch, The Snowbite, Smile Savior

                    Characteristic: I enjoy rap music
                    Names: Rhythm Renegade, Rap Rager, MC Marvel

                    Characteristic: I am happy
                    Names: The Joyful Juggernaut, The Ecstatic Warrior, The Thrilled Thunderer, The Elated Guardian

                    

                    Characteristic: {}
                    Names:""".format(animal.capitalize()
    )
