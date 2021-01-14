import random

# Create string containing possible characters
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ0123456789!@$%^&*"


def create_password():
    # Ask user how many passwords to create
    password_count = input("How many passwords would you like to create? ")

    # Ask user how many characters to make the password
    char_count = input("How many characters will your password(s) be? ")

    # Ask user what applications the passwords will be for
    apps = input("Enter the app(s) you are creating a password for, separated by commas if multiple: ")
    split_apps = apps.split(", ")

    # Create certain number of passwords as requested
    for x in range(int(password_count)):
        new_password = ''
        password_dict = {}

        # Create each individual password
        for i in range(int(char_count)):
            character = random.choice(chars)
            new_password += character

        # Create a dictionary to link each password with its corresponding application
        password_dict[split_apps[x]] = new_password

        # Store each password in text file
        with open('passwords.txt', 'a') as file:
            file.write(f'Your password for {split_apps[x].title()} is: {new_password}\n')

        # Print each password
        print(f"\t>> Your new password for {split_apps[x].title()} is: {new_password}")

    # Ask user if they want to make any more passwords
    ask_more = input("Would you like to create any more passwords? ")
    if ask_more.lower() == "yes" or ask_more.lower() == "y":
        create_password()
    else:
        print("Have a great day!")


create_password()
