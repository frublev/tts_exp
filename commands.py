from fuzzywuzzy import fuzz
from datetime import datetime
from num2words import num2words

from recorder import file_to_play
from tts import va_play, speak


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


def weather_forecast_tod():
    audio, sample_rate = file_to_play('../cash/olivia_forecast_tod')
    va_play(audio, sample_rate)
    return True


def weather_forecast_tom():
    audio, sample_rate = file_to_play('../cash/olivia_forecast_tom')
    va_play(audio, sample_rate)
    return True


def extra_q_check():
    audio, sample_rate = file_to_play('olivia_cancel1')
    va_play(audio, sample_rate)
    return False


va_functions = {
    'stop': va_speak,
    'ctime': va_current_time,
    'weather_forecast_tod': va_speak,
    'weather_forecast_tom': va_speak,
    'timer': va_speak,
}
