from random import randint  # to randomly draw countries
import json  # to handle json filed
from typing import Any, Type  # for type hints
import inflect  # for formatting number strings: 1st, 2nd, 3rd, etc..
from Resources.myStyles import Colors  # for formatting strings with colors
from colorama import Fore, Back, Style  # used for color formatting with highlighting (ex. wrong/correct answers)

COUNTRIES = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
             'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland',
             'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco',
             'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia',
             'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine',
             'United Kingdom']

Countries_to_Check = ['Albania', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
                      'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
                      'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Moldova', 'Netherlands', 'Norway',
                      'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
                      'Switzerland', 'Ukraine', 'United Kingdom']

CAPITALS = ['Tirana', 'Andorra la Vella', 'Vienna', 'Minsk', 'Brussels', 'Sarajevo', 'Sofia', 'Zagreb', 'Prague',
            'Copenhagen', 'Tallinn', 'Helsinki', 'Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome',
            'Riga', 'Vaduz', 'Vilnius', 'Luxembourg', 'Valletta', 'Chisinau', 'Monaco', 'Podgorica', 'Amsterdam',
            'Skopje', 'Oslo', 'Warsaw', 'Lisbon', 'Bucharest', 'Moscow', 'San Marino', 'Belgrade', 'Bratislava',
            'Ljubljana', 'Madrid', 'Stockholm', 'Bern', 'Kiev', 'London']

COUNTRIES_AND_CAPITALS = {'Albania': 'Tirana', 'Andorra': 'Andorra la Vella', 'Austria': 'Vienna', 'Belarus': 'Minsk',
                          'Belgium': 'Brussels', 'Bosnia and Herzegovina': 'Sarajevo', 'Bulgaria': 'Sofia',
                          'Croatia': 'Zagreb', 'Czech Republic': 'Prague', 'Denmark': 'Copenhagen',
                          'Estonia': 'Tallinn', 'Finland': 'Helsinki', 'France': 'Paris', 'Germany': 'Berlin',
                          'Greece': 'Athens', 'Hungary': 'Budapest', 'Iceland': 'Reykjavik', 'Ireland': 'Dublin',
                          'Italy': 'Rome', 'Latvia': 'Riga', 'Liechtenstein': 'Vaduz', 'Lithuania': 'Vilnius',
                          'Luxembourg': 'Luxembourg', 'Malta': 'Valletta', 'Moldova': 'Chisinau', 'Monaco': 'Monaco',
                          'Montenegro': 'Podgorica', 'Netherlands': 'Amsterdam', 'North Macedonia': 'Skopje',
                          'Norway': 'Oslo', 'Poland': 'Warsaw', 'Portugal': 'Lisbon', 'Romania': 'Bucharest',
                          'Russia': 'Moscow', 'San Marino': 'San Marino', 'Serbia': 'Belgrade',
                          'Slovakia': 'Bratislava', 'Slovenia': 'Ljubljana', 'Spain': 'Madrid', 'Sweden': 'Stockholm',
                          'Switzerland': 'Bern', 'Ukraine': 'Kiev', 'United Kingdom': 'London'}

all_users = dict()


def createDict(data_keys: list, data_values: list) -> dict:
    """
    Creates a dict from two lists; first one as key and second list as values.
    Used as countries_and_capitals generator.
    @:param data_keys: list that will be assigned as keys to the dict.
    @:param data_values: list that will be assigned as values to the dict.
    :return: dict of combined two lists.
    """
    complete_dict = dict()  # at the beginning it was "countries and capitals"
    for i in range(len(data_keys)):
        complete_dict[data_keys[i]] = data_values[i]
    print(complete_dict)
    return complete_dict


def createList(f_name: str) -> list:
    """
    Creates a list from a text file.
    @param f_name: File's name to be converted.
    @return: list from data entered.
    """
    # countries_txt_f = "Countries.txt"
    # capitals_txt_f = "Capitals.txt"
    data = ""
    with open(f_name) as f:
        f_txt = f.read()
    for line in f_txt:
        # country = COUNTRIES.append(line)
        # country += line
        data += line
    # COUNTRIES = country.split("\n")
    constant_data = data.split("\n")
    print(constant_data)
    return constant_data


