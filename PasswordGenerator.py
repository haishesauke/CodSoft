import tkinter as tk
import random
import string

def password_generator():
    length = int(length_entry.get())
    if length < 8:
        password_label.config(text = "Password length must be 8 charcters")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}")


root = tk.Tk()
root.title("Password genrator")

length_label = tk.Label(root , text= "how long you want your password to be? :", font =("Helvetica", 12))
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command= password_generator , font =("Helvetica", 12))
generate_button.pack()

password_label = tk.Label(root, text ="", wraplength= 300, font =("Helvetica", 14))
password_label.pack()

root.mainloop()