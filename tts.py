import torch
import sounddevice as sd

from recorder import record

language = 'ru'
model_id = 'v4_ru'
device = torch.device('cpu')

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)  # gpu or cpu

ssml_sample = '''
              <speak>
              <p>
                  <s>не разобрала</s>
                  <s>повтори параметры</s>
              </p>
              </speak>
              '''

sample_rate = 48000
speaker = 'xenia'  # aidar, baya, kseniya, xenia, random


def speak(text, recorder=False, file_name='', play=True):
    audio = model.apply_tts(ssml_text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=True,
                            put_yo=True)
    if play:
        sd.play(audio, sample_rate * 1.05)
        sd.wait()
        sd.stop()
    if recorder:
        record(audio, sample_rate, file_name)


def va_play(audio, sample_rate):
    sd.play(audio, sample_rate)
    sd.wait()
    sd.stop()


if __name__ == '__main__':
    speak(ssml_sample, True, 'voices/olivia_misunderstood1')
