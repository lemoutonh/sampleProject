# -*- coding: utf-8 -*-

import os
import random
import math

#helper functions (seperate class?)

def getRandomNumber(length): #produce random nr, length = digits
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
    
def getFantasyWord(syllableList): #create fantasy word from input list. concats 3-5 "words" to make fantasy word
    word = ""
    for i in range (2,random.randint(3,5)):
        syllable = getRandomWord(syllableList)
        word = word + syllable
        
    return word
    
def shuffleDict(myDict):
    resDict = {}
    elementsChosen = []
    
    
    while len(resDict) < len(myDict):
        r = random.randint(0,len(myDict)-1)
        while r in elementsChosen:
            r = random.randint(0,len(myDict)-1)   
        elementsChosen.append(myDict.keys()[r])
        #print myDict.keys()[r],  ":", myDict.values()[r] #TEST
        resDict[myDict.keys()[r]] = myDict.values()[r]
           
    return resDict

#----CLASSES----

class WordMemory(object):
    def __init__(self,wordAmount,syllableList, wordList):
        self.WordAmount = wordAmount 
        self.SyllableList =syllableList 
        self.WordList = wordList
        self.FantasyWords = []
        self.TranslationWords = []
        self.WordPairs = {} # key : value = FantasyWord : TranslationWord
            
        for i in range(0,self.WordAmount):
            self.FantasyWords.append(getFantasyWord(self.SyllableList))
            self.TranslationWords.append(getRandomWord(self.WordList))

            
    def startGame(self):
        print "FantasyWords= ", self.FantasyWords
        print "TranslationWords=", self.TranslationWords
        
        print "Word Memory\n"
        #show "word : translation" + save wordpairs in dict
        for i in range(0, len(self.FantasyWords)):
            print self.FantasyWords[i], " : ", self.TranslationWords[i]
            #add to dict
            self.WordPairs[self.FantasyWords[i]] = self.TranslationWords[i]
        
        #clear screen on input
        print "Press key, if you want to cover words"
        raw_input('> ')
        
        #os.system('clear')
        
        #shuffle
        shuffledPairs = shuffleDict(self.WordPairs)
        userResults = []
        #get answer for each word:translation
        for wordPair in shuffledPairs:
            print wordPair
            myInput = raw_input('< ')
            userResults.append(myInput)
            
        #show result
        i = 0
        for wordPair in shuffledPairs:
            print wordPair, " : ", shuffledPairs[wordPair]
            print "you entered: ", userResults[i]
            if shuffledPairs[wordPair] == userResults[i]:
                print "RIGHT :)"
            else:
                print "WRONG :("
            i = i+1
            
        
        
class NumberMemory(object):
    #imports don't work here -> top of file
    
    def __init__(self,NumAmount, NumLen):
        self.NumAmount = NumAmount
        self.NumLen = NumLen
        self.Numbers = []
        
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
