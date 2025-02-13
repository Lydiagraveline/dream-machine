# Sarcastic Dream-Machine  

This web app is a **sarcastic dream-machine** that uses AI to generate playful dream interpretations and surrealist dream depictions. While the AI is prompted to analyze dreams through the lens of **Carl Jung’s theories**, it takes a deliberately **unreliable and rude** approach. **Don’t take it too personally!**  

## About  

After researching Jung’s dream analysis methods, I found that his process is highly **personal** and relies on the **context of an individual’s life**. Since AI lacks this insight, and user-submitted dream descriptions vary in detail, I took a different route.  

Instead of aiming for accuracy, the AI is designed to be an **overconfident, arrogant novice** who may misinterpret dreams with **unwarranted certainty**. It is also prompted to **invent personal opinions and assumptions** about the dreamer’s life and instructed to be **judgmental, irreverent, and to swear liberally**. This exaggeration contrasts Jung’s individualized approach, making the analysis more **entertaining than precise**.  

### Surrealist Image Generation  

For image generation, the AI is prompted to create surrealist artwork inspired by **Leonora Carrington, Max Ernst, and Remedios Varo**. These artists are known for their **dreamlike and symbolic visuals**, aligning well with Jungian dream interpretation’s emphasis on the **unconscious mind**.  

---

## User Guide  

### **Input**  

1. Users type a **description of their dream** into the text area on the web page.  
2. After clicking the **submit button**, the AI processes the dream and generates both a **textual analysis** and a **visual representation**.  

### **Output**  

- The AI provides an **interpretation** of the dream’s images and symbols based on Jungian theories. Given the assistant’s **exaggerated arrogance**, responses may be **wildly inaccurate, humorous, and filled with strong opinions**.  
- An **AI-generated surrealist image**, inspired by the user’s dream, is displayed below the text response.  
- The user’s input remains in the text area after submission, allowing for **easy edits and re-submission** if desired.  

---

```
# Create virtual environment
python3 -m venv ./venv

# Activate your virtual environment
source venv/bin/activate

# Install the required packages. For example
pip3 install flask openai python-dotenv

# Rename the file .env-bup to .env. 
# Add your OPENAI_API_KEY to the .env file.

# Run the app
python3 app.py
```
