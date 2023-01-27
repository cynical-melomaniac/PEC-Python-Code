def find_panagram():

    input_string = input("Enter a string: ")

    input_no_whitspace = input_string.replace(" ", "")

    input_no_whitspace = input_no_whitspace.upper()

    char_comparison_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    count = 0

    for char in input_no_whitspace:
        for char_comparison in char_comparison_list:
            if char == char_comparison:
                char_comparison_list = char_comparison_list.replace(char_comparison, "")

    if (char_comparison_list == ""):
        print("The string entered is a panagram.")
    else:
        print("The string entered is not a panagram.")

find_panagram()