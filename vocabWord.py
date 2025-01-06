
def enterNewWords(words):
    pass

def main():
    words = {}
    print("What would you like to do???:\n")
    print("1. Enter a new word")
    print("2. Practice words")
    resp = input("Choose either 1 or 2: ")
    if type(resp) != int or (resp < 1 or resp > 2):
        print("Choose a proper number")
        return
    if resp == 1:
        enterNewWords(words)


main()