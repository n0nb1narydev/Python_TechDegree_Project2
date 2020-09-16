import constants
import copy



teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
experienced = []
inexperienced = []
bandits = []
panthers = []
warriors = []
# function that balances players across the three teams
    # Ex: num_players_team = len(PLAYERS) / len(TEAMS)

# when menu or stats display to console, should be readable with \n

def menu():
    print("              ________             \n      o      |   __   |            \n        \_ O |  |__|  |            \n     ____/ \ |___WW___|            \n     __/   /     ||                \n                 ||                \n                 ||                \n  _______________||________________\n")
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
            display_team("Bandits", bandits)
        elif second_command == 2:
            display_team("Panthers", panthers)
        elif second_command == 3:
            display_team("Warriors", warriors)
        else:
            raise ValueError("Enter a valid number. Try again.")
    except ValueError:
        ("Enter a valid number")


def convert_player_height():
    for player in players:
    # Converts height to integer
        height = player['height'].split(" ")
        player['height'] = int(height[0])


def convert_player_exp():
    for player in players:
        if player['experience'] == "YES":
            player['experience'] = bool("YES")
            experienced.append(player)
        elif player['experience'] == "NO":
            player['experience'] = bool("")
            inexperienced.append(player)


def create_teams():
    bandits.extend(experienced[:3])
    bandits.extend(inexperienced[:3])
    panthers.extend(experienced[3:6])
    panthers.extend(inexperienced[3:6])
    warriors.extend(experienced[6:])
    warriors.extend(inexperienced[6:])


def guardian_list(team):
    guardian = []
    print("\n        Guardians:")
    for i in range(0, 6, 1):
        guardian.append(team[i]['guardians'].split(","))
    # ", ".join(guardian)
        guardian.split("and")
    print(guardian)


def display_team(team_name, team):
    print(f"\n\n        {team_name} Stats\n      -----------------")
    print("\n        Players:\n")
    for i in range(0, 6, 1):
        print("          " + team[i]['name'])
    guardian_list(team)
    print("\n\n There are {} experienced players, {} inexperienced players, and {} total players on this team.")
    print("The average height is: {}\n")



if __name__ == "__main__":
    convert_player_height()
    convert_player_exp()
    create_teams()


    # To start game
    menu()