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


            elif round_open > 1 and parenthesis == ')':
                round_open -= 1
            
            elif square_open > 1 and parenthesis == ']':
                square_open -= 1
            
            elif curly_open > 1 and parenthesis == '}':
                curly_open -= 1


            if round_open == 0 and square_open == 0 and curly_open == 0:
                print("Given string has valid parentheses.")
                break
            
            if round_open != 0 or square_open != 0 or curly_open != 0:
                print("Given string has invalid parentheses.")
                break

validity_of_parentheses(input_string)