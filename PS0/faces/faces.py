def main(): 
    output = convert(input("What would you like to say?"))
    print(output)


def convert(word):
    return word.replace(":)", "🙂").replace(":(", "🙁")

main()