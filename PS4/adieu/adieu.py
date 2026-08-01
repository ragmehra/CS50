def main(): 
    names = []
    #neverending loop collecting names
    while True: 
        #Collect names
        try: 
            name = input("Name: ")
            names.append(name)

        #catching user Ctrl + D
        except EOFError:
            print()
            if len(names) == 1: 
                print(f"Adieu, adieu, to {names[0]}")
            elif len(names) == 2: 
                print(f"Adieu, adieu, to {names[0]} and {names[1]}")
            else:
                #collect last name, join list with commas, add last name with final and
                last_name = names.pop()
                print("Adieu, adieu, to " + ", ".join(names) + f", and {last_name}")

            break


if __name__ == "__main__":
    main()