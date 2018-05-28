# -*- coding: utf-8 -*-

from urllib import urlopen
import sys
import linecache
#my imports
import classes

WORD_URL = "http://learncodethehardway.org/words.txt"
ENGLISH_WORDS = []
GERMAN_WORDS = []

def initWordlists(): #init lists for WordGame

    # load up the ENGLISH_WORDS from the website
    for word in urlopen(WORD_URL).readlines():
        ENGLISH_WORDS.append(word.strip())
        
    #load up GERMAN_WORDS from file (random sample)
    for word in open("./word_list_german_spell_checked.txt",'r').readlines():
        GERMAN_WORDS.append(word)
        
           
def main():

    initWordlists()
    
    #test numberMemory
    #numberG = classes.NumberMemory(5,8)
    #numberG.startGame()
    
    #test wordMemory
    print classes.getRandomWord(GERMAN_WORDS)
    print classes.getFantasyWord(ENGLISH_WORDS)
    wordG = classes.WordMemory(5,ENGLISH_WORDS,GERMAN_WORDS)
    wordG.startGame()
    
   

main()
