import argparse
import math

def read_input(input_f) :

    with open(input_file, "r") as day6 :

        for line in day6 :

            if line.startswith("Time") :
                time = [int(x) for x in line.strip().split(":")[1].split()]
                # print(time)

            elif line.startswith("Distance") :
                distance = [int(x) for x in line.strip().split(":")[1].split()]
                # print(distance)

            else :
                print("error in input")

    return time, distance


def part1(time, distance) :

    print(time, distance)
    list_ways_to_win_all_races = []

    for index, time_race in enumerate(time) :
        ways_to_win = 0
        # print(index, time_race)

        for time_button_hold in range(1, time_race+1) :

            time_left_for_race = time_race-time_button_hold
            distance_travelled = time_button_hold * time_left_for_race
            # print(time_button_hold, time_left_for_race, distance_travelled)
            # print("dist",distance)
            if distance_travelled > distance[index] :
                ways_to_win += 1

        list_ways_to_win_all_races.append(ways_to_win)

    # print(ways_to_win)
    return list_ways_to_win_all_races



#####

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", help="")
args = parser.parse_args()

input_file = args.input

time_races, distance_races = read_input(input_file)
nb_ways_to_win_all_races = part1(time_races, distance_races)

nb_ways_beat_record = math.prod(nb_ways_to_win_all_races)
print(f"There are {nb_ways_beat_record} ways to beat the record.")


time_part2 = [int("".join(str(ele) for ele in time_races))]
distance_part2 = [int("".join(str(ele) for ele in distance_races))]

# print(time_part2, distance_part2)

nb_ways_to_win_part2_race = part1(time_part2, distance_part2)
print(f"There are {nb_ways_to_win_part2_race} ways to win the race in part2.")
