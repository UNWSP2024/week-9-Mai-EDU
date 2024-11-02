# Programmer: Mai Lillie
# Date: 11/1/24
# Program #1: Item Counter

def count_file_lines():
    name_file = open('names.txt', 'r')
    counter = 0
    name = name_file.readline()
    while name != "":
        counter += 1
        name = name_file.readline()
    name_file.close()
    print(f"There are {counter} items in this file.")

if __name__ == '__main__':
    count_file_lines()
