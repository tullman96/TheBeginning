import random

# Create string containing possible characters
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ0123456789!@$%^&*"


def create_password():
    # Ask user how many passwords to create
    password_count = input("How many passwords would you like to create? ")

    # Ask user how many characters to make the password
    char_count = input("How many characters will your password be? ")

    # Create certain number of passwords as requested
    for x in range(int(password_count)):
        new_password = ''

        # Create each individual password
        for i in range(int(char_count)):
            character = random.choice(chars)
            new_password += character

        # Print each password
        print(f"\t>> Your new password is: {new_password}")

    # Ask user if they want to make any more passwords
    ask_more = input("Would you like to create any more passwords? ")
    if ask_more.lower() == "yes" or ask_more.lower() == "y":
        create_password()
    else:
        print("\nHave a great day!")


create_password()