def checkX() -> None:
    from random import randint
    print("Length of dict:", len(COUNTRIES_AND_CAPITALS.keys()))
    x_s = list()
    for i in range(50):
        x = randint(0, len(COUNTRIES_AND_CAPITALS.keys()) - 1)
        x_s.append(x)
        print(x, end=", ")
    x_s.sort()
    print("\n", x_s)


def drawCountry() -> str:
    """
    Draws a random number from 0 to the length of the countries and capitals dict.
    @return: Country from COUNTRIES list.
    """
    x = randint(0, len(Countries_to_Check) - 1)  # len func starts from 1, whereas indexing from list starts from 0
    return Countries_to_Check[x]


def severalCountries(r: int) -> set:
    """
    Creates a set of unique countries, randomly selected.
    :param r: Number of rounds player wishes to play.
    :return: Set of selected randomly countries.
    """
    random_countries = set()
    while len(random_countries) < r:
        x = randint(0, len(Countries_to_Check) - 1)  # len func starts from 1, whereas indexing from list starts from 0
        random_countries.add(Countries_to_Check[x])
    return random_countries


def guessCountry(country: str) -> str:
    """
    Receives a country from drawCountry, prompts an input for a user answer.
    @param country: Random country from COUNTRIES list
    @return: user's answer of the country
    """
    print("What is", Colors.BOLD + country + Colors.END + "'s capital?")
    usr_answer = input(">>> ")
    usr_answer = usr_answer.lower().title()
    return usr_answer


def addScore(usr_name: str, score_to_add: int) -> None:
    """
    Adds score to user's dict according to his answer.
    @param usr_name: User's name to look up in the users table (all_users.json)
    @param score_to_add: int of score to be added to the dict
    @return: None
    """
    with open("Resources/all_users.json", "r") as usrs_r_f:
        users = json.load(usrs_r_f)  # this is now a dict
        current_score = users[usr_name]["Score"]  # check what is the current user's score
    with open("Resources/all_users.json", "w") as usrs_w_f:
        new_score = current_score + score_to_add
        users[usr_name]["Score"] = new_score
        json.dump(users, usrs_w_f, indent=2)


def deductScore(usr_name: str, score_to_deduce: int) -> None:
    """
    Deduct score to user's dict according to his wrong answer.
    @param usr_name: User's name to look up in the users table (all_users.json)
    @param score_to_deduce: int of score to be deducted from the dict
    @return: None
    """
    with open("Resources/all_users.json", "r") as usrs_r_f:
        users = json.load(usrs_r_f)  # this is now a dict
        current_score = users[usr_name]["Score"]  # check what is the current user's score
    with open("Resources/all_users.json", "w") as usrs_w_f:
        new_score = current_score - score_to_deduce
        users[usr_name]["Score"] = new_score
        json.dump(users, usrs_w_f, indent=2)


def checkAnswer(usr_name: str, country: str) -> bool:
    """
    Checks if user's input is correct; If user asks for hint, calls reqHint for hint prompts; if answer is not hint and
    not correct - checks for spelling through spellCheck. (later, if answer is not close to the answer, answer is marked
    wrong and points are deducted).
    @param usr_name: User's name to look up in the users table (all_users.json)
    @param country: Country to be checked.
    @return: Boolean if answer is true, or calls reqHint or spellCheck. [currently there is no use in returned bool]
    """
    answer = guessCountry(country)
    capital = COUNTRIES_AND_CAPITALS[country]
    correct_answer = "\n" + Back.GREEN + "Correct!" + Style.RESET_ALL + " " + country + \
                     "'s capital is indeed", capital + ".\n"
    if answer == capital:
        print(*correct_answer)  # correct_answer is tuple, * is unpacking to print normal
        addScore(usr_name=usr_name, score_to_add=5)  # adds 5 points to player
        return True
    elif answer == "Hint":
        reqHint(answer, country, capital, usr_name=usr_name)
    else:
        spellCheck(answer, country, capital, usr_name=usr_name)


def checkAnotherCapital():
    # func to check if user's answer is another country's capital.
    # ex - user entered Stockholm for Norway, func will return Stockholm's country.
    pass


