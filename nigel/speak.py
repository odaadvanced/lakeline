from tts import TTS

tts = TTS(engine="espeak")
tts.lang("en-US")

def main():
    tts.say("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    while True:
        pass
    
def destroy():
    tts.say("I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, I hope you die, ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()
        
