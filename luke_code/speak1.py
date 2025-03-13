from tts import TTS

tts = TTS(engine="espeak")
tts.lang("en-US")
def main():
    tts.say("AHH")
    

    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()