import getpass
import json
import random
import string

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
    service = input("Enter the service name: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    passwords = get_passwords()
    passwords[service] = {"username": username, "password": password}
    save_passwords(passwords)
    print("Password created successfully!")

# Function to retrieve a password
def retrieve_password():
    service = input("Enter the service name: ")
    
    passwords = get_passwords()
    if service in passwords:
        username = passwords[service]["username"]
        password = passwords[service]["password"]
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print("Password entry not found.")

# Function to delete a password
def delete_password():
    service = input("Enter the service name: ")
    
    passwords = get_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print("Password deleted successfully!")
    else:
        print("Password entry not found.")

# Function to authenticate the user
def authenticate():
    password = getpass.getpass("Enter your screenlock password: ")

    # Let's assume the username is "admin" and password is "password"
    if password == "password":
        return True
    else:
        print("Authentication failed.")
        return False

# Main menu loop
while True:
    if authenticate():
        print("\nPassword Manager Menu:")
        print("1. Create new password entry")
        print("2. Retrieve password")
        print("3. Suggest random password")
        print("4. Delete password")
        print("5. Exit")

        choice = input("Enter your choice (1-5):")

        if choice == "1":
            create_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            length = int(input("Enter the length of the password: "))
            password = generate_password(length)
            print("Suggested password:", password)
        elif choice == "4":
            delete_password()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        break
    else:
        print("Authentication failed. Please try again.")