from tts import TTS

tts = TTS(engine="espeak")
tts.lang("en-US")
A = input("give a word you would like to say: ")
def main():
    tts.say(A)
    while True:
        pass
    
def destroy():
    tts.say("See you later")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()