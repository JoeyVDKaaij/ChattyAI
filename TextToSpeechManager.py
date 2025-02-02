import os
import azure.cognitiveservices.speech as speechsdk
import re


class TextToSpeechManager:
    audio_config = None
    speech_config = None
    speech_synthesizer = None

    api_key = os.getenv('Azure_Api_Key')
    region = os.getenv('Azure_Region')

    def __init__(self):
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.speech_config = speechsdk.SpeechConfig(subscription=self.api_key, region=self.region)
        self.speech_config.speech_recognition_language = "en-US"
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)

    def texttospeech(self, text: str, voice='en-US-DavisNeural'):
        # Regular expression to match sentences with or without emotions
        pattern = r"(?:\((.*?)\))?\s*([^()]+(?:[!?]+)?)"

        # Find all matches
        matches = re.findall(pattern, text)

        # Convert matches into a list of dictionaries
        results = [{"emotion": emotion if emotion else "neutral", "sentence": sentence.strip()} for emotion, sentence in
                  matches]

        print(results)

        ssml_start = (f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts' xmlns:emo='http://www.w3.org/2009/10/emotionml' xml:lang='en-US'>"
                        f"<voice name='{voice}'>")
        ssml_end = (f"</voice></speak>")
        ssml_body = ""
        for result in results:
            ssml_body += (f"<mstts:express-as style='{result["emotion"]}'>"
                                f"{result["sentence"]}</mstts:express-as>")

        ssml_text = ssml_start + ssml_body + ssml_end
        self.speech_synthesizer.speak_ssml(ssml_text)


if __name__ == '__main__':
    texttospeechManager = TextToSpeechManager()
    texttospeechManager.texttospeech("(sad) hello there. (neutral) Who are you. (angry) why are you here??")