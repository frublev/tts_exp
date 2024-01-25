import sys
from datetime import date

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox, QWidget, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QTextBrowser, \
    QGridLayout

from apps.forms.test2 import Ui_Form
from apps.forms.day_dialog import Ui_Dialog
from global_var import settings


def change_global_vars(var, val):
    settings.charts[var] = val


class AlertDialog(QDialog):
    def __init__(self, parent, m=None, t=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.resize(250, 100)
        btn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(btn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.setCenterButtons(btn)
        self.label1 = QLabel(m)
        self.label1.setStyleSheet("font-size: 20px")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1, alignment=Qt.AlignCenter)
        if t:
            self.label2 = QLabel(t)
            self.label2.setStyleSheet('font-size: 32px; color: red')
            self.layout.addWidget(self.label2, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class DayDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, event=None):
        super().__init__(parent)
        self.setupUi(self)
        self.layout_main = QVBoxLayout()
        self.textbox1 = QTextBrowser()
        self.layout_main.addWidget(self.textbox1)
        if event:
            self.layout_grid = QGridLayout()
            for n in enumerate(event):
                btn = QDialogButtonBox.Ok
                self.buttonBox = QDialogButtonBox(btn)
                self.buttonBox.accepted.connect(self.accept)
                self.buttonBox.setCenterButtons(btn)
                self.label = QLabel(n[1])
                self.layout_grid.addWidget(self.label, n[0], 0, alignment=Qt.AlignLeft)
                self.layout_grid.addWidget(self.buttonBox, n[0], 0, alignment=Qt.AlignRight)

            self.layout_main.addLayout(self.layout_grid)

            self.setLayout(self.layout_main)

    def event_handle(self, n):
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.calendarWidget.clicked.connect(self.calendar_action)
        self.check_global_vars()
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.check_global_vars)

    def check_global_vars(self):
        current_time = QDateTime.currentDateTime()
        current_time = current_time.toString('d MMM ddd hh:mm')
        self.textBrowser_28.setFontPointSize(18)
        self.textBrowser_28.setText(current_time)

        global_vars = settings.charts
        if global_vars['timer']:
            ttt = global_vars['timer']

            h = ttt // 3600
            m = (ttt % 3600) // 60
            s = (ttt % 3600) - m * 60
            hh_mm_ss = [str(h), str(m), str(s)]
            for t in range(3):
                if len(hh_mm_ss[t]) == 1:
                    hh_mm_ss[t] = '0' + hh_mm_ss[t]
            self.textBrowser_30.setFontPointSize(18)
            self.textBrowser_30.setText(f'Timer  {hh_mm_ss[0]}:{hh_mm_ss[1]}:{hh_mm_ss[2]}')
            self.textBrowser_30.setAlignment(Qt.AlignmentFlag.AlignRight)
            if global_vars == settings.charts:
                ttt -= 1
                settings.charts['timer'] = ttt
                if ttt < 5:
                    self.textBrowser_30.setStyleSheet('color: red;')
                if ttt == 0:
                    self.textBrowser_30.setText(f'Timer  00:00:00')
                    self.textBrowser_30.setAlignment(Qt.AlignmentFlag.AlignRight)
                    c_t = QDateTime.currentDateTime().toString('hh:mm:ss')
                    self.alert_up('Timer was turned off at', c_t)
                    settings.charts['timer_off'] = True
        elif global_vars['timer_off']:
            print(global_vars['timer_off'])
        else:
            self.textBrowser_30.setText('')

    def alert_up(self, message, text):
        dlg = AlertDialog(self, message, text)
        dlg.resize(250, 100)
        dlg.show()
        dlg.buttonBox.accepted.connect(lambda: change_global_vars('timer_off', False))

    def calendar_action(self):
        our_date = self.calendarWidget.selectedDate().getDate()
        our_date = date(our_date[0], our_date[1], our_date[2])
        our_day = our_date.strftime('%d %B %Y %A')
        our_week = int(our_date.strftime('%W'))
        if our_week % 2:
            our_week = 'Long week'
        else:
            our_week = 'Short week'
        our_day = our_day + ' / ' + our_week
        dlg = DayDialog(self, )
        dlg.show()


# ['number 1', 'number 2', 'number 3', 'number 4', 'number 5', 'number 6', 'number 7']

def start_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    start_gui()
