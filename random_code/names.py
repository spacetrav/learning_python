import name_function as nf 

print("Enter 'q' at any time to quit")
while True:
    first = input("\nEnter first name: ")
    if first == 'q':
        break
    last = input("\nEnter last name: ")
    if last == 'q':
        break

    formatted_name = nf.get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')