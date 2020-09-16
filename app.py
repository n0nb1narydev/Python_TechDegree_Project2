import constants
import copy


teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)





# function that balances players across the three teams
    # Ex: num_players_team = len(PLAYERS) / len(TEAMS)

# when menu or stats display to console, should be readable with \n

def menu():
    print("            ________             \n    o      |   __   |            \n      \_ O |  |__|  |            \n   ____/ \ |___WW___|            \n   __/   /     ||                \n               ||                \n               ||                \n_______________||________________\n")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n        BASKETBALL TEAM STATS\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n\n    --------- Main Menu ---------\n\n")
    
    print("     What would you like to do?\n\n        1) Display Team Stats\n        2) Quit\n\n")
    first_command = int(input("Enter an option: "))
    if first_command == 1:
        display_teams()
    elif first_command == 2:
        print("Thanks for using my stats tool!")


def display_teams():
    print("\n\n    Which Team would you like to view stats for?\n")
    for index, team in enumerate(sorted(teams), 1):
        print(f'        {index}) {team}')
    try:
        second_command = int(input("\n\nEnter an option: "))
        if second_command == 1:
            print("You Chose the Bandits")
        elif second_command == 2:
            print("You Chose the Pathers")
        elif second_command == 3:
            print("You Chose the Warriors")
        else:
            raise ValueError("Enter a valid number. Try again.")
    except ValueError:
        ("Enter a valid number")


def convert_player_values():
    for player in players:
    # Converts height to integer
        height = player['height'].split(" ")
        player['height'] = int(height[0])
        player['experience'] = bool(player['experience'])

    # Converts experience to boolean
        if player['experience'] == "YES":
            player['experience'] = bool("YES")
        elif player['experience'] == "NO":
            player['experience'] = bool("")
        
        print(player['experience'])


if __name__ == "__main__":
    convert_player_values()
    # menu()
    # Covert height to integer


    # Convert experience to bool


