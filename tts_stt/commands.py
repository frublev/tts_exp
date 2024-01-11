from time import sleep
from threading import Thread

from fuzzywuzzy import fuzz
from datetime import datetime
from num2words import num2words

from tts_stt.recorder import file_to_play
from tts_stt.tts import va_play, speak
from text_to_numb import tex_to_num

from global_var import settings


is_running = False


def recognize_cmd(cmd, cmds):
    rc = {'cmd': '', 'percent': 80}
    for c, v in cmds.items():
        for x in v['phrase']:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc


def va_speak(what='olivia_bye1'):
    audio, sample_rate = file_to_play(what)
    va_play(audio, sample_rate)
    return False


def va_current_time():
    audio, sample_rate = file_to_play('olivia_wait1')
    va_play(audio, sample_rate)
    ctime = datetime.now()
    h_str = num2words(ctime.hour, lang='ru')
    if ctime.minute < 10:
        m_str = 'ноль ' + num2words(ctime.minute, lang='ru')
    else:
        m_str = num2words(ctime.minute, lang='ru')
    answer = f'''
              <speak>
              <p>
                  прямо сейчас {h_str} {m_str}
              </p>
              </speak>
              '''
    speak(answer)
    return True


def timer(sec):
    global is_running
    va_speak('olivia_timer_on1')
    settings.charts['timer'] = sec
    s = sec
    while is_running and s > 0:
        print(s)
        print(is_running)
        sleep(1)
        s -= 1
    is_running = False
    if s == 0:
        settings.charts['timer'] = 0
        va_speak('olivia_timer_end1')


def start_timer(t_):
    global is_running
    is_running = False
    settings.charts['timer'] = 0
    print('dfgsdg', is_running)
    sleep(1)
    if t_ == 'ноль ноль ноль':
        is_running = False
        settings.charts['timer'] = 0
        va_speak('olivia_timer_off1')
        return False
    else:
        h_m_s = tex_to_num(t_)
        if h_m_s:
            print(h_m_s)
            seconds = 0
            for k, v in h_m_s.items():
                if k == 'h':
                    seconds += v * 3600
                elif k == 'm':
                    seconds += v * 60
                elif k == 's':
                    seconds += v
            if seconds > 0:
                is_running = True
                timer_thread = Thread(target=timer, args=(seconds,), daemon=True)
                timer_thread.start()
            else:
                is_running = False
                va_speak('olivia_timer_off1')
            return False
        else:
            return True


va_functions = {
    'stop': va_speak,
    'ctime': va_current_time,
    'weather_forecast_tod': va_speak,
    'weather_forecast_tom': va_speak,
    'timer': start_timer,
    'stop_timer': start_timer,
}
