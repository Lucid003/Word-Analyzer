import operator
import os


class Word:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.previous_word = {}
        self.previous_word2 = {}
        self.previous_word3 = {}
        self.next_word = {}
        self.next_word2 = {}
        self.next_word3 = {}
    
    def setCount(self):
        self.count += 1
    
    def getCount(self):
        return self.count
    
    def setPreviousWords(self, prev1, prev2, prev3):
        if prev1 != None:
            self.previous_word.setdefault(prev1, 1)
            self.previous_word[prev1] += 1
        if prev2 != None:
            self.previous_word2.setdefault(prev2, 1)
            self.previous_word2[prev2] += 1
        if prev3 != None:
            self.previous_word3.setdefault(prev3, 1)
            self.previous_word3[prev3] += 1
    
    def setNextWords(self, next1, next2, next3):
        if next1 != None:
            self.next_word[next1] += 1
            self.next_word.setdefault(next1, 1)
        if next2 != None:
            self.next_word2.setdefault(next2, 1)
            self.next_word2[next2] += 1
        if next3 != None:
            self.next_word3.setdefault(next3, 1)
            self.next_word3[next3] += 1
    
    def getPreviousWord(self):
        return self.previous_word
    
    def getPreviousWord2(self):
        return self.previous_word2
    
    def getPreviousWord3(self):
        return self.previous_word3


wordDict = {} # empty dictionary for words
listed = [] # empty list for sentences

# reading entire text file into string, cleaning it up, and separating into list of sentences
with open('book.txt', encoding='utf-8') as file: 
    entire_book = file.read().replace('\n', ' ').replace('!', '.').replace('?', '.').replace('"', '').upper()
    sentences = entire_book.split(". ")
    for sentence in sentences:
        listed.append(sentence)


trashChars = '''()[]{};:,'"\,<>/@#$%^&*_~“”''' # characters to be removed from sentences
for sentence in listed:
    sentence = sentence.replace('...', '').replace("’s", '') # other stuff being removed from sentence
    for ele in sentence:
        if ele in trashChars:
            sentence = sentence.replace(ele, '') # removing trashChars
    words = sentence.split(' ') # splitting sentence into words
    index = 0
    prev1 = None
    prev2 = None
    prev3 = None
    for word in words:
        for ele in word:
            if '.' in ele:
                word = word.replace('.', '') # removing periods from words
        if len(words) >= index + 4:
            next1 = words[index + 1]
            next2 = words[index + 2]
            next3 = words[index + 3]
        elif len(words) == index + 3:
            next1 = words[index + 1]
            next2 = words[index + 2]
            next3 = None
        elif len(words) == index + 2:
            next1 = words[index + 1]
            next2 = None
            next3 = None
        else:
            next1 = None
            next2 = None
            next3 = None

        if word not in wordDict:
            wordDict[word] = Word(word)
            wordDict[word].setPreviousWords(prev1, prev2, prev3)
        else:
            wordDict[word].setCount()
            wordDict[word].setPreviousWords(prev1, prev2, prev3)
        index += 1
        prev3 = prev2
        prev2 = prev1
        prev1 = word
        
del wordDict['']

'''for key in wordDict:
    if wordDict[key].getCount() >= 100:
        print(key + ' appears ' + str(wordDict[key].getCount()) + " times.")'''

''' Test case

sortedPrevWord = sorted(wordDict['EDWARD'].getPreviousWord().items(), key=operator.itemgetter(1), reverse=True)
for x, y in sortedPrevWord:
    print(x + ' appeared before EDWARD ' + str(y) + ' times.')
'''
