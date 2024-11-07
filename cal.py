print("Calculator project : ")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")

operation = int(input("Select any operation of calculator : "))

if operation == 1:
    first_number = int(input("Enter the number :"))
    second_number = int(input("Enter the number :"))
    summation = first_number + second_number
    print("Summation :", int(summation))

elif operation == 2:
    first_number = int(input("Enter the number :"))
    second_number = int(input("Enter the number :"))
    subtraction = first_number - second_number
    print("Summation : ", subtraction)

elif operation == 3:
    first_number = int(input("Enter the number :"))
    second_number = int(input("Enter the number :"))
    multiplication = first_number*second_number
    print("Summation :", int(multiplication))

elif operation == 4:
    first_number = int(input("Enter the number :"))
    second_number = int(input("Enter the number :"))
    division=first_number / second_number
    print("Summation :", float(division))

else :
    print("Invalid")