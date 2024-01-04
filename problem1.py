def piggify(text):
    list = 'aeiou'
    newW = ""
    if text[0] in list:
        newW = text + "yay"
    else:
        i = 0
        while(text[0] not in list and i < len(text)):
            text = text[1:] + text[0]
            i = i+1
        newW = text + "ay"
    print(newW)

def tester():
    word = ""
    while(word != "."):
        word = input("Please type a word to be piggified: \n")
        if(word != "."):
            piggify(word)
        else:
            print("Thank you for playing!")
