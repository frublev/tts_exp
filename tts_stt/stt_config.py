VA_NAME = 'Оливия'

VA_ALIAS = ('оливия', 'оливка', 'олива', 'оливер', 'оливье')

VA_CMD_LIST = {
    'stop': {'phrase': ('остановись', 'отбой', 'выключайся', 'спать', 'стоп', 'стол'),
             'non-stop': False,
             'params': 'olivia_bye1',
             'extra': False},
    'ctime': {'phrase': ('время', 'текущее время', 'сейчас времени', 'который час', 'сколько время', 'сколько времени'),
              'non-stop': True,
              'params': None,
              'extra': False},
    'weather_forecast_tod': {'phrase': ('погода сегодня', 'погода на сегодня',
                                        'прогноз погоды на сегодня', 'прогноз на сегодня'),
                             'non-stop': True,
                             'params': '../cash/olivia_forecast_tod',
                             'extra': False},
    'weather_forecast_tom': {'phrase': ('погода завтра', 'погода на завтра',
                                        'прогноз погоды на завтра', 'прогноз на завтра'),
                             'non-stop': True,
                             'params': '../cash/olivia_forecast_tom',
                             'extra': False},
    'timer': {'phrase': ('таймер', 'поставь таймер', 'включи таймер', 'тайна'),
              'non-stop': True,
              'params': None,
              'extra': 'olivia_timer1'},
    'stop_timer': {'phrase': ('стоп таймер', 'останови таймер', 'выключи таймер', 'выруби таймер',),
                   'non-stop': True,
                   'params': 'ноль ноль ноль',
                   'extra': False},
}