def reqHint(answer: str, country: str, capital: str, usr_name: str) -> bool:  # currently not working
    """
    NOT WORKING PROPERLY ATM; loop problems - function won't exit properly if there is max hints and the answer is wrong
    If user asks for hint in answer prompt, func uncovers one letter at the time from answer (capital) until reaching
    max hints = length of capital minus 2 letters.
    @param answer: user's answer
    @param country: country being checked
    @param capital: capital of the country being checked == correct answer
    @param usr_name: User's name to look up in the users table (all_users.json)
    @return: Boolean if answer is true, or calls spellCheck to see if answer is close to capital
    """
    p = inflect.engine()  # convert number to numeric suffix: 1st, 2nd, 3rd, etc...
    # wrong_answer = "\nWrong ;(\n" + country + "'s capital is", capital + ".\n"
    correct_answer = "\n" + Back.GREEN + "Correct!" + Style.RESET_ALL + " " + country + \
                     "'s capital is indeed", capital + ".\n"
    max_hints = len(capital) - 2  # maximum number of hints = the length of the capitals name minus 2.
    hint_loc = 1  # flagger inside while loop to indicate location; 0 has no meaning since going up until this location.

    def checkInsideAnswer(country, capital, usr_name):
        sec_answ = input(">>> ")
        sec_answ = sec_answ.lower().title()
        if sec_answ == capital:
            print(*correct_answer)  # correct_answer is tuple, * is unpacking to print normal
            addScore(usr_name=usr_name, score_to_add=2)  # adds 2 points to player
            return True
        else:
            spellCheck(sec_answ, country, capital, usr_name=usr_name)

    if answer == capital:
        print(*correct_answer)  # correct_answer is tuple, * is unpacking to print normal
        addScore(usr_name=usr_name, score_to_add=2)  # adds 2 points to player
        return True
    elif hint_loc >= max_hints and answer != capital:
        print("Sorry, you've reached maximum hints.")
        checkInsideAnswer(capital=capital, country=country, usr_name=usr_name)
        # second_answer = input(">>> ")
        # second_answer = second_answer.lower().title()
        # if second_answer == capital:
        #     print(*correct_answer)  # correct_answer is tuple, * is unpacking to print normal
        #     addScore(usr_name=usr_name, score_to_add=2)  # adds 2 points to player
        #     return True
        # else:
        #     spellCheck(second_answer, country, capital, usr_name=usr_name)
    elif answer == "Hint":
        print("The " + str(p.ordinal(hint_loc)) + " letter is " + capital[:hint_loc])
        hint_loc += 1
        checkInsideAnswer(capital=capital, country=country, usr_name=usr_name)
        # while hint_loc <= max_hints and (second_answer == "Hint" or answer == "Hint"):
        #     # if hint_loc >= max_hints:
        #     #     print("Sorry, you've reached maximum hints.")
        #     # else:
        #     print("The " + str(p.ordinal(hint_loc)) + " letter is " + capital[:hint_loc])
        #     hint_loc += 1
        #     second_answer = input(">>> ")
        #     second_answer = second_answer.lower().title()
        #     if second_answer == capital:
        #         print(*correct_answer)  # correct_answer is tuple, * is unpacking to print normal
        #         addScore(usr_name=usr_name, score_to_add=2)  # adds 2 points to player
        #         return True
        #     elif answer == "Hint" or second_answer == "Hint":
        #         continue
        #     else:
        #         spellCheck(second_answer, country, capital, usr_name=usr_name)
        #         break
    else:
        spellCheck(answer, country, capital, usr_name=usr_name)
        # return False  # return False only if this is wrong answer again.


