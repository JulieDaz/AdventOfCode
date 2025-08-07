with open('inputs/input_day9_dummy.txt', 'r') as f:
    puzzle_input = f.read().strip()


def part1(puzzle_input):
    total = 0
    for line in puzzle_input.split('\n'):
        nums = [int(n) for n in line.split()]
        final_nums = []

        print("start", nums)
        while set(nums) != set([0]):
            print("while", nums)
            print("final", final_nums)
            final_nums.append(nums[-1])
            nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]
            print("final2", final_nums)
            print("while2", nums)

        print(final_nums)
        total += sum(final_nums)

    return total

print('Part 1:', part1(puzzle_input))
