import argparse
import math
import re

def read_data(input_f) :

    with open(input_f, "r") as data :

        puzzle = data.read()

    return puzzle

def part1(puzzle) :

    engine_parts = puzzle.split("\n")

    regex_symbol = r"[^\d.]"
    regex_num = r"\d+"

    coord_symbol_set = set()

    for row, line in enumerate(engine_parts) :

        symbol = re.finditer(regex_symbol, line.strip())
        for ele in symbol :
            pos = int(ele.start())

            ## then we look for the coordinates around the symbol 
            ## that represent the position where a number can be to be
            ## considered adjacent

            coord_symbol_set |= {(i, j) for i in range(row-1, row+2) for j in range(pos-1, pos+2)}

    sum_value = 0

    for row, line in enumerate(engine_parts) :
        number = re.finditer(regex_num, line.strip())

        for ele in number:

            if any((row, col) in coord_symbol_set for col in range(*ele.span())) :

                sum_value += int(ele.group())

    # print(sum_value)
    return sum_value


def part2(puzzle) :

    engine_parts = puzzle.split("\n")

    dict_check_match = {}
    
    regex_symbol = r"[*]"

    for row, line in enumerate(engine_parts) :

        star = re.finditer(regex_symbol, line.strip())
        for ele in star :
            pos = int(ele.start())

            # keep the coordinates of the * symbol and add them in the dict
            dict_check_match[row, pos] = []

    regex_num = r"\d+"

    for row, line in enumerate(engine_parts) :
        number = re.finditer(regex_num, line.strip())

        for nb in number:
            nb_value = int(nb.group())

            for i in range(row-1, row+2) :
                for j in range(nb.span()[0]-1, nb.span()[1]+1) :

                    if (i,j) in dict_check_match :
                        dict_check_match[i, j].append(nb_value)
    
    print(dict_check_match)

    sum_gear_ratios = 0

    for key, value in dict_check_match.items() : 

        # we look for the symbol that have exactly 2 numbers adjacent
        # so we look for 2 elements in the list
        if len(value) == 2 :

            product = math.prod(value)
            sum_gear_ratios += product

    print(sum_gear_ratios)


##### MAIN
parser = argparse.ArgumentParser(description="coucou")
parser.add_argument("--input", help="")
args = parser.parse_args()

input_file = args.input
puzzle_data = read_data(input_file)
part1(puzzle_data)
part2(puzzle_data)