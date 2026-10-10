def login(f):
    def wrapper(*args):
        print("Welcome")
        f(*args)
        if args[0]=="admin":
            print("You are an Administrator")
        else:
            print("You are a User")
    return wrapper

@login
def user(username):
    print(f"I am a {username}")
user("admin")

@login
def user(username):
    print(f"I am a {username}")

user("user")
