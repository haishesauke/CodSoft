import tkinter as tk
from tkinter import messagebox
contacts = []       # contacts are stored here


# functoion to add new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"Name" : name, "Phone" : phone, "Email" : email, "Address" : address})
        clear_fields()
        update_contact_list()
    else:
        messagebox.showwarning("Error", "Name and Phone number are requires fields!")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def search_contact():
    search_query = search_entry.get().lower()
    search_results = []
    for contact in contacts:
        if search_query in contact['Name'].lower() or search_query in contact['Phone']:
            search_results.append(f"{contact['Name']} - {contact['Phone']}")

    for result in search_results:
        contact_list.insert(tk.END, result)

# function for veiwing contacts
def veiw_contact():
    select_contact = contact_list.curselection()
    if select_contact:
        index = select_contact[0]
        contact = contacts[index]
        details_text.config(text=f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
    else:
        details_text.config(text="")

#function for updating contact 
def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        
        if name and phone:
            contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            clear_fields()
            update_contact_list()
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")
    else:
        messagebox.showwarning("Error", "Select a contact to update.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Error", "Select a contact to delete.")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    

# creating main fram
root = tk.Tk()
root.title("Contacts")

# Name Label
name_label = tk.Label(root, text= "Name :")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Phone number Label
phone_label = tk.Label(root, text= "Phone Number :")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

# E-mail Add Label
email_label = tk.Label(root, text= "E-mal Address :")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# House Address Label
address_label = tk.Label(root, text= "House Address :")
address_label.grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

# Button to add contacts
addcontacts_button = tk.Button(root, text= "Add Contact", command= add_contact)
addcontacts_button.grid(row= 4, column=0, columnspan=2)

# button for updating contact
update_button = tk.Button(root, text ="Update", command= update_contact)
update_button.grid(row= 6, column=0, columnspan=2)

# button to delete contact
delete_button = tk.Button(root, text ="Delete", command= delete_contact)
delete_button.grid(row=7, column= 0, columnspan=2)

# Search button
search_label = tk.Label(root, text="Search :")
search_label.grid(row=5, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1)
search_button = tk.Button(root, text="Search: ", command = search_contact)
search_button.grid(row=5,column=2, columnspan=2)

# List to display contacts
contact_list = tk.Listbox(root, width=40, height=10)
contact_list.grid(row=0, column=3, rowspan= 8)
contact_list.bind("<<ListboxSelect>>", lambda event : veiw_contact)

# label to display contact details
details_text = tk.Label(root, text="", font=("Helvetica", 12))
details_text.grid(row=8, column=0, columnspan=4)

root.mainloop()