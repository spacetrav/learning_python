# initialize
my_dict = {}

# add item
my_dict['name'] = 'Travis'
my_dict['state'] = 'South Dakota'
my_dict['age'] = 22

# access item
print my_dict['name']

# change item
my_dict['name'] = 'SpaceTrav'
print my_dict['name']
print my_dict

# remove an item by index
# del my_dict['state']
print my_dict

# iterate
for k, v in my_dict.iteritems():
    print k, '=>', v