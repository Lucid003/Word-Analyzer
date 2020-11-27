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


wordSet = set()
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
    for word in words:
        for ele in word:
            if '.' in ele:
                word = word.replace('.', '') # removing periods from words
        #temporarily using dictionary to store words and word counts
        wordDict.setdefault(word, 1)
        wordDict[word] += 1
        0
        if word not in wordSet:
            wordSet.add(word)
            word = Word(word)
        #else:
         #   word.count += 1



del wordDict['']
#sorting full dictionary by value in descending order
sortedDict = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

'''for x, y in sortedDict:
    if y > 30:
        print(x + " appeared " + str(y) + " times.")'''
