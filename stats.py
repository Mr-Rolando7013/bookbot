def count_words(text):
    count = 1
    wordCount = 0
    myDict = {}
    for word in text.split():
        wordCount += 1
        #count += 1
        letters = list(word.lower())
        for letter in letters:
            #print("letter: ", letter, "word: ", word)
            if letter in myDict:
                myDict[letter] = myDict[letter] + 1
            else:
                myDict[letter] = count
    #print(wordCount, "words found in the document")
    return myDict, wordCount

def sortDict(myDict, wordCount):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", wordCount, " total words")
    print("--------- Character Count -------")
    myDict2 = {}
    for  key, value in myDict.items():
        if key.isalpha():
            myDict2[key] = value 
        else:
            pass

    myDict3 = dict(sorted(myDict2.items(), key=lambda item: item[1], reverse=True))
    for key, value in myDict3.items():
        print(key + ":", value)

    print("============= END ===============")
