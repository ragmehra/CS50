def main(): 
    word = input("Camel Case: ")
    to_snake(word)
    print(f"Snake Case: {to_snake(word)}")


def to_snake(camel_word): 
    result = ''
    for l in camel_word: 
        if l.isupper() == True: 
            result = result + "_" + l.lower()
        else: 
            result = result + l
    return result

if __name__ == "__main__": 
    main()