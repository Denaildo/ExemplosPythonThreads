#!/usr/bin/python

import threading
import time
import random
from os import system
import re

printHorse = []
winners = []

class RunHorse (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        handleThreadhOfHorse(self.threadID)

def handleThreadhOfHorse(threadID):
    counter = 0
    startTime = time.time()
    while counter < 10:
        delay = random.randint(1,6)
        time.sleep(delay)
        printHorse[threadID][counter] = "M"
        if (counter > 0):
            printHorse[threadID][counter-1] = "_"
        counter += 1
    endTime = time.time()
    winners.append("| Horse Number: " + str(threadID+1) + "| Time Race: " + str(endTime-startTime) + " |")

def printHorseInRun(number, winners):
    while len(winners) < numberOfHorse:        
        system("clear")
        for x in xrange(number):
            print "Horse " + str(x+1) + " |",
            for y in xrange(10):
                print printHorse[x][y],
            print "| \n"
        time.sleep(1)

    for x in xrange(number):
        print "Horse " + str(x+1) + " |",
        for y in xrange(10):
            print printHorse[x][y],
        print "| \n"
    print "Winner" + winners[0] + "\n --------- All time of Race: -------- \n"
    for position in winners:
        print position

def instanceOfHorse(numberOfHorse):
    for position in range(numberOfHorse):
        printHorse.append(["M","_","_","_","_","_","_","_","_","_"])
        horse = RunHorse(position)
        horse.start()

numberOfHorse = input("Number of horse runners \n")
instanceOfHorse(numberOfHorse)
printHorseInRun(numberOfHorse, winners)

