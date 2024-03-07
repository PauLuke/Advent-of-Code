from numpy import zeros

symbols = ['@', '#', '$', '%', '&', '*', '-', '=', '+', '/']
numbers = list(range(1, 9))
 

with open('text.txt') as file:
    for count_line, line in file:
        for i in range(len(line)):
            if line[i] in symbols:
                
                
