#try except finally

def ask():
    while True:
        try:
            n=int(input("Enter the number"))
        except:
            print("Whoops! Thats not a number")
        else:
            break
    return n**2

print(ask())
