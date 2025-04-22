import argparse


def part1(input_f) :

    with open(input_f, "r") as day5: 

        data = day5.read().strip()
        line = data.split("\n\n")

        seeds = [int(x) for x in line[0].strip().split(":")[1].split()]
        # print(seeds)

        dict_maps = {}

        for maps in line[1:] :
            map_name = maps.split("\n")[0].split()[0]
            dict_maps.setdefault(map_name, [])

            for sublist in maps.split("\n")[1:] :
                value = [int(nb) for nb in sublist.split()]

                dict_maps[map_name].append(value)
    
    # print(dict_maps)

    return seeds, dict_maps


def calculate_smallest_location(seeds, dict_maps) :

    min_location = float('inf')

    for s in seeds:

        for each_map, list_values in dict_maps.items() :

            for destination, source, range_len in list_values :

                if source <= s < source + range_len :

                    s += destination - source
                    break
        
        min_location = min(s, min_location)

    # print(min_location)
    return min_location


def part_2(input_f) :

    list_seeds2check = []

    with open(input_f, "r") as day5:

        data = day5.read().strip()
        line = data.split("\n\n")

        seeds = [int(x) for x in line[0].strip().split(":")[1].split()]
        # print(seeds)

        for i in range(0, len(seeds), 2) :

            # print(i)
            # print(seeds[i], seeds[i+1])
            x = list(range(seeds[i], seeds[i] + seeds[i+1]))
            # print(range(seeds[i], seeds[i+1]))
            list_seeds2check += list(x)

    # print(list_seeds2check)
    print(len(list_seeds2check))
    return list_seeds2check

#### MAIN

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", help="")
args = parser.parse_args()

input_file = args.input

seeds_list, dico_maps = part1(input_file)
calculate_smallest_location(seeds_list, dico_maps)

seed_list_part2 = part_2(input_file)
sol_part2 = calculate_smallest_location(seed_list_part2, dico_maps)


print(f"solution to part 2 is {sol_part2}")
