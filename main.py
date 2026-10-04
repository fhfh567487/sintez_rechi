import pyttsx3
engine = pyttsx3.init()

rate=int(input('ведите кол-во слов в минуту '))
engine.setProperty('rate', rate )     # setting up new voice rate

engine.say(input('ведите текст '))
engine.runAndWait()
engine.stop()
