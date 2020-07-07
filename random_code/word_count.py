# path = 'c:/Users/space/OneDrive/Files/Python/python/pcc/'
# file_name = path + 'alice.txt'

def count_words(filename):
# count approximate number of words in the file.
    try:
        with open('c:/Users/space/OneDrive/Files/Python/python/pcc/' + filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_words = len(words)
        print("The number of words found in " + filename + " is: " + str(num_words))


filenames = ['alice.txt','sihhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)

# print(contents[3:100])