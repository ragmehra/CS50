import requests
import sys

def main(): 
    try: 
        if len(sys.argv) <= 1: 
            sys.exit("Missing command line argument")
        elif float(sys.argv[1]): 
            n = float(sys.argv[1])
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f694383ee07a771b382bc2736dfe0c0f8f2fe9fe33753c8383677c0c20192533")
            price = float(response.json()['data']["priceUsd"])
            bit_in_usd = n * price
            print(f"${bit_in_usd:,.4f}")
            
    except ValueError: 
        sys.exit("Command line argument not a number")


if __name__ == "__main__": 
    main()