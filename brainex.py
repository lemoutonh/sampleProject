from urllib import urlopen
import sys
import linecache

#my imports
from classes import *

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
        
           
def main():
    initWordlists()
    
    numberG = NumberMemory(5,8)
    print numberG.NumLen
    print numberG.NumAmount
    numberG.init()
    numberG.startGame()
   

main()
