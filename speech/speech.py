import pyttsx3

RATE = 145

engine = pyttsx3.init()
engine.setProperty('rate', RATE)


def speech_out_msg(message):
    engine.say(message)

    engine.runAndWait()
    engine.stop()
