import requests
from bs4 import BeautifulSoup

# The website to scrape info from
base_url = 'https://www.baseball-reference.com/leaders/TB_career.shtml'
req = requests.get(base_url)
soup = BeautifulSoup(req.content, 'lxml')

# Create a list with each player and their number of years in MLB
player_and_career_length = soup.find_all('td', class_='')
player_list = list(player_and_career_length)

formatted_player_list = []

# Turn each entry into a string that can be manipulated
for item in player_list:
    item_string = str(item.text)
    # Remove the + from any entry that has it. Fix an issue with spaces. Split by space to get rid of unnecessary info.
    formatted_player = item_string.replace('+', '').replace('\xa0', ' ').split(' ')
    # Create the formatted list of players
    formatted_player_list.append(formatted_player[0] + ' ' + formatted_player[1])

# Find the total number of bases for each player
player_rank_bases_and_bats = soup.find_all('td', csk='')

# Create the formatted list containing rank, total bases, and bat hand
formatted_rank_bases_and_bats_list = []
for entry in player_rank_bases_and_bats:
    x = entry.text
    formatted_rank_bases_and_bats_list.append(x)

# Grab each third entry to create a formatted list of total bases
formatted_bases_list = []
step = range(1, 3000, 3)
for num in step:
    formatted_bases_list.append(formatted_rank_bases_and_bats_list[num])

# Create dictionary that matches each player to their respective total career bases
player_dict = {}
for i in range(0, 1000):
    player_dict[formatted_player_list[i]] = formatted_bases_list[i]


def find_total_bases():
    """Enter a player to find out how many bases they collected over their career,
    and how many miles they traveled."""
    input_player = input("\nEnter player: ").title()
    if input_player in player_dict:
        print(f"{input_player} collected {player_dict[input_player]} total bases. That means he traveled "
              f"{int(player_dict[input_player])*90/5280} miles over the course of his career!")
        ask_again = input("Would you like to look up another player? ")
        if ask_again.lower() == "yes":
            find_total_bases()
        else:
            quit()
    else:
        print(f"{input_player} did not make the list. Try a different player.")
        find_total_bases()


find_total_bases()
