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


def is_valid(numbers_list, colors_list):
    print(f'Number list: {numbers_list}\nColors list: {colors_list}')
    for j in range(len(colors_list)):
        if colors_list[j] == 1:
            if int(numbers_list[j]) > 12:
                return False
        elif colors_list[j] == 2:
            if int(numbers_list[j]) > 13:
                return False
        else:
            if int(numbers_list[j]) > 14:
                return False
    return True


sum_of_valids = 0

with open('./text.txt') as file:
    for count_line, line in enumerate(file):
        new_line = clean_line(line, count_line)
        print(f'\nLine {count_line + 1}: {new_line}')
        numbers, colors = data_catalog(new_line)
        if is_valid(numbers, colors):
            sum_of_valids += count_line + 1
            print(f'Valid line: {count_line + 1}')
print(f'\n The sum of the valid lines is: {sum_of_valids}')
