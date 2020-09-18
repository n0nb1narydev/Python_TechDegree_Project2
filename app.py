import constants
import copy


teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
experienced = []
inexperienced = []
bandits = []
panthers = []
warriors = []


def menu():
    """ main menu called at the beginning and anytime return is selected """
    print("              ________             \n      o      |   __   |            \n        \_ O |  |__|  |            \n     ____/ \ |___WW___|            \n     __/   /     ||                \n                 ||                \n                 ||                \n  _______________||________________\n")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n        BASKETBALL TEAM STATS\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n\n    --------- Main Menu ---------\n\n")
    print("     What would you like to do?\n\n        1) Display Team Stats\n        2) Quit\n\n")
    first_command = None

    while first_command != 1 or first_command != 2:
        try:
            first_command = int(input("Please enter a 1 or a 2: "))
            if first_command > 2:
                raise ValueError("Enter a valid option.")
        except ValueError as error:
            print("Enter a valid option.")
        else:
            if first_command == 1:
                display_teams()
                break
            elif first_command == 2:
                print("Thanks for using my stats tool!")
                break
            else:
                continue



def display_teams():
    """ displays the list of teams to view stats for """
    print("\n\n    Which Team would you like to view stats for?\n")
    for index, team in enumerate(sorted(teams), 1):
        print(f'        {index}) {team}')
    print("\n")
    second_command = None

    while second_command != 1 or second_command != 2 or second_command != 3:
        try:
            second_command = int(input("Please enter a 1, 2, or a 3: "))
            if second_command > 3:
                raise ValueError("Enter a valid option.")
        except ValueError as error:
            print("Enter a valid option.")
        else:
            if second_command == 1:
                display_team("Bandits", bandits)
                break
            elif second_command == 2:
                display_team("Panthers", panthers)
                break
            elif second_command == 3:
                display_team("Warriors", warriors)
                break
            else:
                continue


def convert_player_height():
    """ converts height to integer """
    for player in players:
        height = player['height'].split(" ")
        player['height'] = int(height[0])


def convert_player_exp():
    """ converts experience to boolean value """
    for player in players:
        if player['experience'] == "YES":
            player['experience'] = bool("YES")
            experienced.append(player)
        elif player['experience'] == "NO":
            player['experience'] = bool("")
            inexperienced.append(player)


def create_teams():
    """ separates teams based on experience """
    bandits.extend(experienced[:3])
    bandits.extend(inexperienced[:3])
    panthers.extend(experienced[3:6])
    panthers.extend(inexperienced[3:6])
    warriors.extend(experienced[6:])
    warriors.extend(inexperienced[6:])


def guardian_list(team):
    """ creates list of guardians separated by commas """
    guardian = []
    print("\n        Guardians:\n")
    for i in range(0, 6, 1):
        guardian.append(", ".join(team[i]["guardians"].split(" and ")))
    print("    " + ", ".join(guardian))


def display_team(team_name, team):
    """ displays the selected team from the menu """
    team_list = []
    num_experienced = 0
    num_inexperienced = 0
    total_height = 0
    team_size = len(team_list)
    avg_height = 0

    print(f"\n\n        {team_name} Stats\n      -----------------")
    print("\n        Players:\n")

    for i in range(0, 6, 1):
        team_list.append(team[i]['name'])
        if team[i]["experience"] == True:
            num_experienced += 1
        elif team[i]["experience"] == False:
            num_inexperienced += 1
        total_height += team[i]["height"]

    print("    " + ", ".join(team_list))
    guardian_list(team)
    print(f"\n\n    There are {num_experienced} experienced players, {num_inexperienced} inexperienced players, and {team_size} total players on this team.")
    print("    The average height is: {}\n\n\n".format(round(total_height / len(team_list), 1)))
    return_to_menu()



def return_to_menu():
    """ gives player option to return to main menu or quit the application """
    return_menu = None
    while return_menu != "R" or return_menu != "Q":
        try:
            return_menu = input("Press 'R' to return to the main menu or 'Q' to quit: ")
        except ValueError as error:
            print("Enter a valid option.")
        else:
            if return_menu.upper() == 'R':
                menu()
                break
            elif return_menu.upper() == "Q":
                print("Thanks for using my stats tool!")
                break
            else:
                continue


if __name__ == "__main__":
    convert_player_height()
    convert_player_exp()
    create_teams()
    # To start game
    menu()