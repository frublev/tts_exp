from threading import Thread

from tts_stt.stt import listen, stt
from apps.gui import start_gui

if __name__ == '__main__':
    va_thread = Thread(target=listen, args=(stt,), daemon=True)
    va_thread.start()
    start_gui()
