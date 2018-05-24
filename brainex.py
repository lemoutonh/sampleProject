import random
from urllib import urlopen
import math
import sys
import linecache
import os

WORD_URL = "http://learncodethehardway.org/words.txt"
ENGLISH_WORDS = []
GERMAN_WORDS = []

def initWordlists():
    # load up the ENGLISH_WORDS from the website
    for word in urlopen(WORD_URL).readlines():
        ENGLISH_WORDS.append(word.strip())
        
    #load up GERMAN_WORDS from file (random sample)
    for word in open("word_list_german_spell_checked.txt",'r').readlines():
        GERMAN_WORDS.append(word)
        

def getRandomNumber(length):
    number = 0
    i = 0
    while i < length:
        j = random.randrange(0,9,1) #random: semi-random nr, DO NOT USE FOR CRYPTOGRAPHIC PURPOUS
        number = number + j * math.pow(10,i)
        i = i+1
    return int(number)
    
def getRandomWord(wordList):
    word = wordList[random.randint(0,len(wordList)-1)]
    return word
    

class NumberMemory(object):
    #imports don't work here -> top of file
    
    def __init__(self,NumAmount, NumLen):
        self.NumAmount = NumAmount
        self.NumLen = NumLen
        self.Numbers = []
        
    def init(self):
        for i in range(0,self.NumAmount):
            nr = getRandomNumber(self.NumLen)
            self.Numbers.append(nr)
            
    def startGame(self):
        print "Number Memory\n"
        
        #show numbers
        for i in range(0,self.NumAmount):
            print self.Numbers[i]
            
        #[maybe implement timer]
        print "Press key, if you want to cover numbers"
        raw_input('> ')
        
        #clear screen
        os.system('clear')
        
        #get input number, by number and show answer
        print "Type in each number to see comparision"
        answer = None
        question = None
        cnt_correct = 0
        
        for i in range(0,self.NumAmount):
            question = self.Numbers[i]
            #[maybe implement regex to make sure answer is integer, if not -> error at int(answer)]
            answer = raw_input('> ')
            print question
            #[maybe implement true/false per question + points]
            if question == int(answer):
                print "correct :)"
                cnt_correct = cnt_correct + 1
            else:
                print "wrong answer :("
        if cnt_correct == 1:
            print "game finished, you got ", cnt_correct, " number right."
        else:
            print "game finished, you got ", cnt_correct, " numbers right."
           

def main():
    initWordlists()
    
    numberG = NumberMemory(5,8)
    print numberG.NumLen
    print numberG.NumAmount
    numberG.init()
    numberG.startGame()
   

main()
