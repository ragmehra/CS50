def main(): 

    d = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True: 
        date = input("Date: ")
        try: 
            if "/" in date: 
                date = date.strip().split("/")
                date[0] = int(date[0])
                date[1] = int(date[1])
                date[2] = int(date[2])

                if 1 <= date[0] <= 12 and 1 <= date[1] <= 31: 
                    print(f"{date[2]}-{date[0]:02}-{date[1]:02}")
                    return
                else:
                    continue
            else: 
                for m in d:
                    if date.startswith(m): 
                        date = date.strip().split()
                        date[0] = d[date[0]]
                        date[1] = int(date[1][:-1])
                        date[2] = int(date[2])
                        #print(date)

                        if 1 <= date[0] <= 12 and 1 <= date[1] <= 31: 
                            print(f"{int(date[2])}-{date[0]:02}-{int(date[1]):02}")
                            return
                        
        except ValueError: 
            print("Value Error")
            pass

                    


if __name__ == "__main__": 
    main()