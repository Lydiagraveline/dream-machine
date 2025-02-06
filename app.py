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
    if request.method == "POST":
        prompt = request.form["prompt"]
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[{"role": "developer", "content": "You are a Carl Jung dream interpretation assistant. You will be given a descriptions of a dreams, and you will provide short interpretations based on the symbols and themes present in the dream."}, 
                          {"role": "user", "content": prompt}],
                          temperature=1.2,
                          max_completion_tokens=150
            )
            result = response.choices[0].message.content
            
            # Generate an image using DALL·E
            image_response = openai.images.generate(
                model="dall-e-3",
                prompt=f"A simple drawing on paper depicting the following dream description: '{prompt}.' In the style of Leonora Carrington, Max Ernst, and Remedios Varo. The scene should visually depict the dream’s underlying Jungian symbols, archetypes, and the collective unconscious. Include mysterious, mythological, and psychological elements that reflect the dream’s deeper meaning. Avoid text and words.",
                n=1,
                size="1024x1024"
            )
            image_url = image_response.data[0].url  # Extract generated image URL
       
       
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result, image_url=image_url,)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing