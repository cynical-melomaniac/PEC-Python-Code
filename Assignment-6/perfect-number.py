def perfect_number():

    input_value = int(input("Enter the value: "))
    divisor = 1
    sum_value = 0

    while(divisor < input_value):
        if(input_value % divisor == 0):
            sum_value = sum_value + divisor
        divisor = divisor + 1

    if (sum_value == input_value):
        print(input_value, "is a Perfect Number")
    else:
        print(input_value, "is not the Perfect Number")

perfect_number()