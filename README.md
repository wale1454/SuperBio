# Superhero Name Generator - Unleash Your Superhero Alter-Ego

This is an AI Superhero Name Generator app which uses the OpenAI GPT-3 [API](https://beta.openai.com/docs/quickstart) to give you a super hero name based on a specific characteristic/ fun trait you input in it. 



----

----



<table>
  <tbody>
    <tr>
      <td>
        <video src="https://user-images.githubusercontent.com/31905212/214253892-c5f0b1ab-613c-4a24-9bbf-3b559192aaed.mp4   ">
      </td>
      <td>
        <video src="https://user-images.githubusercontent.com/31905212/214254208-7e4259dc-7ecd-469e-b04f-21af29b57113.mp4">
      </td>
    </tr>
 
  </tbody>
</table>

----


----





It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework.  
Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ mkdir Superhero_Name_Generator
   ```

4. Create a new virtual environment

   ```bash
   $ virtualenv newEnvironment
   $ source newEnvironment/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```


6. Add your [API key](https://beta.openai.com/account/api-keys) to the app.py file replacing "OPENAI API KEY"

7. Run the app

   ```bash
   $ export FLASK_APP=app.py
   $ export FLASK_ENV=development
   $ flask run
   ```

You should be able to access the app at [http://localhost:5000](http://localhost:5000)
