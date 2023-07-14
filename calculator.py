
first_number  = int(input("enter first number: "))
second_number = int(input("enter second number: "))
operator = input("enter the operator: ")

if operator == "+":
    answer=first_number + second_number
    print(f"{answer}")

elif operator == "-":
    answer=first_number - second_number
    print(f"{answer}")        

elif operator == "*":
    answer=first_number * second_number
    print(f"{answer}")            

elif operator == "/":
    answer=first_number / second_number
    print(f"{answer}")  



