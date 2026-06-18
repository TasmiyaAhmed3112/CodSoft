import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation

    try:
        password_length=int(entry.get()) 
        if password_length<=4:
            result.set("Enter value greater than 4")
            return
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        print("Your password is:\t")
        password= "".join(random.sample(s,password_length))
        result.set(password)

    except (ValueError):
        result.set("Invalid input")

def copy_password():
    password=result.get()

    if password and password not in ['Invalid input','Enter value greater than 4']:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo('Copied','Password Copied Successfully!')
    else:
        messagebox.showinfo('Try again', 'No password to copy!')



root=tk.Tk()
root.title("Pass-word Generator!!")
root.geometry("500x400")

label = tk.Label(root, text="Password Generator", font=("Arial", 18))
label.pack(pady=10)

label = tk.Label(root, text="Enter the length of the password", font=("Arial", 12))
label.pack(pady=8)



entry = tk.Entry(root)
entry.pack(pady=10)

btn = tk.Button(root, text="Generate Password", command=generate_password)
btn.pack(pady=10)

result = tk.StringVar()
output = tk.Label(root, textvariable=result, font=("Arial", 14))
output.pack(pady=20)

btn = tk.Button(root, text="Copy Password", command=copy_password)
btn.pack(pady=10)

root.mainloop()


