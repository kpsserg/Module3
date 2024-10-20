def greet_users(names):
    for name in names:

        msg = f"Hello, {name.title()}!"
        print(msg)
    names.clear()

usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)
print(usernames)

usernames = ['hannah', 'ty', 'margot']
print(usernames)
greet_users(usernames[:])
print(usernames)