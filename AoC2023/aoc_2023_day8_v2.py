import argparse
import re
import itertools
import math

def parse_input_part1(input_f) :

    with open(input_f, "r") as day8 :

        lines = day8.read().split("\n")
        instructions = lines[0]
        instructions = instructions.replace("R", "1")
        instructions = instructions.replace("L", "0")

        network = {}

        for line in lines :
            regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
            for node, left, right in re.findall(regex, line):
                network[node] = [left, right]

        print(network)
        return instructions, network


def part1(instructions, network) :

    """_summary_

    Use of the cycle function from itertools to be able to loop on the instruction
    sequence. Eg: if instruction is "RL" but needs more iterations, cycle will
    allow it.

    Returns:
        int: value of the number of iterations to reach the final node.
    """

    counter = 0
    curr_node = "AAA"
    end_node = "ZZZ"

    cycled_instructions = itertools.cycle(instructions)

    for instruction in cycled_instructions :
        if curr_node == end_node :
            break

        curr_node = network[curr_node][int(instruction)]
        counter += 1

    print(counter)
    return counter


def part2(instructions, network) :

    starting_nodes = []
    list_counters = []

    # for node in network :
    #     regex = r'(\d{2}A)'
    #     start_nodes = re.findall(regex, node)
    #     for n in start_nodes :
    #         starting_nodes.append(n)

    starting_nodes = [node for node in network if node[2] == "A"]

    print(starting_nodes)

    cycled_instructions = itertools.cycle(instructions)

    for node in starting_nodes:
        counter = 0
        print(node)
        for instruction in cycled_instructions :

            node = network[node][int(instruction)]
            print(node)
            counter += 1
            if node[2] == "Z" :
                list_counters.append(counter)
                break

    print(list_counters)
    print(math.lcm(*list_counters))

#### 

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", help="")
args = parser.parse_args()

input_file = args.input

navigation_instructions, dico_network = parse_input_part1(input_file)
# nb_iterations = part1(navigation_instructions, dico_network)

# print(f"To go from AAA to ZZZ, we need {nb_iterations} iterations.")

part2(navigation_instructions, dico_network)
