def getPerson(text):
    # Splitting the text into a list of words
    wordList = text.split()

    for i in range(0,len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() =='who' and wordList[i+1].lower() =='is':
            return wordList[i+2] + ' '+wordList[i+3]
