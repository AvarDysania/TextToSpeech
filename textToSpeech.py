#This Is Google text to speech api
from gtts import gTTS
import os
  
mytext="";
# The text that you want to convert to audio
file=open("test.txt","r",encoding="utf-8");
mytext=file.read();
  
# Language in which you want to convert
language = 'en'

''' here we have marked slow=False. Which tells 
the module that the converted audio should 
 have a high speed'''
 
myobj = gTTS(text=mytext, lang=language, slow=False)
#Saving The Mp3 file in audio
myobj.save("welcome.mp3")
  
# Playing Mp3 audio
os.system("welcome.mp3");