from tts import TTS

tts= TTS(engine="espeak")
tts.lang("en-US")

def main():
    tts.say("I saw a saw in Arkansas, that could outsaw any saw you ever saw, if you think that you could find a saw that could outsaw the saw that i saw in Arkansas, then that saw has to outsaw every saw in the world")
    while True:
        pass

def destroy():
    tts.say("See you later")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            destroy()