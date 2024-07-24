import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
    
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"
        
        label_result.config(text="Result: " + str(result))
        
    except ValueError:
        print("Enter Input in first grid and second grid: ")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Create operation selection
label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0)

operation_var = tk.StringVar(root)
operation_var.set("+")

operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1)

# Create calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2)

# Create result label
label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
