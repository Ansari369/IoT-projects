from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('ZmfQSpS-m85wNBln69v_ojQDkFIlhJMIrQP3w5Y3hegP')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/3e6111c0-3fec-4fe0-92d2-61e9250fc06b')

with open('hello_world.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'hey you, yes you ansari',
            voice='en-US_AllisonVoice',
            accept='audio/mp3'        
        ).get_result().content)

playsound('hello_world.mp3')
