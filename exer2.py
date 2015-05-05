#!/usr/bin/python
import threading
import time
import random
from os import system

class FreePosition(threading.Thread):

    def __init__(self, ide):
        threading.Thread.__init__(self)
        self.ide = ide  
        self.s = threading.Semaphore()
    def run(self):
        for x in range(10):    
            count = 0
            employee = random.randint(0,6)
            if listOfEmployeer[employee].situation == 0:                
                self.s.acquire()
                listOfEmployeer[employee].situation = 1
                listOfEmployeer[employee].positionID = self.ide+1
                while count <= 5:
                    
                    value = random.randint(-300,300)
                    listOfEmployeer[employee].balance += value
                    time.sleep(random.randint(1,3))
                    count += 1       
                listOfEmployeer[employee].situation = 0
                listOfEmployeer[employee].positionID = 0
                self.s.release()        

class EmployeeBank():
    def __init__(self,name, ide, balance, situation, positionID):
        self.name = name
        self.ide = ide
        self.balance = balance
        self.situation = situation
        self.positionID = positionID
listOfEmployeer = []
for x in range(7):
    listOfEmployeer.append(EmployeeBank(str(x),x,1000, 0, 0))

for x in range(3):
    f = FreePosition(x)
    f.start()

while True:
    count = 0    
    system("clear")    
    for x in listOfEmployeer:
        print "Funcionario: " + str(x.name) + " antendendo no caixa: " + str(x.positionID) + " Saldo: " + str(x.balance) + "\n"
        count += x.positionID
    if count == 0:
        
        break;
    time.sleep(1)
