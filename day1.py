from aoc_help import *
lines = read_file('data/input-day1.txt')
data = [int(x) for x in lines]

# part 1
count = 0
for i in range(1, len(data)):
    count += data[i] > data[i-1]

print(f"Part 1: {count}")

# part 2
count = 0
for i in range(1, len(data)-2):
    sum1 = sum(data[(i-1):(i+2)])
    sum2 = sum(data[i:(i+3)])
    count += sum2 > sum1

print(f"Part 2: {count}")