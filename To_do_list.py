import tkinter as tk

root=tk.Tk()
root.geometry("800x400")
root.title("TO-DO List")

def add_command():
    task=ent.get()
    lstbox.insert(tk.END,task)
    ent.delete(0,tk.END)

def mark_command():
    pos=lstbox.curselection()[0]
    task=lstbox.get(pos)
    lstbox.delete(pos)
    lstbox.insert(tk.END,f"{task}   \u2713")


def delete_command():
    pos=lstbox.curselection()[0]
    lstbox.delete(pos)

def update_command():
    pos=lstbox.curselection()[0]
    task = lstbox.get(pos)

    ent.delete(0, tk.END)
    ent.insert(0, task)

    lstbox.delete(pos)

lb1=tk.Label(root,text="Enter the Task", font=('calibri',14))
lb1.place(x=10, y=45)

ent=tk.Entry(root,width=80)
ent.place(x=150, y=50)

lstbox=tk.Listbox(root,width=80, height=15)
lstbox.place(x=150,y=80)

btn1=tk.Button(root, text="ADD", command=add_command)
btn1.place(x=160, y=350)

btn2=tk.Button(root, text="UPDATE", command=update_command)
btn2.place(x=280, y=350)

btn3=tk.Button(root, text="MARK", command=mark_command)
btn3.place(x=440, y=350)

btn4=tk.Button(root, text="REMOVE", command=delete_command)
btn4.place(x=580, y=350)


root.mainloop()