import keyboard
import os
import azure.cognitiveservices.speech as speechsdk

# ROOT\MEDIA\0006

speechrecognitionSetUp = False
class SpeechToTextManager:
    speechsdk = None
    audio_config = None
    speech_recognizer = None
    api_key = os.getenv('Azure_Api_Key')
    region = os.getenv('Azure_Region')

    def __init__(self):
        self.audio_config = speechsdk.audio.AudioConfig(device_name='{0.0.1.00000000}.{67C4E068-5714-445F-827A-42623B6735D6}')
        self.speech_config = speechsdk.SpeechConfig(subscription=self.api_key, region=self.region)
        self.speech_config.speech_recognition_language = "en-US"
        self.speech_config.set_profanity(speechsdk.ProfanityOption.Raw)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=self.audio_config)
        print('Azure set up.')

    def SpeechToTextContinuous(self, stopkey="p"):

        global speechrecognitionSetUp
        stopRecognizing = False

        def recognized_cb(evt: speechsdk.SpeechRecognitionEventArgs):
            print('RECOGNIZED: {}'.format(evt))
        if not speechrecognitionSetUp:
            self.speech_recognizer.recognized.connect(recognized_cb)
            speechrecognitionSetUp = True

        all_results = []

        def handle_final_result(evt):
            all_results.append(evt.result.text)
        self.speech_recognizer.recognized.connect(handle_final_result)

        result = self.speech_recognizer.start_continuous_recognition_async()
        result.get()

        while not stopRecognizing:
            if keyboard.is_pressed(stopkey):
                self.speech_recognizer.stop_continuous_recognition_async()
                stopRecognizing = True

        result = " ".join(all_results).strip()
        return result

if __name__ == '__main__':
    speechtotextManager = SpeechToTextManager()
    message = speechtotextManager.SpeechToTextContinuous()
    print(message)