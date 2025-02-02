import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# {0.0.1.00000000}.{67C4E068-5714-445F-827A-42623B6735D6}
# start_continuous_recognition_async

def TestAzureSpeechToTextToggle(api_key, region):
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.audio.AudioConfig(device_name='{0.0.1.00000000}.{67C4E068-5714-445F-827A-42623B6735D6}')
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Set timeout durations
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs,
                                              "10000")  # default 60 seconds
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs,
                                              "2000")  # default 20 seconds

    print("Speak into your microphone now. Say 'stop session' to end")

    while True:
        speech_recognition_result = speech_recognizer.start_continuous_recognition().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print('Recognized: {}'.format(speech_recognition_result.text))
            if "stop session" in speech_recognition_result.text.lower():
                print("Session ended by user.")
                break
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

def TestAzureSpeechToText(api_key, region):
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.audio.AudioConfig(device_name='{0.0.1.00000000}.{67C4E068-5714-445F-827A-42623B6735D6}')
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Set timeout durations
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "10000") # default 60 seconds
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "2000") # default 20 seconds

    print("Speak into your microphone now. Say 'stop session' to end")

    while True:
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print('Recognized: {}'.format(speech_recognition_result.text))
            if "stop session" in speech_recognition_result.text.lower():
                print("Session ended by user.")
                break
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

load_dotenv()

api_key = os.getenv("api_key")
region = os.getenv("region")

TestAzureSpeechToText(api_key, region)