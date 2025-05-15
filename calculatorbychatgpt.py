import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# GUI Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()

# Input field
input_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=equalpress).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=lambda t=text: press(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear).grid(row=5, column=0, columnspan=4, sticky="we")

root.mainloop()
