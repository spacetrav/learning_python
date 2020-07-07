import json

def get_stored_username():
    # Get stored username from json file if available
    filename = 'python/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        print("no file found")
        return None
    else: 
        # print(username)
        return username

def get_new_username():
    username = input("What's your name? ")
    filename = 'python/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
            

def greet_user():
    # Greet user by name
    username = get_stored_username()

    if username:
        print("Welcome back, " + username)
    else:
        username = get_new_username()
        print("We'll remember you, bruh.")
    
    # filename = 'python/username.json'
    # try:
    #     with open(filename) as f_obj:
    #         username = json.load(f_obj)
    # except FileNotFoundError:
        
    # else:
    #     print("Welcome back " + username + "!")
# get_stored_username()
greet_user()
# get_new_username()