
""" def main(): 
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
            pass """
            

def main():
    while True: 
        fuel = input("Input: ")
        fuel = convert(fuel)
        if gauge(fuel): 
            print (gauge(fuel))
            break



# 1. convert expects a str in X/Y format as input, 
# 2. wherein X is a non-negative integer and Y is a positive integer, 
# and returns that fraction as a percentage rounded to the nearest int 
# between 0 and 100, inclusive. 
# If X and/or Y is not an integer, or if X is greater than Y, 
# then convert should raise a ValueError. 
# If Y is 0, then convert should raise a ZeroDivisionError.
def convert(fraction):
    
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0: 
            raise ZeroDivisionError
        if x > y or x < 0 or y < 0:
            raise ValueError
        
        if x >= 0 and y > 0: 
            if x <= y:
                return round((x * 100)/ y)
    

def gauge(percentage):
    if percentage >= 99: 
        return "F"
    elif percentage <= 1: 
        return "E"
    elif 1 < percentage < 100: 
        return f"{percentage}%"


if __name__ == "__main__":
    main()