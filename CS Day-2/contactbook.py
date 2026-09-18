import json
try:
    with open("contactbook.json", "r") as file:
        contactbook = json.load(file)
except FileNotFoundError:
    contactbook = {}

def save_contacts():
    with open("contactbook.json", "w") as file:
        json.dump(contactbook, file, indent=4) 

def add_contact():
    name = input("Enter name: ")
    if name in contactbook:
        print("Contact already exists!")
        return
    phone = input("Enter phone: ")
    contactbook[name] = {
        "phone": phone,
        
    }
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contactbook:
        print("No contacts found.")
        return
    for name, details in contactbook.items():
        print("Name:", name)
        print("Phone:", details["phone"])
        print("----------------")

def search_contact():
    name = input("Enter name to search: ")
    if name in contactbook:
        details = contactbook[name]
        print("Name:", name)
        print("Phone:", details["phone"])
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contactbook:
        del contactbook[name]
        save_contacts()
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")        
main()            