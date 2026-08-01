import emoji


def main(): 
    output = input("Input: ")
    print(emoji.emojize(f"Output: {output}", language='alias'))



if __name__ == "__main__": 
    main()