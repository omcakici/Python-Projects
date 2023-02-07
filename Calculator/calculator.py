from art import logo
from replit import clear

def add(n1, n2):
  return n1 + n2

def divide(n1, n2):
  return n1 / n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

print(logo)

first_number = 0
start_zero = True
is_calculation_continues = True

while is_calculation_continues:
  if start_zero:
    first_number = float(input("What's the first number?: "))
  for key in operations: 
    print(key)
  operation = input("Pick an operation above: ")
  next_number = float(input("What's the next number?: "))
  result = operations[operation](first_number, next_number)
  
  print(f"{first_number} {operation} {next_number} = {result}")
  continue_calc = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start new calculation: ")
  if continue_calc == 'y':
    start_zero = False
    first_number = result
    is_calculation_continues = True
  else:
    print('You have type wrong input, please try again from the beginning')
    is_calculation_continues = False
    clear()
