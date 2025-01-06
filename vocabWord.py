
def enterNewWords(words):
    print("Enter words here")

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