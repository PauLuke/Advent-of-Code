def text_to_number(string):
    list_num = []
    list_pos = []
    found = False
    for key in my_dict:
        if string.find(key) != -1:
            list_num.append(key)
            list_pos.append(string.find(key))
            if string.count(key) > 0:
                for i in range(string.count(key) - 1):
                    list_num.append(key)
                    list_pos.append(string.find(key, list_pos[-1] + 1))
            found = True
    if found:
        test = list_pos[0]
        index_min = 0
        for i in range(len(list_pos)):
            if list_pos[i] <= test:
                index_min = i
                test = list_pos[i]
        minima = list_num[index_min]
        string = string.replace(minima, my_dict[minima], 1)
    else:
        return string

    list_num = []
    list_pos = []
    found = False
    for key in my_dict:
        if string.find(key) != -1:
            list_num.append(key)
            list_pos.append(string.find(key))
            if string.count(key) > 0:
                for i in range(string.count(key) - 1):
                    list_num.append(key)
                    list_pos.append(string.find(key, list_pos[-1] + 1))
            found = True
    if found:
        test = list_pos[0]
        index_max = 0
        for i in range(len(list_pos)):
            if list_pos[i] >= test:
                index_max = i
                test = list_pos[i]
        maxima = list_num[index_max]
        string = string.replace(maxima, my_dict[maxima], 1)
    return string


def get_first(string):
    for i in range(len(string)):
        if string[i].isnumeric():
            return string[i]


def get_last(string):
    for j in range(len(string) - 1, -1, -1):
        if string[j].isnumeric():
            return string[j]


my_dict = {"one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
values_sum = 0
count = 1
with open('./text.txt') as file:
    for line in file:
        new_line = text_to_number(line)
        first = get_first(new_line)
        last = get_last(new_line)
        values_sum += int(first + last)
        print(f'{count}. First = {first}, Last = {last}, Number = {int(first + last)}, Sum = {values_sum}')
        count += 1
