
from sys import stdout
from time import sleep
class Slow:
    def write(text, second):
        for t in text:
        	x = text.replace(text , t+"")
        	xx = x.capitalize()
        	stdout.write(xx)
        	stdout.flush()
        	sleep(second)
        	stdout.flush()