def spellCheck(answer: str, country: str, capital: str, usr_name: str) -> bool:
    """
    Checks if user's answer is close to the capital (==correct answer) by checking if either the first 4 letters or the
     last three matches the capital's name.
     (I thought of moving the wrong_answer and correct_answer vars up top to be available as global, but they neet to
     get the country's and capital's that are being checked, and that will complicate things).
    @param answer: user's answer
    @param country: country being checked
    @param capital: capital of the country being checked == correct answer
    @param usr_name: User's name to look up in the users table (all_users.json)
    @return: True if answer is correct, false if answer is wrong.
    """
    wrong_answer = "\n" + Back.BLACK + "Wrong ;(" + Style.RESET_ALL + "\n" + country + "'s capital is", capital + \
                   ".\n"
    correct_answer = "\n" + Back.GREEN + "Correct!" + Style.RESET_ALL + " " + country + \
                     "'s capital is indeed", capital + ".\n"
    if answer == capital:
        print(*correct_answer)  # correct_answer is tuple, * is unpacking to print normal
        addScore(usr_name=usr_name, score_to_add=2)  # adds 2 points to player
        return True
    elif answer.startswith(capital[:4]) or answer.endswith(capital[-3:]):  # number 4 is prone to error for short names
        print("Sorry, couldn't found " + Colors.ITALIC + answer + Colors.END + " in our database.")
        print("Did you mean " + capital + "?")
        second_answer = input(">>> ")
        second_answer = second_answer.upper()
        if second_answer == "YES":  # if user says the suggested name is his answer
            print(*correct_answer)  # correct_answer is tuple, * is unpacking to print normal
            addScore(usr_name=usr_name, score_to_add=2)  # adds 2 points to player
            return True
        else:
            print(*wrong_answer)  # wrong_answer is tuple, * is unpacking to print normal
            deductScore(usr_name=usr_name, score_to_deduce=1)  # deduce 1 point to player
            return False
    else:
        print(*wrong_answer)
        deductScore(usr_name=usr_name, score_to_deduce=2)  # deduce 2 points to player
        return False


def addUser(usr_name: str) -> None:
    """
    Adds the user's name to the dict of all users (all_users.json)
    @param usr_name: User's name to be added
    @return: None
    """
    from datetime import datetime  # used for adding joined date to user

    class User:
        user_id: int | Any = assignID()  # pyCharm suggested that | any, I'm not sure why is it needed.
        today_date = datetime.date(datetime.now())  # gets today's date
        join_date = today_date.strftime("%B, %d, %Y")  # formats date as "Month, DD, Year"; "January, 23, 2023"

        def __init__(self, score):
            self.id = self.user_id
            self.score = score

    with open("Resources/all_users.json", "r") as usrs_r_f:
        users = json.load(usrs_r_f)  # this is now a dict; import json used at top
    with open("Resources/all_users.json", "w") as usrs_w_f:
        new_usr = User(score=0)  # set a new user with the score 0; ID is auto assigned
        users[usr_name] = {"ID": new_usr.id, "Score": new_usr.score, "Join Date": new_usr.join_date}
        json.dump(users, usrs_w_f, indent=2)


def assignID() -> int:
    """
    Reads the last ID assigned from IDs.json, increments by 1, updates the IDs.json.
    @return: New ID to be assigned.
    """
    with open("Resources/IDs.json", "r") as ID_r_f:
        id_data = json.load(ID_r_f)  # Dict of all ids
        last_id = id_data["Last ID"]  # get the last ID assigned
    with open("Resources/IDs.json", "w") as ID_w_f:
        new_id = last_id + 1  # add 1 to the last ID
        id_data["Last ID"] = new_id
        json.dump(id_data, ID_w_f, indent=2)
    return new_id


def checkUser(usr_name: str) -> int:
    """
    Checks if the user's name entered exists in the system; if exists - welcomes him and shows his score, otherwise
    adds the new user to the dict of all users (all_users.json)
    @param usr_name: username to be checked or added.
    @return: Users score (or zero if user is new)
    """
    with open("Resources/all_users.json", "r") as usrs_f:
        users = json.load(usrs_f)
    if usr_name in users.keys():
        print("Welcome back, " + Colors.GREEN + usr_name + Colors.END + "!")
        user_score = Colors.BOLD + str(users[usr_name]["Score"]) + Colors.END
        print("Your current score is " + user_score + ".")
        return user_score
    else:
        print("Welcome to the Countries & Capitals game, " + Colors.GREEN + usr_name + Colors.END + "!")
        addUser(usr_name)  # adds the new user to the .json file of all users.
        return 0  # == user score, which is set to zero since it's a new user.


