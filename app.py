from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
from dotenv import load_dotenv
import os

model = genai.GenerativeModel('gemini-pro')

load_dotenv();
my_api_key_gemini = os.getenv('MY_KEY')

# my_api_key_gemini = "AIzaSyDjGwWxe8asJWt_Ml_MwTzZwZBddNfNyFY"

genai.configure(api_key=my_api_key_gemini)

app = Flask(__name__)

# Define your 404 error handler to redirect to the index page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = "Please consider yourself as a learner and you need to ask your doubts to the user and then at the end please analyse this chat on the basis of grammer, tone of the agent should be professional, summarize the chat and comments what staps agent should take to increase the user experience. Also agent should guide the user to solution. Rate teh agent on the basis of each factor on scale of 10. please gave response in the form of JSON object having keys for rating in grammer, rating for tone, rating for agent's approach also add some comments in comments key"

            response = model.generate_content(question)

            if response.text:
                return response.text
            else:
                return "Sorry, but I think Gemini didn't want to answer that!"
        except Exception as e:
            return "Sorry, but Gemini didn't want to answer that!"

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
