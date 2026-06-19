import speech_recognition as mic
import webbrowser as browse
import subprocess as apps
from pathlib import Path as files 
from openai import OpenAI as AI
import wikipedia as know
import os as system 
voice_of_conformation=""
name = "main"
pdf = "open pdf"
def say(text):
   system.system(f"say {text}")

speak="information not available"

say("hello i am jarvis  ")   
text = "something"
def voicecommand():
 with mic.Microphone as start: 
      check=mic.Recognizer() 
      check.pause_threshold=1
      check.adjust_for_ambient_noise(start, duration=0.2)
      print ("please start speaking ") 
      audio= check.listen(start)
      try:
       amendment=check.recognize_amazon(audio)
       print(f"ahcaa or kiaa is ke ilaawa{amendment}")
       return amendment
      except Exception as q:
         return (" some error has occured  " )

# making funciton to activate the webbrowser on call 
def activatewebsite():
   browse.open.__new__(f"https://{data_of_voice}.com")  #making the voice command search on webbrowser 
   voice_of_conformation="the website has opened successfully in the browser"
   say(voice_of_conformation)

def ok ():
   command= " ok sir "
   say(command)
#opening the apps 


def openingapps():
   apps.Popen([data_of_voice])
   voice_of_conformation= "the apps is opened successfully"
   say(voice_of_conformation) # to conforthe voice 
   print ("the app has opened ")

    
      
# making a use of open AI    
def AI_response():
   know.wikipedia(data_of_voice)
   if data_of_voice in know.wikipedia:
      speak="yes this infoemation is available"
      say(speak)
   else:
      say(speak)   

def opening_text_files(txtfile):                 # for opening text files 
    ok()
    for file in files.home().rglob("*.txt"):
      if txtfile.lower in file.name.lower():
         system.startfile(file)
         print("opening file ",file)
         break

def opening_pdf_files(pdffile):
   ok()
   for file in files.home().rglob("*.pdf"):    #opening pdf files
      if pdffile.lower in file.name.lower():
         system(file)
         voice_of_conformation="the  pdf file has opened successfully "
         say(voice_of_conformation) 
         break
    



#main code    
if name == "main":
      say("hello i am jarvis ")
      while True:
       print("listening")
       data_of_voice =voicecommand()
       say(data_of_voice)
       if "open site" in data_of_voice.lower():     #checking if the funciton contains the voice
          activatewebsite(data_of_voice)
       if "open app " in data_of_voice.lower(): # openning the app   
         openingapps(data_of_voice)
       if "tell me " in data_of_voice.lower():
          AI_response(data_of_voice)
       if "open text files" in data_of_voice.lower():   # opening a txt files through search 
            matter = data_of_voice
            opening_text_files(matter)
       if open in data_of_voice.lower():
            matter=data_of_voice
            opening_pdf_files(matter)
          