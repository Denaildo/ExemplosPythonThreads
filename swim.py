#!/usr/bin/python

import threading
import time
import random
from os import system
import re

printSwimmers = [["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"]]
winners = []

class RunSwimmer (threading.Thread):
    def __init__(self, threadID, distanceOfSwin):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.distanceOfSwin = distanceOfSwin
    def run(self):
        createThreadhOfSwimmer(self.threadID, self.distanceOfSwin)
def createThreadhOfSwimmer(threadID, distanceOfSwin):
    counter = 0
    caseOne = 0
    caseTwo = 9
    startTime = time.time()
    while counter < distanceOfSwin:
        delay = random.randint(1,4)
        time.sleep(delay)
        if ((counter <= 9) or (counter >= 20 and counter < 30) or (counter >= 40 and counter < 50) or (counter >= 60 and  counter < 70)):
            printSwimmers[threadID][caseOne] = ">"
            if (counter > 0):
                printSwimmers[threadID][caseOne-1] = "_"
            caseOne += 1
            caseTwo = 9
        elif ((counter > 9 and counter < 20) or (counter >= 30 and counter < 40) or (counter >= 50 and counter < 60) or (counter >= 70)):
            printSwimmers[threadID][caseTwo] = "<"
            if (caseTwo < 9):
                printSwimmers[threadID][caseTwo+1] = "_"
            caseTwo -= 1            
            caseOne = 0
        counter += 1
    endTime = time.time()
    winners.append("| Swimmer number: " + str(threadID+1) + "| Elapsed time: " + str(endTime-startTime) + " |")

def printSwimmerInRun(winners):
    while len(winners) < 8:
        system("clear")
        for x in xrange(8):
            print "Swimmer lane " + str(x+1) + " |",
            for y in xrange(10):
                print printSwimmers[x][y],
            print "| \n"
        time.sleep(1)
    system("clear")
    for x in xrange(8):
        print "Swimmer lane " + str(x+1) + " |",
        for y in xrange(10):
            print printSwimmers[x][y],
        print "| \n"
    print "Distance Elapsed: " + str(distance) + "\n Winner" + winners[0] + "\n --------- All time of Race Swim: -------- \n"
    for position in winners:
        print position

def instanceSwimmer(counter):
    for position in range(8):
        swimmer = RunSwimmer(position, counter)
        swimmer.start()

distance = input("Please, insert 50, 100, 200 or 400 to run distance \n")
if distance == 50:
    instanceSwimmer(10)
elif distance == 100:
    instanceSwimmer(20)
elif distance == 200:
    instanceSwimmer(40)
elif distance == 400:
    instanceSwimmer(80)
printSwimmerInRun(winners)

