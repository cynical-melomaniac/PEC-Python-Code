input_string = input("Enter a string with parentheses: ")

class validity_of_parentheses:
    
    def __init__(self, _input_string):

        round_open = 0
        square_open = 0
        curly_open = 0

        for parenthesis in _input_string:
            if parenthesis == '(':
                round_open += 1
            
            elif parenthesis == '[':
                square_open += 1
            
            elif parenthesis == '{':
                curly_open += 1


            elif parenthesis == ')':
                round_open -= 1
            
            elif parenthesis == ']':
                square_open -= 1
            
            elif parenthesis == '}':
                curly_open -= 1


        if round_open == 0 and square_open == 0 and curly_open == 0:
            print("Given string has valid parentheses.")
            
        if round_open != 0 or square_open != 0 or curly_open != 0:
            print("Given string has invalid parentheses.")

validity_of_parentheses(input_string)