# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        if date == date.currentDate():
            painter.setBrush(QtGui.QColor(0, 200, 200, 50))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawRect(rect)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 366)
        Form.setAutoFillBackground(False)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 461, 331))
        self.tabWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.calendar_tab = QtWidgets.QWidget()
        self.calendar_tab.setObjectName("calendar_tab")
        self.calendarWidget = MyCalendar(self.calendar_tab)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 461, 301))
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget.addTab(self.calendar_tab, "")
        self.weather_tab = QtWidgets.QWidget()
        self.weather_tab.setObjectName("weather_tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser.setGeometry(QtCore.QRect(120, 0, 101, 31))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 30, 121, 31))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_7.setGeometry(QtCore.QRect(0, 120, 121, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_8.setGeometry(QtCore.QRect(0, 210, 121, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_5.setGeometry(QtCore.QRect(120, 30, 101, 91))
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_9.setGeometry(QtCore.QRect(120, 120, 51, 91))
        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_10.setGeometry(QtCore.QRect(170, 120, 51, 91))
        self.textBrowser_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.graphicsView = QtWidgets.QGraphicsView(self.weather_tab)
        self.graphicsView.setGeometry(QtCore.QRect(0, 60, 121, 61))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.weather_tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 150, 121, 61))
        self.graphicsView_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.weather_tab)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 240, 121, 61))
        self.graphicsView_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_6.setGeometry(QtCore.QRect(220, 30, 71, 91))
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_3.setGeometry(QtCore.QRect(220, 0, 71, 31))
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_13.setGeometry(QtCore.QRect(290, 30, 71, 91))
        self.textBrowser_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_4.setGeometry(QtCore.QRect(290, 0, 71, 31))
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_14.setGeometry(QtCore.QRect(360, 30, 101, 41))
        self.textBrowser_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_15.setGeometry(QtCore.QRect(360, 0, 101, 31))
        self.textBrowser_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_11.setGeometry(QtCore.QRect(120, 210, 51, 91))
        self.textBrowser_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_12.setGeometry(QtCore.QRect(170, 210, 51, 91))
        self.textBrowser_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_16.setGeometry(QtCore.QRect(220, 120, 71, 91))
        self.textBrowser_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_17.setGeometry(QtCore.QRect(220, 210, 71, 91))
        self.textBrowser_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_18.setGeometry(QtCore.QRect(290, 120, 71, 91))
        self.textBrowser_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_19.setGeometry(QtCore.QRect(360, 70, 51, 51))
        self.textBrowser_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.textBrowser_20 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_20.setGeometry(QtCore.QRect(410, 70, 51, 51))
        self.textBrowser_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.textBrowser_21 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_21.setGeometry(QtCore.QRect(290, 210, 71, 91))
        self.textBrowser_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.textBrowser_22 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_22.setGeometry(QtCore.QRect(360, 160, 51, 51))
        self.textBrowser_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_22.setObjectName("textBrowser_22")
        self.textBrowser_23 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_23.setGeometry(QtCore.QRect(360, 120, 101, 41))
        self.textBrowser_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_23.setObjectName("textBrowser_23")
        self.textBrowser_24 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_24.setGeometry(QtCore.QRect(410, 160, 51, 51))
        self.textBrowser_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_24.setObjectName("textBrowser_24")
        self.textBrowser_25 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_25.setGeometry(QtCore.QRect(360, 250, 51, 51))
        self.textBrowser_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_25.setObjectName("textBrowser_25")
        self.textBrowser_26 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_26.setGeometry(QtCore.QRect(360, 210, 101, 41))
        self.textBrowser_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_26.setObjectName("textBrowser_26")
        self.textBrowser_27 = QtWidgets.QTextBrowser(self.weather_tab)
        self.textBrowser_27.setGeometry(QtCore.QRect(410, 250, 51, 51))
        self.textBrowser_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_27.setObjectName("textBrowser_27")
        self.tabWidget.addTab(self.weather_tab, "")
        self.textBrowser_28 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_28.setGeometry(QtCore.QRect(0, 0, 261, 41))
        self.textBrowser_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_28.setObjectName("textBrowser_28")
        self.textBrowser_30 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_30.setGeometry(QtCore.QRect(260, 0, 201, 41))
        self.textBrowser_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_30.setObjectName("textBrowser_30")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sweet Home Solution"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calendar_tab), _translate("Form", "Calendar"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Temp, C</span><span style=\" font-size:12pt; vertical-align:super;\">o</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Now</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Today</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Tommorow</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">0</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">0</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Hum, %</span></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">0</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">P, mm</span></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">W</span></p></body></html>"))
        self.textBrowser_15.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Wind</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_16.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_17.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_18.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_19.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">10</span></p></body></html>"))
        self.textBrowser_20.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">20</span></p></body></html>"))
        self.textBrowser_21.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">0</span></p></body></html>"))
        self.textBrowser_22.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">10</span></p></body></html>"))
        self.textBrowser_23.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">W</span></p></body></html>"))
        self.textBrowser_24.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">20</span></p></body></html>"))
        self.textBrowser_25.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">10</span></p></body></html>"))
        self.textBrowser_26.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">W</span></p></body></html>"))
        self.textBrowser_27.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">20</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weather_tab), _translate("Form", "Weather"))
        self.textBrowser_28.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Date - Time</span></p></body></html>"))
        self.textBrowser_30.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Timer</span></p></body></html>"))
