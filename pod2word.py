from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
from google.oauth2 import service_account
from google.cloud.speech import types
import io
import speech_recognition as sr
import oauth2client
import googleapiclient
def sample_recognize(storage_uri,credentials):

    client = speech_v1p1beta1.SpeechClient(credentials = credentials)
    language_code = "en-US"


    r = sr.Recognizer()
    with open("My First Project-4184c83023f8.json") as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()
    offset = 0
    with sr.AudioFile(storage_uri) as source:
        length = source.FRAME_COUNT/source.SAMPLE_RATE
        while offset < length:
            audio = r.record(source,duration = 15,offset = offset)
            text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            offset += 15
            print(text)

credentials = service_account.Credentials.from_service_account_file('My First Project-4184c83023f8.json')
storage_uri = 'cse253.wav'
sample_recognize(storage_uri,credentials)