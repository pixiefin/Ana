from flask import Flask, request, send_file, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/speak', methods=['POST'])
def speak():
    # Get the text from the POST request
    data = request.get_json()
    text = data.get('text')

    if not text:
        return "No text provided", 400

    # Convert text to speech
    tts = gTTS(text, lang='en')
    audio_file = "speech.mp3"
    tts.save(audio_file)

    # Create a JSON response including the text and the audio file
    response = {
        'text': text,
        'audio_file': os.path.abspath(audio_file)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
