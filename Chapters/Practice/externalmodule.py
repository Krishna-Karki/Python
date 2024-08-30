import pyttsx3

engine = pyttsx3.init()

line1 = "Mother,Fucker"
rate = engine.getProperty('rate')
engine.setProperty('rate',80)
engine.say(line1)

line = "Mr krishna karki, nigga"

rate = engine.getProperty('rate')
engine.setProperty('rate',200)

volume = engine.getProperty('volume')
engine.setProperty('volume',volume*2)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[9].id)
engine.say(line)
engine.runAndWait()