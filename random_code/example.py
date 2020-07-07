path = 'c:/Users/space/OneDrive/Files/Python/python/'
file_names = ['dogs.txt','cats.txt']

for name in file_names:     
    try:
        with open(path + name) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(content)




# print(contents[3:100])