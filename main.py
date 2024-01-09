import characters
import random


def parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


# This function generates a random number, changes the array to an unordered set, changes again to a list
# and returns the random index of the array.


def random_character(char_array):
    rand_num = random.randint(0, len(char_array))
    set_array = set(char_array)
    list_array = list(set_array)
    return list_array[rand_num]


def validate_int_input():  # This function validates if the user input is a string.
    while True:
        num_input = input('Enter password length: ')
        parsed_int = parse_int(num_input)

        if parsed_int is None:
            print('Invalid Input!')
        else:
            return parsed_int


# This function takes the user length as range and returns a random character in every iteration,
# appending them to an empty array. After that, the array is concatenated as the new password
# and printed on screen.

def generate_password(array, length):
    new_array = []

    for i in range(0, length):
        rand_char = random_character(array)
        new_array.append(rand_char)

    password_str = ''.join(new_array)
    print('Your new password is:')
    print(password_str)


def main():
    user_num = validate_int_input()
    generate_password(characters.characters, user_num)


if __name__ == '__main__':
    main()

