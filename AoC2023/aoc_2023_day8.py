import argparse
import re

def part1(input_f) :

    with open(input_f, "r") as day8 :

        # for line in day8 : 
            # print(line)

        lines = day8.read().split("\n")
        instructions = lines[0]
        instructions = instructions.replace("R", "1")
        instructions = instructions.replace("L", "0")

        network = {}

        for line in lines :
            regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
            for node, left, right in re.findall(regex, line):
                network[node] = [left, right]

        print(instructions, network)

        return instructions, network


def do_stuff(instructions, network) :

    counter = 0
    keys_network = list(network)
    curr_node = keys_network[0]
    end_node = keys_network[-1]

    # create iterator
    iterator = iter(instructions)

    print(curr_node, end_node)

    while True : 

        try :
            instruction = next(iterator)
            
        except StopIteration :
            iterator = iter(instructions)

        else :
            if curr_node == end_node :
            
                break

            curr_node = network[curr_node][int(instruction)]
            counter += 1

    print(counter)


#### 

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", help="")
args = parser.parse_args()

input_file = args.input

navigation_instructions, dico_network = part1(input_file)
do_stuff(navigation_instructions, dico_network)