def getUserData(usr_name: str, data: str) -> None | int:
    """
    Checks if user is in dict of all users (all_users.json); if so - gets the user's data from the dict.
    Used mainly for checking user's score, can be used to check any other data (join date, ID, etc..)
    @param usr_name: User's name to be checked.
    @param data: Type of data to be searched.
    @return: Data requested of user or error if data/user not found.
    """
    with open("Resources/all_users.json", "r") as usrs_f:
        users = json.load(usrs_f)
    if data in users[usr_name]:
        return users[usr_name][data]
    else:
        return None


def CalcLeaderboard(prnt=False) -> list:
    """
    Calculates the leaderboard of players. Gets user data as dict from all_users.json file, creates a new dict of
    usernames and scores, sorts the dict by values and outputs as list of tuples.
    :param prnt: bool - True/False - whether to print or not the top 3 places and their score; default set to False.
    :return: Leaderboard as list of tuples.
    """
    with open("Resources/all_users.json", "r") as usrs_f:
        users = json.load(usrs_f)
    users_scores = {usr: data["Score"] for usr, data in users.items()}  # create a dict of users and scores only
    ldr_brd = (sorted(users_scores.items(), key=lambda item: item[1], reverse=True))  # list of tuples
    if prnt:  # if prnt == True
        first_place = ldr_brd[0]
        second_place = ldr_brd[1]
        third_place = ldr_brd[2]
        print("First place is " + str(first_place[0]) + " with the score of " + str(first_place[1]))
        print("Second place is " + str(second_place[0]) + " with the score of " + str(second_place[1]))
        print("Third place is " + str(third_place[0]) + " with the score of " + str(third_place[1]))

    return ldr_brd


def getUserRank(usr_name: str, ldr_brd: list) -> int:
    """
    Fetches the user's rank from the leaderboard.
    :param usr_name: User's name to be checked.
    :param ldr_brd: Leaderboard to be checked from.
    :return: User's rank in the leaderboard.
    """
    # In the future, implement a feature that checks if the player's location in the leaderboard has changed.
    usr_rank = None
    for usr_lst in ldr_brd:
        if usr_name == usr_lst[0]:
            usr_rank = ldr_brd.index(usr_lst)
    usr_rank += 1  # since place "0" has no meaning, increased by one
    return usr_rank


def printUserRank(usr_rank: int) -> None:
    """
    Prints the user's rank with the inflect module = 1st, 2nd, 3rd, etc..
    :param usr_rank: User's name to be printed.
    :return: None
    """
    p = inflect.engine()  # convert number to numeric suffix: 1st, 2nd, 3rd, etc...
    print(f"You are currently ranked in the {Colors.BOLD}{Colors.YELLOW}{(p.ordinal(usr_rank))}{Colors.END} place.")


def genPodium(ldr_brd: list) -> str:
    """
    Doesn't function properly atm, when changing tags with usernames, the spaces changes as well.
    A suggested solution is to count the amount of whitespaces needed to be perfectly aligned.
    Gets the podium art from podium.txt, switches the top three players from the leaderboard into a new copied file,
    returns  the named podium as str.
    :param ldr_brd: Leaderboard to check the top 3 players from.
    :return: Str of new podium with top 3 player's usernames.
    """
    with open("Resources/podium.txt", "r") as pdm_f:
        art = pdm_f.read()

    first_place = ldr_brd[0]
    second_place = ldr_brd[1]
    third_place = ldr_brd[2]

    winners = [first_place[0], second_place[0], third_place[0], "\t " + str(first_place[1]),
               "\t\t" + str(second_place[1]),
               "\t  " + str(third_place[1]) + "\tֿ"]
    tags = ["@first_p", "@second_p", "@third_p", "@first_score", "@second_score", "@third_score"]
    with open("Resources/podium_winners.txt", "w") as copy_file:
        copy_file.write(art)  # copied the content of the podium txt file to another file; so the file with the winners
        # to be changed will renew every run
    with open("Resources/podium.txt", "r") as read_pdm_f:
        with open("Resources/podium_winners.txt", "w") as pdm_wins_f:
            for line in read_pdm_f:
                for tag, winner in zip(tags, winners):
                    line = line.replace(tag, str(winner))
                pdm_wins_f.write(line)

    with open("Resources/podium_winners.txt", "r") as final_read_f:
        podium = final_read_f.read()  # load the updated podium

    return podium


