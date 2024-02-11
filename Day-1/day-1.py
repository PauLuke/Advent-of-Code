def part1(string):
    digits = []
    for i in range(len(string)):
        if string[i].isdigit():
            digits.append(string[i])
    return int(digits[0] + digits[-1])


def part2(string):
    my_dict = {"one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    digits = []
    for i in range(len(string)):
        if string[i].isdigit():
            digits.append(string[i])
        else:
            for key in my_dict.keys():
                if string[i:].startswith(key):
                    digits.append(my_dict[key])
    return int(digits[0] + digits[-1])


values_sum = 0
with open('./text.txt') as file:
    for line in file:
        values_sum += part1(line)

print(f'Sum = {values_sum}')
