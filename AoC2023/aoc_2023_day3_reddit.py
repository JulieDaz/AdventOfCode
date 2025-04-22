import re
# from operator import mul

# with open('inputs/input_03.txt', 'r') as f:
with open('inputs/input_03_dummy.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):

    lines = puzzle_input.split('\n')

    symbol_regex = r'[^.\d]'
    symbol_adjacent = set()
    for row, line in enumerate(lines):
        print(row)
        for m in re.finditer(symbol_regex, line):
            print(m)
            j = m.start()
            print(j)
            symbol_adjacent |= {(r, c) for r in range(row-1, row+2) for c in range(j-1, j+2)}
    print(symbol_adjacent)

    number_regex = r'\d+'
    part_num_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            if any((i, j) in symbol_adjacent for j in range(*m.span())):
                part_num_sum += int(m.group())

    return part_num_sum

print('Part 1:', part1(puzzle_input))
