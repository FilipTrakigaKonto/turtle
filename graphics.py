import tkinter as tk

def calculate():
    result = int(entry1.get()) + int(entry2.get())
    result_label.config(text=f"Result: {result}")
def minus():
    result = int(entry1.get()) - int(entry2.get())
    result_label.config(text=f"Result: {result}")

root = tk.Tk()

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Add", command=calculate)
button.pack()

button2 = tk.Button(root, text="Subtract", command=minus)
button2.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

#still don't understand how to use it for my calc but it works atleast
