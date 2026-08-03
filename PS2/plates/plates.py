def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validity = False

    if s[0:2].isalpha() == True: 
        if 2 <= len(s) <= 6: 
            if number_check(s) == True: 
                if punctuation_check(s) == True: 
                    return True
                else: 
                    return False

    return False

def number_check(s1): 
    i = 0
    check = ''
    for l in s1: 
        if l.isdigit() == True and l == '0': 
            return False
        elif l.isdigit() == True and l != '0': 
            check = s1[i:]
            #print(f"Check: {check}")
            if check.isdigit() == False:
                return False
            else: 
                return True 
        i += 1
    return True


def punctuation_check(s2): 
    for l in s2: 
        if l in r'''!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ''':
            return False

    return True

if __name__ == "__main__":
    main()