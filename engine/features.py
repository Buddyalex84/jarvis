from playsound import playsound
import eel
#play assistance sound function
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\vendorus\\texllate\\audio\\jarvis-147563 (mp3cut.net).mp3"
    playsound(music_dir)