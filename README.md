# Python-Learnings
I have adding files here which are whatever I have learned day by day.
#Text to audio# In this basic project with online help I have created this project:
from gtts import gTTS
import os
mytext = "Python has a simple syntax similar to the English language. Python has syntax that allows developers \n" \
         "to write programs with fewer lines than some other programming languages. Python runs on an interpreter system,\n" \
         " meaning that code can be executed as soon as it is written. This means that prototyping can be very quick"
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save('welcome.mp3')
os.system("welcome.mp3")
