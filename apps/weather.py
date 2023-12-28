from datetime import datetime
import json
import time

import requests
from num2words import num2words

from tts import speak

coord = {'latitude': 48.0353930, 'longitude': 17.2635956}


def get_forecast(coordinates):
    latitude_f = coordinates['latitude']
    longitude_f = coordinates['longitude']
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?'
                            f'latitude={latitude_f}&longitude={longitude_f}&'
                            f'cell_selection=land&'
                            f'timezone=auto&'
                            f'forecast_days=2&'
                            f'windspeed_unit=ms&'
                            f'hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,'
                            f'pressure_msl,'
                            f'windspeed_10m,winddirection_10m,windgusts_10m,'
                            f'precipitation,precipitation_probability,'
                            f'cloudcover,weathercode,visibility&'
                            f'daily=sunrise,sunset,precipitation_sum,precipitation_hours,precipitation_probability_max,'
                            f'wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant&'
                            f'current=temperature_2m,relative_humidity_2m,rain,showers,snowfall,cloud_cover,'
                            f'surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m')
    with open("../cash/forecast.json", "w") as f:
        json.dump(response.json(), f)
    return True


def module(q):
    if q < 0:
        return q * -1
    else:
        return q


def q_end(t_str):
    t_str = t_str.split()
    if t_str[-1] == 'один':
        return ''
    elif t_str[-1] in ['два', 'три', 'четыре']:
        return 'а'
    else:
        return 'ов'


def temperature_to_str(t_min, t_max):
    t_max_str = num2words(module(int(round(t_max, 0))), lang='ru')
    t_min_str = num2words(module(int(round(t_min, 0))), lang='ru')
    if round(t_min, 0) == round(t_max, 0):
        if round(t_min, 0) > 0:
            t_str = f'плюс {t_min_str}'
        elif round(t_min, 0) < 0:
            t_str = f'минус {t_max_str}'
        else:
            t_str = f'ноль'
    elif round(t_min, 0) >= 0:
        degr = q_end(t_max_str)
        t_str = f'{t_min_str} - {t_max_str} градус{degr} тепла'
    elif round(t_max, 0) <= 0:
        degr = q_end(t_min_str)
        t_str = f'{t_max_str} - {t_min_str} {degr} мороза'
    else:
        t_str = f'минус {t_min_str} - плюс {t_max_str}'
        print(t_min, t_max)
    return t_str


def wind_dir_str(wind_dir):
    if 22.5 <= wind_dir < 67.5:
        w_dir_str = 'юго-западный'
    elif 67.5 <= wind_dir < 112.5:
        w_dir_str = 'западный'
    elif 112.5 <= wind_dir < 157.5:
        w_dir_str = 'северо-западный'
    elif 157.5 <= wind_dir < 202.5:
        w_dir_str = 'северный'
    elif 202.5 <= wind_dir < 247.5:
        w_dir_str = 'северо-восточный'
    elif 247.5 <= wind_dir < 292.5:
        w_dir_str = 'восточный'
    elif 292.5 <= wind_dir < 337.5:
        w_dir_str = 'юго-восточный'
    else:
        w_dir_str = 'южный'
    return w_dir_str


def cloud_str(cloud):
    if cloud < 10:
        c_str = 'на небе ни облачка'
    elif 10 <= cloud < 25:
        c_str = 'в целом ясно, но иногда с облочками'
    elif 25 <= cloud < 50:
        c_str = 'временами облачно'
    elif 50 <= cloud < 75:
        c_str = 'облачно с прояснениями'
    elif 75 <= cloud < 90:
        c_str = 'облачно с редкими прояснениями'
    else:
        c_str = 'сплошная облачность'
    return c_str


