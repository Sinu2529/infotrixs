def add_contact(contacts, name, phone, email):
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact(contacts, name):
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = {}
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone, email)

        elif choice == '2':
            view_contacts(contacts)

        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            delete_contact(contacts, name)

        elif choice == '5':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
