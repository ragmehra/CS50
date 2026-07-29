def main(): 
    grocery_list = {}
    while True: 
        try: 
            item = input().strip().upper()
            if item in grocery_list: 
                grocery_list[item] += 1
            else: 
                grocery_list.update({item: 1})

        except EOFError: 
            a_list = sorted(grocery_list)
            for i in a_list: 
                print(f"{grocery_list[i]} {i}")
            break






if __name__ == "__main__": 
    main()