import operator
import os
import re

wordDict = {} # empty dictionary for words

with open('book.txt', encoding='utf-8') as file:
    for line in file:
        lst = re.findall('[0-9A-Z]+', line.upper())
        #print(lst)
        for item in lst:
            #create default key or increment existing key
            wordDict.setdefault(item, 1)
            wordDict[item] += 1

#sorting full dictionary by value in descending order
sortedDict = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
for x, y in sortedDict:
    if y > 30:
        print(x + " appeared " + str(y) + " times.")