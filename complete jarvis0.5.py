import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import requests
import os
import platform
import subprocess
import random

class VoiceAssistant:
    def __init__(self):
        """Initialize the voice assistant."""
        try:
            self.engine = pyttsx3.init('sapi5')  # Windows ke liye
        except:
            self.engine = pyttsx3.init()
        
        self.setup_voice()
        self.recognizer = sr.Recognizer()
        
    def setup_voice(self):
        """Configure voice to female and set properties."""
        try:
            voices = self.engine.getProperty('voices')
            
            # Set female voice
            for voice in voices:
                if 'female' in voice.name.lower() or 'zira' in voice.name.lower() or 'hazel' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
            else:
                if len(voices) > 1:
                    self.engine.setProperty('voice', voices[1].id)
            
            # Set speech properties
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 1.0)
            
        except Exception as e:
            print(f"Voice setup error: {e}")
    
    def speak(self, text):
        """Make the assistant speak AND print."""
        print(f"🔊 Assistant: {text}")  # Print bhi karega
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            self.engine.stop()
        except Exception as e:
            print(f"Speech error: {e}")
    
    def listen(self):
        """Listen to user voice input and convert to text."""
        with sr.Microphone() as source:
            print("🎤 Listening...")  # Print notification
            self.speak("Listening")  # Voice notification
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                return ""
        
        try:
            print("🔎 Recognizing...")  # Print status
            command = self.recognizer.recognize_google(audio, language="en-in")
            print(f"👉 You said: {command}")  # Print what user said
            self.speak(f"You said {command}")  # Voice confirmation
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that. Please repeat.")
            return ""
        except sr.RequestError:
            self.speak("Network error. Please check your internet connection.")
            return ""
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""
    
    def get_time(self):
        """Get current time."""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        self.speak(f"The time is {time_str}")
    
    def get_date(self):
        """Get current date."""
        today = datetime.date.today()
        date_str = today.strftime("%A, %B %d, %Y")
        self.speak(f"Today is {date_str}")
    
    def get_weather(self, city="Meerut"):
        """Get weather information."""
        try:
            url = f"http://wttr.in/{city}?format=%C+%t"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                weather_info = response.text.strip()
                self.speak(f"The weather in {city} is {weather_info}")
            else:
                self.speak("Sorry, I couldn't fetch the weather information.")
        except:
            self.speak("Unable to get weather information. Please check your internet connection.")
    
    def open_application(self, app_name):
        """Open applications."""
        system = platform.system()
        app_name = app_name.lower()
        
        apps = {
            'notepad': {'Windows': 'notepad.exe'},
            'calculator': {'Windows': 'calc.exe'},
            'browser': {'Windows': 'start chrome'},
            'chrome': {'Windows': 'start chrome'},
            'file explorer': {'Windows': 'explorer'},
            'explorer': {'Windows': 'explorer'},
            'paint': {'Windows': 'mspaint.exe'},
            'word': {'Windows': 'start winword'},
            'excel': {'Windows': 'start excel'}
        }
        
        try:
            if app_name in apps and system in apps[app_name]:
                os.system(apps[app_name][system])
                self.speak(f"Opening {app_name}")
            else:
                self.speak(f"Sorry, I don't know how to open {app_name} on this system")
        except:
            self.speak(f"Could not open {app_name}")
    
    def web_search(self, query):
        """Search the web."""
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        self.speak(f"Here are the search results for {query}")
    
    def open_website(self, site):
        """Open popular websites."""
        websites = {
            'youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'gmail': 'https://mail.google.com',
            'facebook': 'https://www.facebook.com',
            'twitter': 'https://www.twitter.com',
            'instagram': 'https://www.instagram.com',
            'whatsapp': 'https://web.whatsapp.com',
            'linkedin': 'https://www.linkedin.com'
        }
        
        if site in websites:
            webbrowser.open(websites[site])
            self.speak(f"Opening {site}")
        else:
            self.speak(f"Sorry, I don't have {site} in my quick access list")
    
    def tell_joke(self):
        """Tell a random joke."""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They would crack each other up!",
            "What did the ocean say to the beach? Nothing, it just waved!"
        ]
        self.speak(random.choice(jokes))
    
    def process_command(self, command):
        """Process user commands."""
        if not command:
            return True
        
        # Greetings
        if any(word in command for word in ['hello', 'hi', 'hey', 'greetings']):
            self.speak("Hello! How can I assist you today?")
        
        # Time - FIXED
        elif 'time' in command and 'weather' not in command:
            self.get_time()
        
        # Date - FIXED
        elif 'date' in command or 'today' in command or 'what day' in command or 'day is' in command:
            self.get_date()
        
        # Weather
        elif 'weather' in command:
            if 'in' in command:
                city = command.split('in')[-1].strip()
                self.get_weather(city)
            else:
                self.get_weather()
        
        # Open applications
        elif 'open' in command:
            app = command.replace('open', '').strip()
            # Check if it's a website
            if any(site in app for site in ['youtube', 'google', 'gmail', 'facebook', 'twitter', 'instagram', 'whatsapp', 'linkedin']):
                for site in ['youtube', 'google', 'gmail', 'facebook', 'twitter', 'instagram', 'whatsapp', 'linkedin']:
                    if site in app:
                        self.open_website(site)
                        break
            else:
                self.open_application(app)
        
        # Web search
        elif 'search for' in command or 'search' in command:
            if 'search for' in command:
                query = command.split('search for')[-1].strip()
            else:
                query = command.split('search')[-1].strip()
            
            if query:
                self.web_search(query)
            else:
                self.speak("What would you like me to search for?")
                query = self.listen()
                if query:
                    self.web_search(query)
        
        # Tell a joke
        elif 'joke' in command:
            self.tell_joke()
        
        # Who are you
        elif 'who are you' in command or 'what is your name' in command:
            self.speak("I am your personal voice assistant, inspired by Jarvis. I'm here to help you with various tasks!")
        
        # Help command
        elif 'help' in command or 'what can you do' in command:
            self.speak("I can help you with many things. You can ask me to tell the time or date, check the weather, open applications like notepad, calculator, or browser, search the web, open websites like YouTube or Google, tell you a joke, and much more!")
        
        # Exit commands
        elif any(word in command for word in ['exit', 'quit', 'bye', 'goodbye', 'stop']):
            self.speak("Goodbye! Have a wonderful day!")
            return False
        
        # Unknown command
        else:           
            self.speak("I'm not sure how to help with that. Try asking for help to see what I can do.")
        
        return True
    
    def run(self):
        """Main assistant loop."""
        print("=" * 50)
        print("🤖 VOICE ASSISTANT STARTING...")
        print("=" * 50)
        self.speak("Voice assistant activated. How may I help you?")
        
        while True:
            try:
                command = self.listen()
                if not self.process_command(command):
                    break
            except KeyboardInterrupt:
                print("\n⚠️ Keyboard interrupt detected!")
                self.speak("Shutting down. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error occurred: {e}")
                self.speak("An error occurred. Please try again.")

# Run the assistant
if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()