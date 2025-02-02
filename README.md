# ChattyAI
An AI you can talk to. Made in Python version 3+.

<h3>How to set it up:</h3>
The program uses keys and regions from OpenAI and Azure. Set up your credit card and subscriptions on those services before using this program. 

1) Download Python version 3+.
2) Download the python source code.
3) Go to windows settings.
4) Go to the about section.
5) Go to Advance Settings.
6) Go to Environment Variables.
7) Make the variables Azure_Api_Key, Azure_Region and Open_API_Key and set the correct keys and region.
8) Test it out if it works.

If you are using a mac or other non-windows devices. Look into how you can set environment variables for those devices. You can also hardcode the keys and regions by replacing functions like os.getenv('Azure_Api_Key') with your keys and regions and that should also work.

<h3>How to use:</h3>
When you start the application. Press the f4 button to have the program start listening to you. When you are done speaking wait until you see the "recognized speech" line in the terminal before stopping with p. After you stop the listening phase with p the program will send the data to OpenAI and the response from ChatGPT will be said out loud with Azure Text to Speech.

In the main file. You can change the buttons and the AIs behaviour by changing the AI description in openai_manager.messages.append({}). There is already an example ready for you to look at and change. If you scroll down you should see keyboard.is_pressed('f4') and speechtotext_manager.SpeechToTextContinuous(stopkey='p'). You can change 'f4' and 'p' to any key you prefer. Lastly you can change the voice by choosing any voice at the top of the main file like #"en-US-DavisNeural" and replacing the current voice in texttospeech_manager.texttospeech(response, "en-US-TonyNeural"). For more questions contact me.