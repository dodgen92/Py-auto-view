import webbrowser
import time
from pykeyboard import PyKeyboard

count = 0
urls = ['#']
k = PyKeyboard()

while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        k.press_keys(['Command','W'])
        count = count + 1

else:
    pass