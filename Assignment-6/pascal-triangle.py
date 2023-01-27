from math import factorial

def pascal_triangle():
    rows = int(input("Enter the number of rows:"))
 
    for row in range(rows):
        for num in range(rows-row+1):
            print(end=" ")
 
        for num in range(row+1):
            print(factorial(row) // (factorial(num) * factorial(row-num)), end=" ")

        print()


pascal_triangle()