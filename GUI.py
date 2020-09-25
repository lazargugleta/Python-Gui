# python3 version of tkinter
import tkinter

# window serves as a main entry into GUI
# that is the windows, where elements are added
window = tkinter.Tk()

# add title to your window
window.title("Python GUI")

# set specific size of the window
window.geometry("450x250")

# Elements
# Label
label = tkinter.Label(window, text="Some label text",width = 50)
label.pack()

# Button
def clicked():
  label = tkinter.Label(window, text="Button label",width = 50)
  label.pack()

butt = tkinter.Button(window, text="Click button!", command=clicked,width = 10)
butt.pack()

# Entry
entry = tkinter.Entry(window, width=10)
entry.pack()

# Text
text = tkinter.Text(window, width=20, height=5)
text.insert(tkinter.INSERT, "Hello")
text.insert(tkinter.END, "World")
text.pack()

# call mainloop and execute all command for that GUI
window.mainloop()



