import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('RSITO0-dy5M80Bl7eM7AkSSWXWkmuID6DJKN3q18JjQl')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/381cb3e1-1245-422c-a4b9-4a4480314571')

with open(join(dirname(__file__), './.', 'hello_world.wav'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav',
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))
