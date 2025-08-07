#-*- coding: utf-8 -*-

import argparse
import math
import re


def read_data(input_f) :

    """Reads the input file.

    Args:
        input_f (str): path of the input file

    Returns:
        list: List of game ids
    """

    dict_conditions = {
        "red" : 12,
        "green" : 13,
        "blue" : 14
    }

    list_game_id = []

    with open(input_f, "r") as game_file :

        for line in game_file :
            game_is_good = True

            myline = line.strip().split(":")
            game_id = myline[0]
            game_res = myline[1]

            for colour, value in dict_conditions.items() :

                pattern = f"[0-9]+ {colour}"
                match = re.findall(pattern, game_res)
                print(match)

                for ele in match :
                    nb, col = ele.split(" ")

                    if int(nb) > value :
                        game_is_good = False
                        break

                if game_is_good is False :
                    break

            if game_is_good is True :
                list_game_id.append(game_id)

    return list_game_id


def calculate_sum(list_game_id) :

    total = sum([int(x.split(" ")[1]) for x in list_game_id])

    print(total)


def pb2(input_f) :

    """Read data and solve the second problem of the day.

    Args:
        input_f (str): path of the input file

    """

    # list_game_id = []

    # list_colour = ["red", "blue", "green"]
    list_val = []

    with open(input_f, "r") as game_file :

        for line in game_file :

            dict_colour = {
                "red" : [],
                "blue" : [],
                "green" : []
            }
            myline = line.strip().split(":")
            game_res = myline[1]

            # will contain the biggest number of cubes for 1 colour
            list_cube_1game = []

            for colour, value in dict_colour.items() :

                pattern = f"[0-9]+ {colour}"
                match = re.findall(pattern, game_res)

                for ele in match :
                    nb, col = ele.split(" ")
                    value.append(int(nb))

            print(dict_colour)
            for cubes in dict_colour.values() :
                # if list not empty
                if cubes :
                    nb_cube_required = max(cubes)
                    list_cube_1game.append(nb_cube_required)

            product_val = math.prod(list_cube_1game)
            list_val.append(product_val)
    print(list_val)
    print(sum(list_val))


### MAIN

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", help="")
args = parser.parse_args()

input_file = args.input
# game_id_list = read_data(input_file)
# calculate_sum(game_id_list)

pb2(input_file)
