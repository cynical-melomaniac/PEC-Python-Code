from math import factorial

def pascal_triangle():
    n = int(input("Enter the number of rows:"))
 
    for a in range(n):
        for b in range(n-a+1):
            print(end=" ")
 
        for b in range(a+1):
            print(factorial(a)//(factorial(b)*factorial(a-b)), end=" ")

        print()


pascal_triangle()