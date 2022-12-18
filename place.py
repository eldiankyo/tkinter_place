import tkinter as tk

root = tk.Tk()
root.title('Place Geometry Manager')
root.resizable(1, 1)
root.geometry('800x600')
root.config(bg='#d9d9d9')

label1 = tk.Label(root, text='Absolute placement', bg='red', fg='white')
label1.place(x=20, y=10)

label2 = tk.Label(root, text='Relative placement', bg='blue', fg='white')
label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')

root.mainloop()