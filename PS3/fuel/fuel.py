def main(): 
    while True: 
        try: 
            fuel = input("Input: ")
            x, y = fuel.split("/")
            x = int(x)
            y = int(y)

            if x >= 0 and y > 0: 
                if x <= y:
                    fuel = round((x * 100)/ y)
                    #print(f"fuel: {fuel}")
                    if fuel >= 99: 
                        print("F")
                    elif fuel <= 1: 
                        print("E")
                    elif 1 < fuel < 100: 
                        print(f"{fuel}%")
                    break
        except (ValueError, ZeroDivisionError): 
            pass










if __name__ == "__main__":
    main()