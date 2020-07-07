absolute_path = '/Users/space/OneDrive/Files/Python/rename'
filename = absolute_path + '/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

    # contents = file_object.read()
    # print(contents.rstrip())