input_string = input("Enter a string with parentheses: ")

class validity_of_parentheses:

    def __init__(self, _input_string = str()):
        
        parentheses_list = ['(', '{', '[', ']', '}', ')']
        parentheses_set_list = ['()', '{}', '[]']
        
        for char in _input_string:
            if char not in parentheses_list:
                _input_string = _input_string.replace(char, '')

        while any(parenthesis_set in _input_string for parenthesis_set in parentheses_set_list):
            for parenthesis_set in parentheses_set_list:
                _input_string = _input_string.replace(parenthesis_set, "", -1)

        print("Given parentheses are valid." if _input_string == "" else "Given parentheses are invalid.")

validity_of_parentheses(input_string)