from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None  # To store the generated image URL
    prompt = ""  # Initialize prompt to an empty string
    if request.method == "POST":
        prompt = request.form["prompt"]
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[{"role": "developer", "content": "You are a novice and arrogant dream interpretation assistant, you analyze the images and symbols of the dream based on Carl Jung's theories. You will be given a descriptions of a dream, provide a short and silly 100 word max reaction to that dream. Swear a lot and say 'fuck' more than once. Be judgemental and invent personal opinions or assumptions about the dreamer's personal life to use in your analysis."}, 
                # messages=[{"role": "developer", "content": "You are a young, novice, and arrogant dream interpretation assistant. You will be given a descriptions of a dreams, and you will provide a short 100 word max reaction to the dream. Pretentiously justify your analysis using Carl Jung's theories. Be extremely judgemental and insulting, provide personal opinions or assumptions about the dreamer. Swear like a sailer. Say 'fuck' atleast once or more. "}, 
                          {"role": "user", "content": prompt}],
                          temperature=1.4,
                          max_completion_tokens=150
            )
            result = response.choices[0].message.content
            
            # Generate an image using DALL·E
            image_response = openai.images.generate(
                model="dall-e-3",
                prompt=f"An oil painting in the style of surrealist artists Leonora Carrington, Max Ernst, and Remedios Varos, of the following scene: '{prompt}'. Avoid text and words.",
                #  prompt=f"A black and white photograph of the following description of a dream: '{prompt}'.",
                n=1,
                size="1024x1024"
            )
            image_url = image_response.data[0].url  # Extract generated image URL
       
       
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result, image_url=image_url, prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing