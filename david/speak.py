from tts import TTS

tts = TTS(engine="espeak")
tts.lang("en-US")

def main():
    tts.say("NOOOOOO00000000000")
    while True:
        pass
    
def destroy():
    tts.say("See you later")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()