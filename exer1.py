#!/usr/bin/python

import threading
import time
import random
from os import system
verificarEnchimento = 0
listOfT = []
listOfF = []
listOfS = []
locaisvagos = []
t = []
class Car (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.s = threading.Semaphore()
        self.counter = random.randint(1, 10)
    def run(self):
        global verificarEnchimento
        global locaisvagos
        self.s.acquire()
        verificarEnchimento += 1
        locaisvagos.append(self.threadID)  
        fileobj.write("Entering in PIT LANE: " + str(self.threadID) + "\n")
        while (self.counter > 0):
            time.sleep(1)
            self.counter -= 1
        verificarEnchimento -= 1
        locaisvagos.remove(self.threadID)
        fileobj.write("Exiting PIT LANE: " + str(self.threadID) + "\n")
        
        self.s.release()
class File (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global listOfT
        global listOfF
        global listOfS
        while (len(listOfT) > 0):
            if (verificarEnchimento <30):
                thread = listOfT.pop(0)
                thread.start()
        while (len(listOfF) > 0):
            if (verificarEnchimento <30):
                thread = listOfF.pop(0)
                thread.start()
        while (len(listOfS) > 0):
            if (verificarEnchimento <30):
                thread = listOfS.pop(0)
                thread.start()

fileobj = open("relatorio.txt","w+")
for i in range(10):
    p = Car("Teacher " + str(i+1), "Teacher")
    t.append(p)
for i in range(15):
    f = Car("Employeer " + str(i+1), "Employer")
    t.append(f)
for i in range(30):
    s = Car("Student " + str(i+1), "Student")
    t.append(s)
random.shuffle(t)
for x in t:
    if (verificarEnchimento < 30):
        x.start()
    elif (x.name == "Teacher"):
        listOfT.append(x)
    elif (x.name == "Employer"):
        listOfF.append(x)
    elif (x.name == "Student"):
        listOfS.append(x)
fi = File("file")
t.append(fi)
fi.start()
while len(locaisvagos) != 0:
    system("clear")
    print "Car in pits: "
    for x in locaisvagos:
        print x
    time.sleep(1)    
for x in t:
    x.join()
fileobj.close
print "Exiting - Access 'relatorio.txt' to view all includes and excludes in the pit"
