from time import sleep

import torch
from playsound import playsound
import soundfile


language = 'ru'
model_id = 'v4_ru'
device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)  # gpu or cpu

ssml_sample = '''
              <speak>
              <p>
                  Когда я просыпаюсь, <prosody rate="x-slow">я говорю довольно медленно</prosody>.
                  Потом я начинаю говорить своим обычным голосом,
                  <prosody pitch="x-high"> а могу говорить тоном выше </prosody>,
                  или <prosody pitch="x-low">наоборот, ниже</prosody>.
                  Потом, если повезет – <prosody rate="fast">я могу говорить и довольно быстро.</prosody>
                  А еще я умею делать паузы любой длины, например две секунды <break time="2000ms"/>.
                  <p>
                    Также я умею делать паузы между параграфами.
                  </p>
                  <p>
                    <s>И также я умею делать паузы между предложениями</s>
                    <s>Вот например как сейчас. Я супер заебись</s>
                  </p>
              </p>
              </speak>
              '''

sample_rate = 48000
speaker = 'xenia'
audio = model.apply_tts(ssml_text=ssml_sample,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=True,
                        put_yo=True)

soundfile.write('test1.wav', audio, sample_rate)
sleep(5)
playsound('test1.wav')
