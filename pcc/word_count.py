print("enter 'q' to exit the program anytime")
while True:
    try:
        x = input("give me a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("give me a number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Please enter only numbers.")
    else:
        print(x+y)