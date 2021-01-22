import random

choices = ["rock", "paper", "scissors"]

print("Rock, Paper, Scissors\nand...\nSHOOT!")


def play_game():
    user_choice = input("\nWhat is your move? ")
    opponent_choice = random.choice(choices)

    def print_matchup():
        print(f"\t{user_choice.title()} vs. {opponent_choice.title()}:")

    if user_choice.lower() == "rock":
        if opponent_choice == "rock":
            print_matchup()
            print("\tIt's a draw! Try again.")
            play_game()
        if opponent_choice == "paper":
            print_matchup()
            print("\tYou lose!")
            play_again()
        if opponent_choice == "scissors":
            print_matchup()
            print("\tYou win!")
            play_again()

    elif user_choice.lower() == "paper":
        if opponent_choice == "rock":
            print_matchup()
            print("\tYou win!")
            play_again()
        if opponent_choice == "paper":
            print_matchup()
            print("\tIt's a draw! Try again.")
            play_game()
        if opponent_choice == "scissors":
            print_matchup()
            print("\tYou lose!")
            play_again()

    elif user_choice.lower() == "scissors":
        if opponent_choice == "rock":
            print_matchup()
            print("\tYou lose!")
            play_again()
        if opponent_choice == "paper":
            print_matchup()
            print("\tYou win!")
            play_again()
        if opponent_choice == "scissors":
            print_matchup()
            print("\tIt's a draw! Try again.")
            play_game()

    else:
        print("\tInvalid move! Try again.")
        play_game()


def play_again():
    ask_play_again = input("\nWould you like to play again? ")
    if ask_play_again.lower() == "yes":
        play_game()
    else:
        quit()


play_game()