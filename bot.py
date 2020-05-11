import webbrowser
import time
from pykeyboard import PyKeyboard

#replace "#" with url website
count = 0
urls = ['#']
k = PyKeyboard()

#replace count< with how many times to visit
while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
# replace "time.sleep" with frequency of repeat views 
         time.sleep(10)
        k.press_keys(['Command','W'])
        count = count + 1

else:
    pass