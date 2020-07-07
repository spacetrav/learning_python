absolute_path = '/Users/space/OneDrive/Files/Python/python/pcc'
filename = '/guest.txt'
n = 0

while n in range(3):
    guest_name = input('What is your name: ')

    with open(absolute_path + filename, 'a') as file_object:
        file_object.write(guest_name + "\n")
    n += 1
