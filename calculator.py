print ("\nBasic Calculator Program : ")

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b


control = True
while control:
    
    first_number = input("\nFirst Number : ")    
    if '.' in first_number:
        first_number = float(first_number)
    else:
        first_number = int(first_number)

    second_number = input("Second Number : ")

    if '.' in second_number:
        second_number = float(second_number)
    else:
        second_number = int (second_number)
    
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Quit the program\n")
    choice = int (input("Enter your choice: "))
    
    #Cases
    if choice==1:
        print(addition(first_number,second_number))
        print("\n")
    if choice==2:
        print(subtraction(first_number,second_number))
        print("\n")
    if choice==3:
        print(multiplication(first_number,second_number))
        print("\n")
    if choice==4:
        print(division(first_number,second_number))
        print("\n")
    if choice==5:
        print(modulus(first_number,second_number))
        print("\n")
    if choice==6:
        control = False
        print("Quiting the program")
