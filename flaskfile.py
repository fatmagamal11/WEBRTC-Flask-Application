from flask import Flask, request, render_template
from flask import Flask, render_template, jsonify
import speech_recognition as sr
import pyttsx3

# app.py

app_skill=Flask(__name__,template_folder='template')




@app_skill.route('/recognize_speech', methods=['POST'])
def recognize_speech():
    recognizer=sr.Recognizer()
    while True:
        
        try:
            with sr.Microphone()as mic:
                print("Say something...")
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)
                text=recognizer.recognize_google(audio)
                text=text.lower()        
                print(text+"\t")
        except sr.UnknownValueError():
            recognizer=sr.Recognizer()
            continue
# @app_skill.route('/lobby')
# def home():
#     return render_template("lobby.html")
@app_skill.route('/')
def home():
    return render_template("home.html")

@app_skill.route('/index.html')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app_skill.run(debug=True, port=9000)
