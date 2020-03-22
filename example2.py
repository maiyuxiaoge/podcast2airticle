from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
from google.oauth2 import service_account
from google.cloud.speech import types
import io
import speech_recognition as sr
import oauth2client
import googleapiclient
def sample_recognize(storage_uri):

    language_code = "en-US"

    sample_rate_hertz = 44100
    r = sr.Recognizer()
    with open("My First Project-4184c83023f8.json") as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()
    with sr.AudioFile(storage_uri) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    print(text)
    return text


# credentials = service_account.Credentials.from_service_account_file('My First Project-4184c83023f8.json')
storage_uri = 'part5.wav'
text = sample_recognize(storage_uri)