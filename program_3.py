# Programmer: Mai Lillie
# Date: 11/1/24
# Program #3: Average Numbers

# Program to add up all the numbers from a file
def sum_numbers_from_file():
    total = 0
    try:
        numbers_file = open('numbers.txt', 'r')
        number = (numbers_file.readline())
        number.rstrip('\n')
        number = int(number)
        while number != "":
            total += number
            number = numbers_file.readline()
            number.rstrip('\n')
            number = int(number)
        numbers_file.close()
    except IOError:
        print("An error occurred trying to read your file.")
    except ValueError:
        if number != "":
            print("Your document contains invalid characters.")
    finally:
        print(f'In the sum_numbers_from_file function, there is a total of {total} numbers.')

# Runs the program
if __name__ == '__main__':
    sum_numbers_from_file()
