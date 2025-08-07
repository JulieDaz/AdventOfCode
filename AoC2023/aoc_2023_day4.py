import argparse


def part1(input_f):

    with open(input_f, "r") as day4 :

        score_all_games = 0

        for line in day4 :

            first = True
            score = 0

            myline = line.strip().split(":")

            winning_game = [int(x) for x in myline[1].split("|")[0].split()]
            mygame = [int(x) for x in myline[1].split("|")[1].split()]

            for win_nb in winning_game :
                if win_nb in mygame :

                    if first is True :
                        score += 1
                        first = False
                    else :
                        score *= 2

            score_all_games += score
            # print(score)

    print(score_all_games)


def part2(input_f) :

    dict_winning_games = {}
    dict_nb_copies_per_game = {}

    with open(input_f, "r") as day4 :

        for line in day4 :

            nb_win_game = 0

            myline = line.strip().split(":")
            card_name = int(myline[0].split()[1])

            winning_game = [int(x) for x in myline[1].split("|")[0].split()]
            mygame = [int(x) for x in myline[1].split("|")[1].split()]

            dict_winning_games.setdefault(card_name, 0)
            dict_nb_copies_per_game.setdefault(card_name, 1)

            for win_nb in winning_game :
                if win_nb in mygame :
                    
                    nb_win_game += 1

                    dict_winning_games[card_name] += 1

    print(dict_winning_games)
    # print(dict_nb_copies_per_game)

    for game_id, games_won in dict_winning_games.items() :

        nb_copies = dict_nb_copies_per_game[game_id]
        print(f"game ident {game_id} has {nb_copies} copies and it has {games_won} winning nb")

        # create a loop to increment subsequent cards
        for i in range(1, games_won + 1) :
            # add copies to the subsequent cards
            dict_nb_copies_per_game[game_id+i] += nb_copies
            print(f"We now have {dict_nb_copies_per_game[game_id+i]} copies of game {game_id+i}")

    # print(dict_nb_copies_per_game)
    total = sum(dict_nb_copies_per_game.values())
    print(total)


####

parser = argparse.ArgumentParser(description="Advent of Code day 4 solution.")
parser.add_argument("--input", help="input file for the 4th day of AoC.")
args = parser.parse_args()


input_file = args.input
part1(input_file)
part2(input_file)