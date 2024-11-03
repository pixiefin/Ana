from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from gtts import gTTS
from io import BytesIO
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message Received from Client: ' + msg)
    processMessage(msg)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def convertToSpeech(msg):
    print("Converting Text : ", msg)

    audio_byte_stream = BytesIO()

    tts = gTTS(msg, lang='en')
    tts.write_to_fp(audio_byte_stream)
    audio_byte_stream.seek(0)
    return audio_byte_stream.getvalue()

def handleWord(word, process=True):
    speech = convertToSpeech(word)
    emit('audio_event', speech)
    emit('text_event', word)
    
def processMessage(msg):
    tokenized = msg.split()
    if len(tokenized) == 1 :
        handleWord(tokenized[0])
    else :
        #check later -- tell Vikas on the issue
        tokenized.append("-")
        for word in tokenized[:-1]:
            time.sleep(1)
            handleWord(word)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port=8083)