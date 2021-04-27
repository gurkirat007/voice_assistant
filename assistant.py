#for speech recognition
import speech_recognition
#regular expressions library
import re
#wikipedia search library
import wikipedia
from googleapi import google
#covid19 data providing library
import COVID19Py
#text to speech library
import pyttsx3
from PyDictionary import PyDictionary

from googleapi import google
# Obtain audio from the microphone
recognizer = speech_recognition.Recognizer()
#text to speech line
engine = pyttsx3.init()
voices = engine.getProperty('voices')
dictionary=PyDictionary()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)
engine.setProperty("voice", voices[1].id)
print("What do you want to do?")
print("A.Type")
print("B.Speak(beta version)")
option=input("Type here\n")
#check whether to use voice recognition
def choice_of_voice_recognition(option):
	if option.lower()=="b":
		print("Ask")
		sentence=voice_recognition()
		print(sentence)
	elif option.lower()=="a":
		sentence=input("Ask\n")
	return sentence

def text_to_speech(reply):
	engine.say(reply)
	engine.runAndWait()


def voice_recognition():
	with speech_recognition.Microphone() as source:
		audio = recognizer.listen(source)
		sentence=recognizer.recognize_google(audio)
		return sentence

def covid_19_cases(country):
	covid19 = COVID19Py.COVID19(data_source="jhu")
	changes = covid19.getLatestChanges()
	latest = covid19.getLatest()
	location = covid19.getLocationByCountryCode(country)
	print("latest data worldwide")
	print(latest)
	print(f"cases in {country} (recovered is zero bcoz source stopped providing data)")
	print(location)
	print("changes since last updated")
	print(changes)

def google_search(sentence):
	num_page = 1
	search_results = google.search(sentence, num_page)
	print(search_results[0].description)




def wiki_search(sentence):
	page=wikipedia.page(sentence)	
	print(wikipedia.summary(sentence))
	text_to_speech(wikipedia.summary(sentence))
	print("for more info click on this link")
	text_to_speech("for more info click on this link")
	print(page.url)
	text_to_speech(page.url)

def dictionary(sentence):
	print (dictionary.meaning(sentence))

#loop to keep program working
while True:
	#voice assistant
	if option.lower()=="b":
		reply="Say something!"
		print(reply)
		text_to_speech(reply)
		sentence=voice_recognition()
		print(sentence)    
	#chatbot		
	elif option.lower()=="a":
		reply="say something"
		print(reply)
		text_to_speech(reply)
		sentence=input("")
		#key to exit program
	if re.search("Exit", sentence, re.IGNORECASE):
		break
	#some talks
	elif re.search("Hello|Hi", sentence, re.IGNORECASE):
		reply="Hello"
		text_to_speech(reply)
		print(reply)
	elif re.search("How", sentence, re.IGNORECASE):
		reply="I am fine, Thank you"
		print(reply)
		text_to_speech(reply)
	#covid19 data
	elif re.search("Case(s)", sentence, re.IGNORECASE):
		country=input("Please Enter your country code as per\nhttps://en.wikipedia.org/wiki/ISO_3166-1\n")
		covid_19_cases(country)
		
		
	#wikisearch
	elif re.search("Ask", sentence, re.IGNORECASE):
		print("what do you want to Ask")
		sentence=choice_of_voice_recognition(option)
		wiki_search(sentence)
	else:
		google_search(sentence)
		







