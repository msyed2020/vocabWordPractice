import unicodedata
import json
import random

def enterNewWords():

    try:
        with open("words.json", "r", encoding="utf-8") as f:
            words = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        words = {}

    
    word = normalize(input("What word would you like to enter (must be in Italian): \n"))
    if checkItalian(word) == False:
        print("This is not a valid word")
        return
    else:
        meaning = input("What does this word mean???\n")
        words[word] = meaning
        with open("words.json", "w", encoding="utf-8") as f:
            json.dump(words, f, ensure_ascii=False, indent=4)
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

def listWords():
    words = getWords()
    if words == {}:
        print("Empty or corrupted words")
    for word, meaning in words.items():
        print(f"{word}: {meaning}")
    


def getWords():
    try:
        with open("words.json", "r", encoding="utf-8") as f:
            words = json.load(f)
        return words
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def wordToDefPrac():
    words = getWords()
    if words == {}:
        print("Empty or corrupted words")
    wordLookup = list(words.keys())
    num = random.randint(0, len(wordLookup) - 1)
    chosenWord = wordLookup[num]
    guess = input("What is the definition of " + chosenWord + "???:\n")
    if guess != words[chosenWord]:
        print("Incorrect!")
        print(chosenWord + " actually means " + words[chosenWord])
    else:
        print("Correct!")

def defToWordPrac():
    words = getWords()
    if words == {}:
        print("Empty or corrupted words")
    wordLookup = list(words.keys())
    num = random.randint(0, len(wordLookup) - 1)
    chosenWord = wordLookup[num]
    guess = input("What word is defined by '" + words[chosenWord] + "'???:\n")
    if guess != chosenWord:
        print("Incorrect!")
        print(chosenWord + " is the correct word.")
    else:
        print("Correct!")

def main():
    
    print("What would you like to do???:\n")
    print("1. Enter a new word")
    print("2. List words")
    print("3. Practice word to definitions")
    print("4. Practice definitions to word")
    resp = input("Choose either 1, 2, 3 or 4: ")
    if int(resp) == 1:
        enterNewWords()
    elif int(resp) == 2:
        listWords()
    elif int(resp) == 3:
        wordToDefPrac()
    elif int(resp) == 4:
        defToWordPrac()
    else:
        print("Choose a proper number")
        return
    


main()