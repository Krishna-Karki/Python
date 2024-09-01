import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

# Initialize necessary components
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "5a6b18e78afe4338839cf842ea491879"  # Ensure your API key is handled securely

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music.get(song)  # Assuming musiclibrary is defined somewhere with a music dictionary
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in the music library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")

        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news right now.")

def voice_mode():
    speak("Voice command mode activated.")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)
            
            # Try recognizing the audio
            try:
                command = recognizer.recognize_google(audio)
                print(f"Heard: {command}")
                
                if "jarvis" in command.lower():
                    speak("What's up?")
                    with sr.Microphone() as source:
                        print("Listening for your command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print(f"Command received: {command}")
                        processCommand(command)
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")
        
        except Exception as e:
            print(f"Error: {e}")
            break  # Break the loop if an unexpected error occurs

def text_mode():
    speak("Text command mode activated.")
    while True:
        command = input("Enter your command: ").strip()
        processCommand(command)

if __name__ == "__main__":
    # Ask for the mode once at the start
    mode = input("Type 'voice' for voice command or 'text' for text command: ").strip().lower()

    if mode == "voice":
        voice_mode()
    elif mode == "text":
        text_mode()
    else:
        print("Invalid mode selected. Please restart the program and choose 'voice' or 'text'.")
