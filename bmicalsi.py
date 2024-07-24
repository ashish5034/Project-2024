import tkinter as tk  # Import the Tkinter library for GUI creation
from tkinter import messagebox  # Import the messagebox module for displaying error messages

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())  # Get the weight entered by the user and convert it to a float
        height = float(height_entry.get())  # Get the height entered by the user and convert it to a float
        bmi = weight / (height ** 2)  # Calculate BMI using weight and height
        category = classify_bmi(bmi)  # Classify BMI into categories
        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")  # Display the BMI and category
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")  # Show error if invalid input

# Function to classify BMI into categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# # Function to save user data to a text file
# def save_data(weight, height, bmi, category):
#     with open("user_data.txt", "a") as file:
#         file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}, Category: {category}\n")

# Create the main window
root = tk.Tk() # Create a Tkinter root window
root.title("BMI Calculator")  # Set the title of the window

# Create labels and entries for weight and height
weight_label = tk.Label(root, text="Weight (kg):")  # Create a label for weight
weight_label.grid(row=0, column=0, padx=50, pady=15)  # Place the weight label in the grid layout

weight_entry = tk.Entry(root)  # Create an entry field for weight
weight_entry.grid(row=0, column=1, padx=50, pady=15)  # Place the weight entry field in the grid layout

height_label = tk.Label(root, text="Height (m):")  # Create a label for height
height_label.grid(row=1, column=0, padx=50, pady=15)  # Place the height label in the grid layout

height_entry = tk.Entry(root)  # Create an entry field for height
height_entry.grid(row=1, column=1, padx=50, pady=15)  # Place the height entry field in the grid layout

# # Create a label to display the result
result_label = tk.Label(root, text=" ")  # Create an empty label
result_label.grid(row=2, columnspan=2, padx=50, pady=15)  # Place the result label in the grid layout

# # Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)  # Create a button with text "Calculate" and bind it to the calculate_bmi function
calculate_button.grid(row=3, columnspan=2, padx=50, pady=15)  # Place the calculate button in the grid layout

# Run the main event loop
root.mainloop()  # Start the Tkinter event loop to display the GUI and handle user interactions
