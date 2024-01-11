class GlobalVar:
    def __init__(self):
        self._charts = {'timer': 0, 'timer_off': False}

    @property
    def charts(self):
        print('Произошел запрос переменной')
        return self._charts

    @charts.setter
    def charts(self, value):
        print('Произошло изменение переменной')
        self._charts = value


settings = GlobalVar()
