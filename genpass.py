import secrets
import random
import string

store = {}


def password_gen(u_name):
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.hexdigits)
    password += secrets.choice(string.octdigits)
    password += secrets.choice(string.octdigits)
    password += secrets.choice(string.punctuation)
    password = list(password)
    random.shuffle(password)
    store[u_name] = "".join(password)


def username():
    user_id = input("Enter User ID : ")
    if (user_id not in store.keys()) and (" " not in user_id):
        password_gen(user_id)
    else:
        print("Already ExistS!!! Try Again")
        username()


def get_data():
    print()
    for key , value in store.items():
        print("{} : {}".format(key, value))


if _name_ == "_main_":
    for i in range(int(input("Enter No. of Users :"))):
        username()
    while 1:
        ch = input("Enter your username")
        if ch in store.keys():
            print("{} : {}".format(ch, store[ch]))
            break
