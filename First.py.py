import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import requests
import time
import threading
import re
import os
from dotenv import load_dotenv

load_dotenv()

def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        voices= engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
           print("Error:", e)
       
       
def wish_user():
    
        hour = int(datetime.datetime.now().hour)
        if hour < 12:
            speak(f"Good Morning {name}!")
            speak("I am your voice assistant. How can I help you today?")
        elif hour < 18:
            speak(f"Good Afternoon {name}!")
            speak("I am your voice assistant. How can I help you today?")
        else:
            speak(f"Good Evening {name}!")
            speak("I am your voice assistant. How can I help you today?")
def listen():
     recognizer = sr.Recognizer()
     recognizer.pause_threshold = 1.2 
     with sr.Microphone() as source:
          print("Listening...")
          audio = recognizer.listen(source)
          try:
               query = recognizer.recognize_google(audio)
               print("You said:", query)
               return query.lower()
          except:
               return ""

def parse_time(command):
       match = re.search(r'(\d+(?:\.\d+)?)\s*(seconds?|minutes?|hours?)',command.lower())
       if not match:
              return None
       value=float(match.group(1))
       unit=match.group(2)

       if "second" in unit:
              seconds=value
       elif "minute" in unit:
              seconds=value*60
       elif "hour" in unit:
              seconds=value*3600

       return int(seconds)

def start_timer(seconds):
       def timer():
                time.sleep(seconds)
                speak("Time's up!")
       threading.Thread(target=timer, daemon=True).start()

       if seconds<60:
                speak(f"Timer set for {seconds} seconds.")
       elif seconds<3600:
                speak(f"Timer set for {seconds // 60} minutes.")
       else:
                speak(f"Timer set for {seconds // 3600} hours.")
              
API_KEY=os.getenv("Openweather_api_key")


def get_weather(city):
       url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
       
       try:
              response = requests.get(url, timeout=10)
              data = response.json()
              if data["cod"]==200:
                     temp= data["main"]["temp"]
                     feels=data["main"]["feels_like"]
                     humidity=data["main"]["humidity"]
                     weather=data["weather"][0]["description"]
                     speak(f"The weather in {city} is {weather}.")
                     speak(f"The temperature is {temp} degrees Celsius.")
                     speak(f"It feels like {feels} degrees.")
                     speak(f"The humidity is {humidity}%.")
              else:
                            speak("Sorry,I couldn't find that city.")
       
       except requests.RequestException as e:
               print("Weather error:", e)
               speak("Sorry, I couldn't connect to the weather service.")
      


speak("Hello! What is your name?")
name=listen()

wish_user()
while True:
 command = listen()
 multiply_pattern=re.search(r'\d\s*x\s*\d', command)
 if "joke" in command:
     speak(pyjokes.get_joke())
 elif "time" in command and "timer" not in command:
      current_time = datetime.datetime.now().strftime("%H:%M")
      speak("The time is "+current_time)
 elif "wikipedia" in command:
               speak("Searching Wikipedia...")
               command = command.replace("wikipedia", "")
               try:
                    result = wikipedia.summary(command, sentences=5)
                    speak("According to Wikipedia:")
                    speak(result)
               except:
                    speak("Sorry, I couldn't find anything.")
 elif 'open youtube' in command:
              speak("Opening YouTube...")
              webbrowser.open("https://www.youtube.com/")
 elif 'open google' in command:
               speak("Opening Google...")
               webbrowser.open("https://www.google.com/")
 elif 'open spotify' in command:
               speak("Opening Spotify...")
               webbrowser.open("https://www.spotify.com/")
 elif 'play' in command:
               song=command.replace("play", "").strip()
               speak(f"Playing {song}")
               pywhatkit.playonyt(song)
 elif "weather" in command:
        speak("Which city?")
        city=listen()
        get_weather(city) 

 elif any(op in command for op in ["plus", "minus", "times", "multiplied by", "into", "divided by", "+", "-", "*", "/"]) or multiply_pattern:

        expression = command.replace("calculate", "")
        expression = expression.replace("what is", "")
        expression = expression.strip()
        expression = expression.replace("multiplied by", "*")
        expression = expression.replace("divided by", "/")
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("times", "*")
        expression = expression.replace("into", "*")
        expression=re.sub(r'(\d)\s*x\s*(\d)',  r'\1*\2', expression)
        try:
               result = eval(expression)
               print("Result :", result)
               speak(f"The answer is {result}")

        except Exception as e:
               print("Error :", e)
               speak("Sorry, I couldn't understand the calculation.")

 elif "timer" in command:
      seconds=parse_time(command)
  
      if seconds:
          start_timer(seconds)
      else:
          speak("Sorry, I couldn't understand the time duration.")      
 
 elif 'exit' in command or 'bye' in command or 'goodbye' in command:
                         speak(f"Goodbye {name}! Have a nice day!")
                         break