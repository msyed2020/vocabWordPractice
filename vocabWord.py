import unicodedata


def enterNewWords(words):
    word = normalize(input("What word would you like to enter (must be in Italian): \n"))
    if checkItalian(word) == False:
        print("This is not a valid word")
        return
    else:
        meaning = input("What does this word mean???\n")
        words[word] = meaning
        return

def normalize(word):
    return unicodedata.normalize("NFC", word)

def checkItalian(word):
    with open("italianwords.txt", "r", encoding="utf-8") as f:
        wordList = set(w.strip().lower() for w in f)
    
    word = word.lower()
    if word in wordList:
        return True
    else:
        return False

def main():
    words = {}
    print("What would you like to do???:\n")
    print("1. Enter a new word")
    print("2. Practice words")
    resp = input("Choose either 1 or 2: ")
    if int(resp) == 1:
        enterNewWords(words)
    elif int(resp) == 2:
        print("list words lol")
    else:
        print("Choose a proper number")
        return
    


main()