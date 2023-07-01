import getpass
import json
import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to retrieve existing passwords from the JSON file
def get_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save passwords to the JSON file
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Function to generate a random password
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to create a new password entry
def create_password():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if not password:
        messagebox.showwarning("Missing Password", "Please enter a password.")
        return
    
    passwords = get_passwords()
    passwords[service] = {"username": username, "password": password}
    save_passwords(passwords)
    
    messagebox.showinfo("Success", "Password created successfully!")
    clear_entries()

# Function to retrieve a password
def retrieve_password():
    service = service_entry.get()
    
    passwords = get_passwords()
    if service in passwords:
        username = passwords[service]["username"]
        password = passwords[service]["password"]
        messagebox.showinfo("Password", f"Username: {username}\nPassword: {password}")
    else:
        messagebox.showwarning("Not Found", "Password entry not found.")

# Function to delete a password
def delete_password():
    service = service_entry.get()
    
    passwords = get_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        messagebox.showinfo("Success", "Password deleted successfully!")
    else:
        messagebox.showwarning("Not Found", "Password entry not found.")
    
    clear_entries()

# Function to clear the input entries
def clear_entries():
    service_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to suggest a random password
def suggest_password():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Create the main Tkinter window
window = tk.Tk()
window.title("Password Manager")

# Create labels and entry fields
service_label = tk.Label(window, text="Service:")
service_label.pack()
service_entry = tk.Entry(window)
service_entry.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create buttons
create_button = tk.Button(window, text="Create Password", command=create_password)
create_button.pack()

retrieve_button = tk.Button(window, text="Retrieve Password", command=retrieve_password)
retrieve_button.pack()

delete_button = tk.Button(window, text="Delete Password", command=delete_password)
delete_button.pack()

suggest_button = tk.Button(window, text="Suggest Password", command=suggest_password)
suggest_button.pack()

# Start the Tkinter event loop
window.mainloop()