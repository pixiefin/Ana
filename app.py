from flask import Flask, request, send_file
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

    # Send the audio file as a response
    return send_file(audio_file, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)