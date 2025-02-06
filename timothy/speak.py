from tts import TTS

tts = TTS(engine="espeak")
tts.lang("en-US")

def main():
    tts.say("Hello, nice to meet you!")
    while True:
        pass

def destroy():
    tts.say("What would you like me to say?")
    tts.say(input("What would you like me to say?"))
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()