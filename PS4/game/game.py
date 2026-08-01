import random
import sys

def main(): 
    while True:
        try:
            #prompt user for a level
            level = int(input("Level: "))
            #check that it's a positive number, otherwise re:prompt
            if level > 0: 
                #create answer, a random number between 1 and level
                answer = random.randint(1,level)
                print(f"Answer: {answer}")

                #prompt the user to guess the answer, give hints if wrong until they guess right
                
                while True:  
                    try:
                        guess = int(input("Guess: "))
                        if guess <= 0: 
                            raise ValueError
                        if guess < answer: 
                            print("Too small!")
                        elif guess > answer: 
                            print("Too large!")
                        elif guess == answer: 
                            break
                    except ValueError: 
                        pass
                    

                print("Just right!")
                return
                    
        except (ValueError, TypeError):
            pass
        
if __name__ == "__main__":
    main()