def read_forecast(time_offset1=24, time_offset2=None):
    with open('../cash/forecast.json') as f:
        forecast = json.load(f)
    next_hour = datetime.now()
    next_hour = next_hour.hour
    tts = ''
    if next_hour < 23:
        time_set = ((next_hour, 23), (23, None))
    else:
        time_set = ((24, None),)
    for t in time_set:
        time_offset1, time_offset2 = t[0], t[1]
        temperature = forecast['hourly']['temperature_2m'][time_offset1:time_offset2]
        temperature.sort()
        t_min, t_max = temperature[0], temperature[-1]
        t_str = temperature_to_str(t_min, t_max)

        relativehumidity_2m = forecast['hourly']['relativehumidity_2m'][time_offset1:time_offset2]
        relativehumidity_2m.sort()
        h_str = num2words(int(round(relativehumidity_2m[-1], 0)), lang='ru')
        h_p = q_end(h_str)

        h_str = f'относительная влажность {h_str} процент{h_p}'

        cloud = forecast['hourly']['cloudcover'][time_offset1:time_offset2]
        cloud = sum(cloud)/len(cloud)
        c_str = cloud_str(cloud)

        precipitation = sum(forecast['hourly']['precipitation'][time_offset1:time_offset2])

        if time_offset1 == 23 or time_offset2 is None:
            f_day = ('Завтра будет', 'tom')
        else:
            f_day = ('Сегодня до конца дня', 'tod')
            precipitation = precipitation * 24 / (time_offset2 - time_offset1)

        if precipitation <= 5:
            prec = 'небольшие'
        elif 5 < precipitation <= 10:
            prec = 'умеренные'
        elif precipitation > 10:
            prec = 'обильные'

        precipitation_probability = forecast['hourly']['precipitation_probability'][time_offset1:time_offset2]
        precipitation_probability.sort()
        if precipitation_probability[-1] > 90:
            p_str = f'пройдут {prec} осадки'
        elif precipitation_probability[-1] > 75:
            p_str = f'весьма вероятны {prec} осадки'
        elif precipitation_probability[-1] > 30:
            p_str = f'вероятны {prec} осадки'
        elif precipitation_probability[-1] > 10:
            p_str = f'не исключены {prec} осадки'
        else:
            p_str = 'скорее всего, обойдется без осадков'

        if t_max < -2 and p_str != 'скорее всего, обойдется без осадков':
            p_str += ' в виде снега'
        elif 1 > t_min > -2 and p_str != 'скорее всего, обойдется без осадков':
            p_str += ' возможно в виде мокрого снега'

        winddirection_10m = forecast['hourly']['winddirection_10m'][time_offset1:time_offset2]
        windspeed_10m = forecast['hourly']['windspeed_10m'][time_offset1:time_offset2]
        wind_sum = sum(windspeed_10m)
        wind_dir = 0
        for count, value in enumerate(winddirection_10m):
            wind_dir += (windspeed_10m[count] / wind_sum) * value

        w_dir_str = wind_dir_str(wind_dir)

        windspeed_10m.sort()
        w_speed_str = num2words(int(round(windspeed_10m[-1], 0)), lang='ru')
        w_ms = q_end(w_speed_str)
        windgusts_10m = forecast['hourly']['windgusts_10m'][time_offset1:time_offset2]
        windgusts_10m.sort()
        w_gusts_str = num2words(int(round(windgusts_10m[-1], 0)), lang='ru')
        g_ms = q_end(w_gusts_str)

        w_str = (f'ветер {w_dir_str}</s> <s>максимальной скоростью {w_speed_str} метр{w_ms} в секунду'
                 f' <s> с порывами {w_gusts_str} метр{g_ms} в секунду</s>')

        tts_forecast = f'''
                      <speak>
                      <p>                      
                            <s>{f_day[0]} {c_str}</s>
                            <s>{t_str}</s>
                            <s>{h_str}</s>
                            <s>{p_str}</s>
                            <s>{w_str}</s>
                      </p>
                      </speak>
                      '''
        speak(tts_forecast, True, f'../cash/olivia_forecast_{f_day[1]}', False)
        tts += tts_forecast
    return tts


if __name__ == '__main__':
    a = get_forecast(coord)
    print(read_forecast())
