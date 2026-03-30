def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")

username = input("What's your name?master ")
greet_user(username)

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie','cat')