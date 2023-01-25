def find_palindrome():

    input_string = input("Enter a string: ")

    input_no_whitspace = input_string.replace(" ", "")

    reversed_input = ""

    for char in input_no_whitspace:
        reversed_input = char + reversed_input

    if (reversed_input == input_no_whitspace):
        print("The string is a palindrome.")

    elif (reversed_input != input_no_whitspace):
        print("The string is not a palindrome.")

find_palindrome()