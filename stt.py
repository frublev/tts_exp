import vosk
import sys
import sounddevice as sd
import queue
import json
from datetime import datetime, timedelta

from stt_config import VA_ALIAS, VA_CMD_LIST, VA_PARAM_CMD_LIST, VA_EXTRA_PARAM
from commands import recognize_cmd, va_functions, extra_q_check


model = vosk.Model(model_name="vosk-model-small-ru-0.22")
samplerate = 48000
device = 1

q = queue.Queue()
none_stop = True
any_q = False


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def stt(voice):
    global none_stop
    global any_q
    if any_q:
        if voice == '':
            print('agagsdg')
            any_q = extra_q_check()
        else:
            print(voice)
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
                if VA_CMD_LIST[command]['params'] and VA_CMD_LIST[command]['extra']:
                    any_q = datetime.now() + timedelta(seconds=5)
                elif VA_CMD_LIST[command]['params']:
                    va_functions[command](VA_CMD_LIST[command]['params'])
                else:
                    va_functions[command]()
                none_stop = VA_CMD_LIST[command]['non-stop']
            else:
                none_stop = True
        elif voice == 'проверка':
            print(voice)
            any_q = datetime.now() + timedelta(seconds=5)


def listen(callback):
    global any_q
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while none_stop:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])
            if any_q:
                if datetime.now() < any_q:
                    pass
                    # print(any_q)


if __name__ == '__main__':
    listen(stt)
