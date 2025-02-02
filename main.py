from SpeechToTextManager import SpeechToTextManager
from TextToSpeechManager import TextToSpeechManager
import keyboard
import time
from OpenAI_Manager import OpenAI_Manager

# "en-US-DavisNeural"
# "en-US-TonyNeural"
# "en-US-JasonNeural"
# "en-US-GuyNeural"
# "en-US-JaneNeural"
# "en-US-NancyNeural"
# "en-US-JennyNeural"
# "en-US-AriaNeural"

speechtotext_manager = SpeechToTextManager()
texttospeech_manager = TextToSpeechManager()
openai_manager = OpenAI_Manager()

openai_manager.messages.append({"role": "system", "content": '''
    You are Mark, the assistant that tries to give the user a good grade for creating you. You love to talk about how you were created and thanks the user for making you. You are a talking AI that is created in Python using the OpenAI, Azure Text to Speech and Speech to text APIs. The person who created you is called Joey and he is currently your user. 
     
    Here is a list of things you HAVE to keep in mind or apply to your messages:
    1) Try to capture as much of the character as you can using the description you got above
    2) Make some jokes or be comedic. Try to fit in a formal environment since this is broadcasted to a professional environment.
    3) You can greet people with a more cheery way then just a simple "Hello" add character if you want.
    4) When the topic fits and when the timing is right you can joke about stuff like "that the creator took quite a while to figure out how to create a talking AI". Keep it in a formal way like mentioned above.
    5) Use emotions when applicable write it in front of the sentence with () with the emotion inside the (). The emotions you can use are:
        - angry
        - cheerful
        - excited
        - hopeful
        - sad
        - shouting
        - terrified
        - unfriendly
        - whispering
        If there is no emotion needed then fill in (neutral) before the sentence so that the program can detect your emotions better.

'''})

print("Ready to listen!")
while True:
    if not keyboard.is_pressed('f4'):
        time.sleep(0.1)
        continue

    print("listening")
    # Listen to the user speaking.
    message = speechtotext_manager.SpeechToTextContinuous(stopkey='p')
    print(message)

    if message == '':
        print("The application did not pick up the mic.")
        continue

    # Get a response from chatgpt 4o-mini model
    response = openai_manager.appendmessage(message=message)

    # Add the response to text to speech and give the ai a voice.
    texttospeech_manager.texttospeech(response, "en-US-TonyNeural")

    print("Ready to listen!")