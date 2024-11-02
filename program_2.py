# Programmer: Mai Lillie
# Date: 11/1/24
# Program #2: Random Number File Writer

# Prompts the user and randomises numbers
def random_number_generator():
    import random
    number_file = open('numbers.txt', 'w')
    iterations = int(input("How many times would you like the program to run? (Up to 1000): "))
    for i in range(0,iterations):
        integer = random.randint(1,500)
        number_file.write(f"{integer}\n")

# Runs the program
if __name__ == '__main__':
    random_number_generator()
