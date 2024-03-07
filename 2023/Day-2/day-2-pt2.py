def clean_line(text, cl):
    return "".join(char for char in text.removeprefix(f'Game {cl + 1}: ') if char not in " ,;")


def data_catalog(text):
    numbers_string = ''
    my_dict = {"red": 1, "green": 2, "blue": 3}
    numbers_integers, colors_list = [], []
    for i in range(len(text)):
        if text[i].isnumeric():
            numbers_string = numbers_string + text[i]
        else:
            numbers_string = numbers_string + ' '
            for key in my_dict:
                if text[i:].startswith(key):
                    colors_list.append(my_dict[key])
    numbers_integers = list(map(int, numbers_string.split()))
    return numbers_integers, colors_list


def power_of_minimum(numbers_list, colors_list):
    red_maximum = 1
    green_maximum = 1
    blue_maximum = 1
    print(f'Number list: {numbers_list}\nColors list: {colors_list}')
    for j in range(len(colors_list)):
        if colors_list[j] == 1:
            if int(numbers_list[j]) > red_maximum:
                red_maximum = int(numbers_list[j])
        elif colors_list[j] == 2:
            if int(numbers_list[j]) > green_maximum:
                green_maximum = int(numbers_list[j])
        else:
            if int(numbers_list[j]) > blue_maximum:
                blue_maximum = int(numbers_list[j])
    return red_maximum * green_maximum * blue_maximum


sum_of_powers = 0
with open('./text.txt') as file:
    for count_line, line in enumerate(file):
        new_line = clean_line(line, count_line)
        print(f'\nLine {count_line + 1}: {new_line}')
        numbers, colors = data_catalog(new_line)
        sum_of_powers += power_of_minimum(numbers, colors)
print(sum_of_powers)
