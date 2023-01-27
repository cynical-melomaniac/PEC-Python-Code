def alphabetical_sorter():

    input_string = input("Enter a string: ")
    input_list = input_string.split("-")

    sorted_list = sorted(input_list)

    print(sorted_list)

    output = ""

    for item in sorted_list:
        if output != "":
            output = output + "-" + item
        if output == "":
            output = output + item

    print("Sorted string: ", output)

alphabetical_sorter()