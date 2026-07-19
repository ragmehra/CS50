def main(): 

    filename = input("Filename: ")

    filename = filename.strip().lower()

    #.gif
    if filename.endswith(".gif"):
        print("image/gif")

    #.jpg
    elif filename.endswith(".jpg"):
        print("image/jpeg")

    #.jpeg
    elif filename.endswith(".jpeg"):
        print("image/jpeg")

    #.png
    elif filename.endswith(".png"):
        print("image/png")

    #.pdf
    elif filename.endswith(".pdf"):
        print("application/pdf")

    #.txt
    elif filename.endswith(".txt"):
        print("text/plain")
    #.zip
    elif filename.endswith(".zip"):
        print("application/zip")

    else: 
        print("application/octet-stream")



main()