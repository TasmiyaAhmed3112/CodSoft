import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('500x600')
root.title('Contact Book')

def add_contacts():
    name=name_ent.get()
    contact=contact_ent.get()
    email=email_ent.get()
    address=address_ent.get()

    tree.insert(
        "",
        "end",
        values=( name, contact, email, address)
    )

    name_ent.delete(0,tk.END)
    email_ent.delete(0,tk.END)
    contact_ent.delete(0,tk.END)
    address_ent.delete(0,tk.END)

def update_contact():
    selected = tree.selection()[0]

    values = tree.item(selected, "values")

    
    name_ent.delete(0, tk.END)
    name_ent.insert(0, values[0])

    contact_ent.delete(0, tk.END)
    contact_ent.insert(0, values[1])

    email_ent.delete(0, tk.END)
    email_ent.insert(0, values[2])

    address_ent.delete(0, tk.END)
    address_ent.insert(0, values[3])

    
    tree.delete(selected)

def delete_contact():
    selected = tree.selection()[0]

    
    tree.delete(selected)



def search_contact():
    name = search_ent.get().lower()

    for item in tree.get_children():
        values = tree.item(item)["values"]

        if name in values[0].lower():
            tree.selection_set(item)
            tree.focus(item)
        else:
            tree.selection_remove(item)



label_info=tk.Label(root,text='Enter contact details')
label_info.place(x=10,y=10)

lb1=tk.Label(root,text='Name:')
lb1.place(x=10,y=45)
name_ent=tk.Entry(width=45)
name_ent.place(x=90,y=51)

lb2=tk.Label(root,text='Contact:')
lb2.place(x=10,y=70)
contact_ent=tk.Entry(width=45)
contact_ent.place(x=90,y=71)

lb3=tk.Label(root,text='Email:')
lb3.place(x=10,y=95)
email_ent=tk.Entry(width=45)
email_ent.place(x=90,y=91)

lb3=tk.Label(root,text='address:')
lb3.place(x=10,y=120)
address_ent=tk.Entry(width=45)
address_ent.place(x=90,y=111)

btn_add=tk.Button(root,text='ADD',command=add_contacts)
btn_add.place(x=20,y=155)

btn_update=tk.Button(root,text='UPDATE', command=update_contact)
btn_update.place(x=90,y=155)

btn_delete=tk.Button(root,text='DELETE', command=delete_contact)
btn_delete.place(x=170,y=155)

label_search=tk.Label(root,text='Search contact')
label_search.place(x=10,y=200)

search_ent=tk.Entry(width=45)
search_ent.place(x=10,y=230)

btn_search=tk.Button(root,text='SEACH', command=search_contact)
btn_search.place(x=315,y=222)


tree_frame = tk.Frame(root)
tree_frame.place(x=10, y=315, width=470, height=250)



columns = ("Name", "Contact", "Email", "Address")

tree = ttk.Treeview(
    tree_frame,
    columns=columns,
    show="headings",
    height=10
)



for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=90)


tree.pack(fill="both", expand=True)

root.mainloop()