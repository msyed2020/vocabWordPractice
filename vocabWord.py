import unicodedata
import json

def enterNewWords(words):
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
    try:
        with open("words.json", "r", encoding="utf-8") as f:
            words = json.load(f)
        for word, meaning in words.items():
            print(f"{word}: {meaning}")
    except FileNotFoundError:
        print("No word file found")
    except json.JSONDecodeError:
        print("Word list empty or corrupted")


def main():
    words = {}
    print("What would you like to do???:\n")
    print("1. Enter a new word")
    print("2. List words")
    resp = input("Choose either 1 or 2: ")
    if int(resp) == 1:
        enterNewWords(words)
    elif int(resp) == 2:
        listWords()
    else:
        print("Choose a proper number")
        return
    


main()