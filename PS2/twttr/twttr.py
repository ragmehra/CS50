def main(): 
    user_input = input("Word: ")
    print(shorten(user_input))


def shorten(word): 
    result = ''
    for l in word: 
        if l in "aeiouAEIOU": 
            continue
        else: 
            result = result + l

    return result


if __name__ == "__main__": 
    main()