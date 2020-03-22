from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
from google.oauth2 import service_account
from google.cloud.speech import types
import io
def sample_recognize(storage_uri,credentials):

    client = speech_v1p1beta1.SpeechClient(credentials = credentials)
    language_code = "en-US"

    sample_rate_hertz = 48000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.mp3'
    # encoding = enums.RecognitionConfig.AudioEncoding.MULAW
    encoding = enums.RecognitionConfig.AudioEncoding.MP3
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    # with io.open(storage_uri, "rb") as f:
    #         content = f.read()
    audio = {"uri": storage_uri}
    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))


credentials = service_account.Credentials.from_service_account_file('My First Project-4184c83023f8.json')
storage_uri = 'part5.wav'
sample_recognize(storage_uri,credentials)
