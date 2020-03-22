import pydub 
import pyaudio
import json
from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
from google.oauth2 import service_account

class podcast2word(object):
    def __init__(self,file):
        self.file = file
        self.audios = []
        self.translations = []
        self.frame_rate = 0
        self.encoding = enums.RecognitionConfig.AudioEncoding.MP3
        self.credentials = service_account.Credentials.from_service_account_file('My First Project-4184c83023f8.json')

    def segmentmp3(self):
        sound = pydub.AudioSegment.from_mp3(self.file)
        self.audios = pydub.silence.split_on_silence(sound,min_silence_len=300,silence_thresh=-70)

    def trans_one_audio(self,audio):
        self.frame_rate = audio.frame_rate
        client = speech_v1p1beta1.SpeechClient(credentials = self.credentials)
        encoding = enums.RecognitionConfig.AudioEncoding.MP3
        config = {
                "language_code": "en-US",
                "sample_rate_hertz": self.frame_rate,
                "encoding": encoding,
                }
        # audio = {"uri": storage_uri}
        response = client.recognize(config, audio)
        for result in response.results:
            alternative = result.alternatives[0]
            print(u"Transcript: {}".format(alternative.transcript))
        return alternative

    def trans_audios(self):
        for audio in self.audios:
            temp = self.trans_one_audio(audio)
            self.translations.append(temp)
            print(temp)

    def save_translations(self):
        pass

cse = podcast2word('cse253.mp3')
cse.segmentmp3()
print(cse.trans_one_audio(cse.audios[0]))
# cse.trans_audios()
