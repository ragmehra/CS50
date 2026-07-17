def main(): 
    output = playback(input("What would you like to say?"))
    print(output)


def playback(word):
    return word.replace(" ", "...")

main()