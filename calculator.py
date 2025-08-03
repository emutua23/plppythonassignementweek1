# Basic Calculator Program

def calculator():
    print("=== Basic Calculator ===")
    print("Available operations: +, -, *, /")
    print()
    
    try:
        # Get first number
        num1 = float(input("Enter the first number: "))
        
        # Get second number
        num2 = float(input("Enter the second number: "))
        
        # Get operation
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
            
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()