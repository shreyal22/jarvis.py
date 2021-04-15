import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import calculator
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
   engine.say(audio)
   engine.runAndWait()
def wishme():
   hour=int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
       speak("good morning sir")
       speak("as you know i am jarvis , do you want to work today or chill sir?")
   elif hour>=12 and hour<=17:
       speak("good afternoon sir")
       speak("jarvis here sir,what to you want me to do sir?")
   else:
       speak("very good evening sir,its jarvis")
       speak("how do you want to spend your evening,i can make arrangements for you sir")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speak("go ahead sir,i am listening")
        r.pause_threshold=1
        r.energy_threshold=200
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"sir said: {query}\n")


    except Exception as e:
        print("Say that again please!")
        speak("say again sir")
        query="None"
    return query
if __name__=="__main__":
 wishme()
while True:
      query=takeCommand().lower()
      if "wikipedia" in query:
            speak("searching wikipedia sir")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia sir")
            speak(result)
            print(result)
            continue

      elif "google" in query:
        webbrowser.open("https://www.google.co.in/")
        continue
      elif "calculate" in query:
          query.split()
          q=query[2:]

          r=(eval(q))
          speak(r)

      elif "youtube" in query:
          webbrowser.open("https://www.youtube.com/?gl=IN&tab=w1")
          continue
      elif "instagram" in query:
          webbrowser.open("https://www.instagram.com/?hl=en")
          continue
      elif "geeks for geeks" in query:
          webbrowser.open("https://www.geeksforgeeks.org/")
          continue
      elif "hotstar"  in query:
          webbrowser.open("https://www.hotstar.com/in")
          break
      elif "prime videos" in query:
          webbrowser.open("https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_67|m_woIqHOSOc_c386559716628")
          break
      elif "spotify" in query:
          webbrowser.open("spotify.com")
          continue
      elif  "amazon" in query:
          webbrowser.open("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
          break
      elif "flipkart" in query:
          webbrowser.open("https://www.flipkart.com/")
          break
      elif "play music" in query:
           playlist='C:\\bts'
           song=os.listdir(playlist)
           os.startfile(os.path.join(playlist,random.choice(song)))
           speak("enjoy bts sir")
           break
      elif "change music" in query:
                  playlist='C:\\bts'
                  song=os.listdir(playlist)
                  os.startfile(os.path.join(playlist,random.choice(song)))
                  break
      elif "time" in query:
          strTime=str(datetime.datetime.now().strftime("%H:%M:%S"))
          speak(strTime)
          continue
      elif "what are you doing" in query:
          speak("just chillin and enjoying life for some time sir as you give me so much work")
          continue
      elif "shut up" in query:
          speak("fine,but you will need me later sir")
          break
      elif  "talk" in query:
          speak("i am also not very fond sir but you made me so i have to")
          continue
      elif "thank you" in query:
          speak("your welcome sir")
          break
      elif "quit" in query:
          speak("all right sir,switching to battery saver mode")
          break
      elif "temperature" in query:
          tem=webbrowser.open("https://www.google.com/search?q=temperature+in+chittorgarh&oq=temp&aqs=chrome.0.69i59j0i433j69i57j0i131i433j0i433j0j69i60l2.4241j1j7&sourceid=chrome&ie=UTF-8")
          speak(tem)
          continue
      elif "photos" in query:
          webbrowser.open("https://photos.google.com/?tab=rq&pageId=none")
      elif "good job" in query:
          speak("really?   thank you sir,you hardly appreciate but i really appreciate that you have appreciated me sir")
          break
      elif "bye" in query:
          speak("bye bye sir")
          break
      elif "specifications"  in query:
          speak("my name is jarvis sir which is the short form of just a rather very intelligent system called jarvis, i am intel core i3-1005g1,CPU @ 1.20 GHz and 8 GB RAM")
          continue
      elif "what can " in query:
          speak("anything and everything sir")
      elif "rain" in query:
          webbrowser.open("https://www.google.com/search?q=will+it+rain+today&gs_ivs=1#tts=0")
      elif "meetings" in query:
          speak("showing sir")
          webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
      elif "news" in query:
          webbrowser.open("https://news.google.com/topstories?tab=Cn&hl=en-IN&gl=IN&ceid=IN:en")
