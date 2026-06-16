import speech_recognition as mic
import webbrowser as browse



import os as system 
name = "main"
def say(text):
   system.system(f"say {text}")



say("hello i am jarvis nilla kunda ")   
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
         return (" some error has occured salee chup kaar ja " )

# making funciton to activate the webbrowser on call 
def activatewebsite():
   browse.open.__new__(f"https://{data_of_voice}.com")  #making the voice command search on webbrowser 
   voice_of_conformation="the website has opened successfully in the browser"
   say(voice_of_conformation)

      
      
    
      
      
#main function      
if name == "main":
      say("hello i am jarvis ")
      while True:
       print("listening")
       data_of_voice =voicecommand()
       say(data_of_voice)
       if "open site" in data_of_voice.lower():     #checking if the funciton contains the voice
          activatewebsite(data_of_voice)