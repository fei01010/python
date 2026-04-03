puppies_available = ['lily','guilong','tianrun','wei']
puppies_preference = ['lily','wei','yu']
for puppy in puppies_preference:
    if puppy in puppies_available:
        print(f"{puppy} will be your new friend!")
        print(f"Please take good care of {puppy}!")
    else:
        print(f"Regret to inform you that {puppy} has been adopted.")
print("Thanks for your understanding!")
    