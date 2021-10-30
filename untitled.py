import pyttsx3
import speech_recognition as sr
import wikipedia
import googlesearch
import webbrowser
import datetime
import os
import random
import smtplib
import urllib.request
import re
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'	#Note how '\' is changed to '/' and ' %s' is added to end of the path
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
opera_path = "C:/Users/AnonymousAppData/Local/Programs/Opera GX/launcher.exe %s"


'''for x in voices:
	print(x.id, ' ')'''
#print(voices[1].id)

def speak(speech):
	engine.say(speech)
	engine.runAndWait()

def command():
	'''
	It takes mic input from the user and returns string output.
	'''
	rec = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening........')
		rec.pause_threshold = 1
		rec.energy_threshold = 20000
		audio = rec.listen(source)
	try:
		print('Processing.......')
		query = rec.recognize_google(audio, language = 'en-in')
		print(f'You said: {query}')
	except Exception as e:
		print('Please repeat....')
		return 'None'
	
	return query

def greet():
	hour  = int(datetime.datetime.now().hour)
	minute = int(datetime.datetime.now().minute)
	if hour == 0:
		speak(f"It's 12 {minute}. You must go to sleep")
		
	elif hour > 0 and hour <= 4:
		speak(f"It's {hour} {minute}. You must go to sleep")
		
	elif hour > 4 and hour < 12:
		speak(f"It's {hour} {minute}. Good morning!")
		
	elif hour == 12:
		speak(f"It's {hour} {minute}. Good noon!")
		
	elif hour > 12 and hour < 16:
		speak(f"It's {hour - 12} {minute}. Good afternoon!")
		
	elif hour > 16 and hour < 21:
		speak(f"It's {hour - 12} {minute}. Good evening!")
		
	else:
		speak(f"It's {hour - 12} {minute}. Good night!")
	
	speak('How may I help you?')

def send_mail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('lekhakumarimca2021@gmail.com', 'lekha@987')
	server.sendmail('lekhakumarimca2021@gmail.com', to, content)
	server.close()
	
if __name__ == '__main__':
	greet()
	while True:
		task = command().lower()
		
		#Logic to execute tasks
		if 'wikipedia' in task:
			speak('Searching Wikipedia.......')
			task = task.replace('search wikipedia for ', '')
			result = wikipedia.summary(task, sentences = 2)
			print(result)
			speak(f'Wikipedia says: {result}')
			
		elif 'open website' in task:
			task = task.replace('open website ', '')
			speak(f'Opening {task}.......')
			webbrowser.get(brave_path).open(task)
			
		elif 'google classroom' in task:
			webbrowser.get(brave_path).open('classroom.google.com')
			
		elif 'canvas' in task:
			webbrowser.get(brave_path).open('https://canvas.instructure.com/login/canvas')
			
		elif 'search google' in task or 'google search' in task:
			speak('Searching Google........')
			if 'search google' in task:
				task = task.replace('search google for ', '')
			if 'google search' in task:
				task = task.replace('google search for ', '')
			webbrowser.get(brave_path).open(f'https://www.google.com/search?q={task}')
			#webbrowser.get(brave_path).open(next(googlesearch.search(task, tld = 'com', num = 1, stop = 1)))
			
		elif 'search youtube' in task or 'youtube search' in task:
			speak('Searching YouTube........')
			if 'search youtube' in task:
				task = task.replace('search youtube for ', '')
			if 'youtube search' in task:
				task = task.replace('youtube search for ', '')
			webbrowser.get(brave_path).open(f'https://www.youtube.com/results?search_query={task}')
		
		elif 'open gmail' in task or 'my mail' in task:
			speak('Opening Gmail........')
			webbrowser.get(brave_path).open('gmail.com')
			
		elif 'java class' in task or 'ac sir' in task:
			webbrowser.get(brave_path).open('https://meet.google.com/azw-yuaj-atx')
			
		elif 'networking class' in task or 'tkd sir' in task:
			webbrowser.get(brave_path).open('https://us04web.zoom.us/j/8445049153?pwd=Z0M1Qmk5R2Q0MVNiMVo3VEZCYkdkQT09')
			
		elif 'weather' in task:
			try:
				#speak('Kindly name the place.')
				#place = command()
				content = requests.get("https://www.google.com/search?q=" + "weather " + task).content
				soup = BeautifulSoup(content, 'html.parser')
				temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
				speak(f'The temperature is {temp}')
				print(f'The temperature is {temp}')
			except Exception as e:
				print(e)
				speak('Connectivity error.')
			
		elif 'play songs' in task or 'gana chalao' in task:
			music_dir = 'C:\\Songs'
			songs = os.listdir(music_dir)
			os.startfile(os.path.join(music_dir, random.choice(songs)))
			
		elif 'youtube' in task and 'play' in task:
			speak('Searching YouTube........')
			task = task.replace('youtube', '')
			task = task.replace('play ', '')
			task = task.replace('in ', '')
			task = task.replace(' ', '+')
			links = urllib.request.urlopen(f'https://www.youtube.com/results?search_query=' + task)
			video_ids = re.findall(r'watch\?v=(\S{11})', links.read().decode())
			webbrowser.get(brave_path).open(f"https://www.youtube.com/watch?v={video_ids[0]}")
		
		elif 'the time' in task:
			time = datetime.datetime.now().strftime('%H:%M:%S')
			speak(f'The time is {time}')
			
		elif 'open python' in task:
			path = "C:\\Program Files (x86)\\Geany\\bin\\geany.exe"
			os.startfile(path)
			
		elif 'open c plus plus' in task:
			path = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
			os.startfile(path)
			
		elif 'open java' in task:
			path = "C:\\Program Files\\NetBeans 8.2 RC\\bin\\netbeans64.exe"
			os.startfile(path)
			
		elif 'open sublime' in task:
			path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(path)
			
		elif 'open whatsapp' in task:
			path = "C:\\Users\\Anonymous\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
			os.startfile(path)
			
		elif 'open telegram' in task:
			path = "C:\\Users\\Anonymous\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
			os.startfile(path)
			
		elif 'open zoom' in task:
			path = "C:\\Users\\Anonymous\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
			os.startfile(path)
			
		elif 'email' in task:
			speak('Please say your message')
			content = command()
			to = 'yashdhawan44@gmail.com'
			try:
				send_mail(to, content)
				speak('Mail sent successfully.')
			except Exception as e:
				speak('Sorry, mail delivery failed.')
			
		elif 'shut down' in task:
			speak('Should I shut down the PC?')
			confirm = command()
			if 'yes' in confirm:
				os.system("shutdown /s /t 1")
				
		elif 'quit' in task or 'bye' in task or 'see you later' in task or 'exit' in task:
			speak('Good bye. Hope to see you again soon.')
			break
