try:
    numerator = int(input("Enter the number to divide: "))
    denominator = int(input("Enter the number to divide by: "))
    result = (numerator)/(denominator)
    print(result)
except ZeroDivisionError:
    print("You can't devide by zero!!")
except ValueError:
    print("You must enter number")