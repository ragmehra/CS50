import random

# Randomly generates ten (10) math problems formatted as X + Y = , 
# wherein each of X and Y is a non-negative integer with 𝑛digits. 
# No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. 
# If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, 
# allowing the user up to three tries in total for that problem. 
# If the user has still not answered correctly after three tries, 
# the program should output the correct answer.

def main():
    level = get_level()
    total_problems = 10
    problems = create_problems(level, total_problems)
    score = 0

    for problem in problems: 
        answer = problem[0] + problem[1]
        for i in range(3): 
            try:
                guess = int(input(f"{problem[0]} + {problem[1]} = "))
            except ValueError: 
                pass

            if guess == answer: 
                score += 1
                break
            else: 
                print("EEE")
            if i == 2: 
                print(f"{problem[0]} + {problem[1]} = {answer}")
            

    print(f"Score: {score}")





# Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
    n = None
    while n != '1' and n != '2' and n != '3':
        n = input("Level: ")
    return int(n)

# generate_integer returns a single randomly generated non-negative integer with level digits 
# or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    if level != 1 and level != 2 and level != 3: 
        raise ValueError
    elif level == 1:
        number = random.randint(0,9)
    elif level == 2: 
        number = random.randint(10, 99)
    elif level == 3: 
        number = random.randint(100, 999)
    return number

def create_problems(level, total): 
    problems = [(generate_integer(level), generate_integer(level)) for _ in range(total)]
    return problems

if __name__ == "__main__":
    main()