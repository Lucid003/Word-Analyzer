import operator
import os



class Word:
    def __init__(self, word):
        self.word = word
        self.cased = {} # word before .lower()
        self.count = 1 
        self.previous_word = {} # dictionary of words that appeared one spot before word
        self.previous_word2 = {} # .................................two spots...........
        self.previous_word3 = {} # ...............................three spots...........
        self.next_word = {}  # dictionary of words that appeared one spot after word
        self.next_word2 = {} # ..................................two spots..........
        self.next_word3 = {} # ................................three spots..........
        self.endOfSentence = 0 # count of how many times word was last word in sentence
        self.startOfSentence = 0 # ..............................first word............
    
    # increments count + 1
    def setCount(self):
        self.count += 1
    
    # returns count
    def getCount(self):
        return self.count
    
    # adds cased version of word to dictionary
    def addCase(self, cased):
        self.cased.setdefault(cased, 0)
        self.cased[cased] += 1
    
    # return cased dictionary
    def getCase(self):
        return self.cased
    
    # sets previous 3 words except for those that are None
    def setPreviousWords(self, prev1, prev2, prev3):
        if prev1 != None:
            self.previous_word.setdefault(prev1, 0)
            self.previous_word[prev1] += 1
        if prev2 != None:
            self.previous_word2.setdefault(prev2, 0)
            self.previous_word2[prev2] += 1
        if prev3 != None:
            self.previous_word3.setdefault(prev3, 0)
            self.previous_word3[prev3] += 1
    
    # sets next 3 words, except for those that are None
    def setNextWords(self, next1, next2, next3):
        if next1 != None:
            self.next_word.setdefault(next1, 0)
            self.next_word[next1] += 1
        if next2 != None:
            self.next_word2.setdefault(next2, 0)
            self.next_word2[next2] += 1
        if next3 != None:
            self.next_word3.setdefault(next3, 0)
            self.next_word3[next3] += 1
    
    # return first previous word
    def getPreviousWord(self):
        return self.previous_word
    
    # return second previous word
    def getPreviousWord2(self):
        return self.previous_word2
    
    # return third previous word
    def getPreviousWord3(self):
        return self.previous_word3

    # return first next word
    def getNextWord(self):
        return self.next_word
    
    # return second next word
    def getNextWord2(self):
        return self.next_word2
    
    # return third next word
    def getNextWord3(self):
        return self.next_word3
    
    # increment endOfSentence
    def endIncrement(self):
        self.endOfSentence += 1
    
    # increment startOfSentence
    def startIncrement(self):
        self.startOfSentence += 1
    
    # return endOfSentence
    def getEnd(self):
        return self.endOfSentence
    
    # return startOfSentence
    def getStart(self):
        return self.startOfSentence

# reads file, removes trash characters, parse text, and return dictionary
def read_file(book):

    wordDict = {} # empty dictionary for words
    listed = [] # empty list for sentences

    # reading entire text file into string, cleaning it up, and separating into list of sentences
    with open(book, encoding='utf-8') as file: 
        entire_book = file.read().replace('\n', ' ').replace('!', '.').replace('?', '.').replace('"', '')
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
            
            cased = word # original casing
            word = word.lower()

            if word not in wordDict:
                wordDict[word] = Word(word)
                wordDict[word].setPreviousWords(prev1, prev2, prev3)
                wordDict[word].addCase(cased)
            else:
                wordDict[word].setCount()
                wordDict[word].setPreviousWords(prev1, prev2, prev3)
            
            if index == 0:
                wordDict[word].startIncrement()
            
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
                wordDict[word].endIncrement()
                
            index += 1
            prev3 = prev2
            prev2 = prev1
            prev1 = word
            
    del wordDict['']
    return wordDict



'''wordDict = read_file('book.txt')

sortedPrevWord = sorted(wordDict['drow'].getPreviousWord().items(), key=operator.itemgetter(1), reverse=True)
for x, y in sortedPrevWord:
    print(x + ' appeared before DROW ' + str(y) + ' times.')'''

'''if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        read_file(arg)
'''
