import tkinter as tk

# main window of our calculator
window = tk.Tk()
window.title("Calculator App")
window.geometry("300x250")

# add function for the addition of two numbers
def add():
  res_box.delete(1.0,"end")
  try:
    res_box.insert(tk.INSERT, int(first_nr.get()) + int(second_nr.get()))
  except ValueError:
    res_box.insert(tk.INSERT, "Number required")

# sub function for subtracking two numbers
def sub():
  res_box.delete(1.0,"end")
  try:
    res_box.insert(tk.INSERT, int(first_nr.get()) - int(second_nr.get()))
  except ValueError:
    res_box.insert(tk.INSERT, "Number required!")

# all elements inside the window
lbl_nr_one = tk.Label(window, text="Enter the first number:", bg="green")
lbl_nr_one.pack(padx=5, pady=5)

first_nr = tk.Entry(window, width=10)
first_nr.pack(padx=5, pady=5)

lbl_nr_two = tk.Label(window, text="Enter the second number:", bg="red")
lbl_nr_two.pack(padx=10, pady=5)

second_nr = tk.Entry(window, width=10)
second_nr.pack(padx=10, pady=5)

button_add = tk.Button(window, text="Add numbers!", command=add)
button_add.pack()

button_sub = tk.Button(window, text="Subtract numbers!", command=sub)
button_sub.pack()

lbl_res = tk.Label(window, text="Result is:")
lbl_res.pack(padx=10, pady=5)

res_box = tk.Text(window, width=15, height=1)
res_box.pack(padx=10, pady=5)

window.mainloop()