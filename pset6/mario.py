while True:
    try:    
        h = int(input("Enter a number: "))
        if h < 9 and h > 0:
            break
    except:
        h = ValueError
        print("Try again!")

for i in range(h):
    print((h - 1 - i) * " ", end="")
    print((i + 1) * "#", end="")
    print("  ", end="")
    print((i + 1) * "#")
    
    
        

