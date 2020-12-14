import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # To use a female voice


class Assistant:

    @classmethod
    def talk(cls, text):
        """
        Gets the user's speech
        """
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def take_command():
        """
        Processes the user's desired information
        according to the parameters
        """
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'assistant' in command:
                    command = command.replace('assistant', '')
                    print(command)
        except:
            pass
        return command

    @classmethod
    def run_assistant(cls):
        """
        uses processed information
        and responds as requested
        """
        command = Assistant.take_command()
        print(command)
        should_continue = True
        while should_continue:
            if 'play' in command:
                song = command.replace('play', '')
                cls.talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                cls.talk(f'Current time is {time}')
            elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                cls.talk(info)
            elif 'joke' in command:
                cls.talk(pyjokes.get_joke())
            elif 'stop' in command:
                should_continue = False
            else:
                cls.talk('Please say the command again.')


if __name__ == 'main':
    Assistant.run_assistant()
