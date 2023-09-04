class User:
    def __init__(self, name_) -> None:
        self.name = name_
        self.is_logged = True

def is_authenticated(function):
    def wrapper(*args):
        if args[0].is_logged == True:
            function(args[0])
    return wrapper
@is_authenticated
def create_blog(user):
    print(f"this is {user.name}'s blog post")
new_user = User("nandom")
create_blog(new_user)

