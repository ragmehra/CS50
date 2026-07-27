def main(): 
    due = 50
    while due > 0: 
        print(f"Amount Due: {due}")
        insert = int(input("Insert Coin: "))
        if insert == 0: 
            print("Not a valid amount")
            continue
        elif insert == 25 or insert == 10 or insert == 5:
            due = due - insert
        else: 
            print("Not a valid amount")

    change =  due * -1
    print(f"Change Owed: {change}") 





if __name__ == "__main__": 
    main()