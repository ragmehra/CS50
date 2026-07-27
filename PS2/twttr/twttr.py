def main(): 
    user_input = input("Word: ")
    print(remove_vowels(user_input))


def remove_vowels(word): 
    result = ''
    for l in word: 
        if l in "aeiouAEIOU": 
            continue
        else: 
            result = result + l

    return result


if __name__ == "__main__": 
    main()