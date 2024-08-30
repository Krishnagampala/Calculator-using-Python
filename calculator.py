# Calculator operations
def addition(a, b):
    return a + b  

def subtraction(a, b):
   return a - b

def multiplication(a, b):
   return a * b

def division(a, b):
    if b == 0:
        print("Cannot divide by 0!")
        return None
    return a / b

# Operation functions dict  
operations = {
    1: addition,
    2: subtraction, 
    3: multiplication,
    4: division 
}

def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
  
    choice = input_number("Enter choice(1-4): ")

    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")

    func = operations.get(choice)
    if func:
        result = func(num1, num2)
        if result is not None:
            print(result) 
    else:
        print("Invalid operation")
   
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
               
calculate()
