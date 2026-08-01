import sys
import random
from pyfiglet import Figlet

def main(): 
    #set up figlet and fonts list
    figlet = Figlet()
    fonts = figlet.getFonts()

    #Check if length of argv is greater than 1
    if len(sys.argv) > 1: 

        #check that argv[1] and argv[2] inputs are correct, otherwise exit
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] == font for font in fonts):

            #if argv input are correct, set up font values 
            figlet.setFont(font=sys.argv[2])
        else: 
            sys.exit("Invalid usage")
    #if lenght is 1, set font to random 
    elif len(sys.argv) == 1: 
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)
    
    #Take input
    text = input("Input: ")
    #Print output 
    print(figlet.renderText(text))





if __name__ == "__main__":
    main()