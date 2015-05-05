#!/usr/bin/python
import threading
import time
import random
s = threading.Semaphore()

class UserBank(threading.Thread):
    def __init__(self, ide, randomOne, randomTwo):
        threading.Thread.__init__(self)
        self.ide = ide
        self.randomOne = randomOne
        self.randomTwo = randomTwo
    def run(self):
        for x in range(10):
            print " Client" + str(self.ide) + " Acessing balance... \n"
            s.acquire()
            userManipulation = random.randint(self.randomOne,self.randomTwo)
            if userManipulation < 0:
                print "Client " + str(self.ide) + "  conected value removed: " + str(userManipulation) + '\n'
            else:
                print "Client " + str(self.ide) + "  conected value add: " + str(userManipulation) + '\n'
            manipulevalue(userManipulation)    
            print "Client " + str(self.ide)  + "  OK! \n"
            time.sleep(3)
            s.release()

def manipulevalue(user):
    global balance 
    balance += user
    print 'Balancer: ' + str(balance)
 
       
balance = 2000
userAppend = UserBank(1,100,300)
userRemove = UserBank(2,-300,-1)
userAppend.start()
userRemove.start()    

