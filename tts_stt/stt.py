import vosk
import sys
import sounddevice as sd
import queue
import json
from datetime import datetime, timedelta

from tts_stt.stt_config import VA_ALIAS, VA_CMD_LIST
from tts_stt.commands import recognize_cmd, va_functions, va_speak


model = vosk.Model(model_name="vosk-model-small-ru-0.22")
samplerate = 48000
device = 1

q = queue.Queue()
none_stop = True
any_q = False
extra_params = ''


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def stt(voice):
    global none_stop
    global any_q
    global extra_params
    if any_q:
        if voice == '':
            print('waiting')
            if datetime.now() >= any_q:
                any_q = False
                va_speak('olivia_cancel1')
        else:
            print(voice)
            none_stop = VA_CMD_LIST[extra_params]['non-stop']
            misunderstood = va_functions[extra_params](voice)
            if misunderstood:
                va_speak('olivia_misunderstood1')
                any_q = datetime.now() + timedelta(seconds=7)
            else:
                extra_params = ''
                any_q = False
    else:
        if voice.startswith(VA_ALIAS):
            print(voice)
            cmd = voice
            for x in VA_ALIAS:
                cmd = cmd.replace(x, '').strip()
            cmd_ = recognize_cmd(cmd, VA_CMD_LIST)
            command = cmd_['cmd']
            print(f'команда: {command}')
            if command:
                if VA_CMD_LIST[command]['extra']:
                    print(VA_CMD_LIST[command]['extra'])
                    va_speak(VA_CMD_LIST[command]['extra'])
                    extra_params = command
                    any_q = datetime.now() + timedelta(seconds=7)
                elif VA_CMD_LIST[command]['params']:
                    print(VA_CMD_LIST[command]['params'])
                    va_functions[command](VA_CMD_LIST[command]['params'])
                else:
                    va_functions[command]()
                none_stop = VA_CMD_LIST[command]['non-stop']
            else:
                va_speak('olivia_repeat1')
                none_stop = True
        elif voice == 'проверка':
            print(voice)
            any_q = datetime.now() + timedelta(seconds=5)


def listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while none_stop:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])


if __name__ == '__main__':
    listen(stt)