def changeInScore(old_score: int, new_score: int) -> int:
    """
    Calculates the change in the user's score
    :param old_score: User's score before started playing.
    :param new_score: User's score after finishing playing.
    :return: Difference in score.
    """
    if new_score > old_score:
        diff = new_score - old_score
        print(f'Your score has increased by {Colors.BOLD}{diff}{Colors.END} points.')
        return diff
    elif old_score == new_score:
        print("Your score hasn't changed.")
        return 0
    else:  # if old score > new_score
        diff = old_score - new_score
        print(f'Your score has decreased by {Colors.BOLD}{diff}{Colors.END} points.')
        return diff


def chooseMode(usr_name) -> Type[ValueError] | None:
    """
    Prompts the user to choose the game mode; 1 == single round; >1 means several rounds. If >1, draws set of several
    countries in a unique set, so no country will be repeated.
    VALID PROMPTS ARE NOT CHECKED YET; PLEASE INSERT PROPER PROMPT CHECK.
    :param usr_name: Player's username.
    :return: None (or error if user's prompt is invalid)
    """
    # enter check for proper input
    import time
    avg_t_per_round = 0.0
    rounds = int(input("Enter the amount of rounds you'd like to play: "))
    if rounds == 1:
        country = drawCountry()
        start_time = time.time()  # start countdown of clock
        checkAnswer(usr_name, country=country)
        avg_t_per_round = time.time() - start_time  # stop countdown of clock; add time value to variable.
    elif rounds > 1:
        selected_countries = severalCountries(rounds)
        total_answer_t = 0.0
        for country in selected_countries:
            start_time = time.time()  # start countdown of clock
            checkAnswer(usr_name, country=country)
            round_time = (time.time() - start_time)  # stop countdown of clock; add time value to variable.
            total_answer_t += round_time
        avg_t_per_round = total_answer_t / rounds  # To calc avg, dividing the total answer time by the number of rounds
    else:  # change later to proper value checking
        return ValueError
    updateAvgTimePerRound(usr_name=usr_name, key="Average answer time per round", this_round_avg_t_pr=avg_t_per_round)


def updateAvgTimePerRound(usr_name: str, key: str, this_round_avg_t_pr: float) -> None:
    """
    Updates the Average Time Per Round in the users' dict (all_users.json).
    :param usr_name: User's name to get updated.
    :param key: Key in dict to check; technically it could be the name of the key without the need for this parameter,
    but it may be useful in the future.
    :param this_round_avg_t_pr: The avg time to be updated to the table.
    :return: None
    """
    with open("Resources/all_users.json", "r") as usrs_r_f:
        users = json.load(usrs_r_f)  # this is now a dict
        if key in users.keys():
            current_avg_t_pr = users[usr_name][key]  # check what is the current user's avg time per round
        else:
            current_avg_t_pr = 0
    with open("Resources/all_users.json", "w") as usrs_w_f:
        new_avg_t_pr = (current_avg_t_pr + this_round_avg_t_pr) / 2
        users[usr_name][key] = new_avg_t_pr
        json.dump(users, usrs_w_f, indent=2)


def main() -> None:
    """
    Main function that runs the program.
    :return: None.
    """
    user_name = input("Enter your user name: ")
    initiated_score = getUserData(usr_name=user_name, data="Score")
    checkUser(user_name)  # includes printing the user's score
    chooseMode(user_name)  # chooses number of rounds
    user_score = getUserData(usr_name=user_name, data="Score")
    print("Your updated score is " + Colors.BOLD + str(user_score) + Colors.END + ".")
    leaderboard = CalcLeaderboard()
    user_rank = getUserRank(usr_name=user_name, ldr_brd=leaderboard)
    printUserRank(user_rank)
    changeInScore(old_score=initiated_score, new_score=user_score)
    print("\n------------------------------------\n")
    user_avg_ans_t = getUserData(usr_name=user_name, data="Average answer time per round")
    print(f'Your average answer time per round is {Fore.LIGHTWHITE_EX}{user_avg_ans_t:.3f}{Fore.RESET} seconds.')
    # print(genPodium(leaderboard))


if __name__ == "__main__":
    main()
