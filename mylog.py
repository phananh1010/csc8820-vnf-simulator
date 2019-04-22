import time
import os

mtime = lambda: int(round(time.time() * 1000))

def log(text):
    print 'DEBUG: {}'.format(text)
    
  
