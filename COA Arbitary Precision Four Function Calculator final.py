import tkinter as tk

from customtkinter import *

from decimal import Decimal

from tkinter import messagebox


elements = []  # List to store input elements


def add(x, y):

    return x + y


def subtract(x, y):

    return x - y


def multiply(x, y):

    return x * y


def divide(x, y):

    if y == 0:

        return "Cannot divide by zero"

    return x / y


def power(x, y):

    return x ** y


def factorial(x):

    if x < 0:

        return "Factorial is not defined for negative numbers"

    elif x == 0:

        return 1

    else:

        result = 1

        for i in range(1, x + 1):

            result *= i
        return result




def set_num_elements():
    num_elements = int(entry_num_elements.get())

    for i in range(num_elements):

        label = tk.Label(root, text=f"Element {i + 1}:", bg="black", fg="white", font=("Arial", 16))

        label.pack()

        element_entry = tk.Entry(root, width=30, font=("Arial", 16), bg="grey")

        element_entry.insert(0, "")

        element_entry.pack(pady=5)
        elements.append(element_entry)


    # Remove the input fields for num1 and num2
    entry_num_elements.destroy()
    num_elements_button.destroy()


    # Add a button to perform operations

    calculate_button = tk.Button(root, text="Calculate", bg="grey", fg="black", font=("Arial", 16), width=15, height=3, command=perform_operations)

    calculate_button.pack(pady=10)
    

def clear():

    result_label.config(text='')


def perform_operations():

    user_input = operation_var.get()

    try:

        nums = [Decimal(element.get()) for element in elements]

    except Exception:

        messagebox.showerror("Error", "Invalid input. Please enter valid decimal numbers.")
        return


    if user_input == "add":

        result_label.config(text=sum(nums))

    elif user_input == "subtract":

        result_label.config(text=nums[0] - sum(nums[1:]))

    elif user_input == "multiply":

        result_label.config(text=Decimal(1).multiply(*nums))

    elif user_input == "divide":

        result = nums[0]

        for num in nums[1:]:

            if num == 0:

                messagebox.showerror("Error", "Cannot divide by zero")
                return

            result = result / num

        result_label.config(text=result)

    elif user_input == "power":

        result_label.config(text=nums[0] ** sum(nums[1:]))

    elif user_input == "factorial":

        result_label.config(text=factorial(int(nums[0])))

    elif user_input == "sqrt":

        result_label.config(text=nums[0])

    else:

        messagebox.showerror("Error", "Invalid input. Please enter a valid operation.")


root = tk.Tk()

root.title("Calculator")

root.geometry("400x600")  # Increased height

root.configure(bg="black")


# Title label

title_label = tk.Label(root, text="Arbitary Precision Four Function Calculator", bg="black", fg="white", font=("Arial", 40))

title_label.pack(pady=10)


options_label = tk.Label(root, text="Enter the number of elements:", bg="black", fg="white", font=("Arial", 30))

options_label.pack(pady=10)


entry_num_elements = tk.Entry(root, width=30, font=("Arial", 16), bg="Grey")

entry_num_elements.insert(0, "")

entry_num_elements.pack(pady=10)


num_elements_button = tk.Button(root, text="Submit Elements", bg="Grey", fg="Black", font=("Georgia", 16), width=15, height=3, command=set_num_elements)

num_elements_button.pack(pady=10)


# Variable to store the selected operation

operation_var = tk.StringVar()

operation_var.set("add")


# Radio buttons for selecting the operation

radio_buttons_frame = tk.Frame(root, bg="black")

radio_buttons_frame.pack(pady=10)


buttons = ["add", "subtract", "multiply", "divide", "power", "factorial", "sqrt"]


for operation in buttons:

    radio_button = tk.Radiobutton(radio_buttons_frame, text=operation.capitalize(), variable=operation_var, value=operation, bg="black", fg="white", font=("Arial", 14))

    radio_button.pack(side=tk.LEFT, padx=10)


Option_label= tk.Label(root, text="Clear The Elements", bg="black", fg="white", font=("Arial", 20))

Option_label.pack(pady=10)


result_label = tk.Label(root, text="", bg="black", fg="white", font=("Arial", 16))

result_label.pack(pady=10)


clear_button = tk.Button(root, text="Clear", bg='Grey', fg="Black", font=("Georgia", 16), width=12, height=3,command=clear)

clear_button.pack(pady=10)





root.mainloop()

