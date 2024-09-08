
contacts = []


def add_contact():
    name = input("Enter name: ")
    while True:
        phone = input("Enter phone number (10 digits): ")
        if len(phone) == 10 and phone.isdigit():
            break
        else:
            print("Invalid phone number! Please enter exactly 10 digits.")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts.append(contact)
    print("\nContact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    print("\nContact List:")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    search_input = input("Enter name or phone number to search: ").lower()

    for contact in contacts:
        if contact['name'].lower() == search_input or contact['phone'] == search_input:
            print("\nContact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            return
    print("Contact not found.\n")


def update_contact():
    search_input = input("Enter name or phone number of contact to update: ").lower()

    for contact in contacts:
        if contact['name'].lower() == search_input or contact['phone'] == search_input:
            print(f"\nCurrent details for {contact['name']}:")
            print(f"1. Name: {contact['name']}")
            print(f"2. Phone: {contact['phone']}")
            print(f"3. Email: {contact['email']}")
            print(f"4. Address: {contact['address']}")

            field = input("Enter the number corresponding to the field you want to update (1-4): ")

            if field == '1':
                contact['name'] = input("Enter new name: ")
            elif field == '2':
                contact['phone'] = input("Enter new phone number: ")
            elif field == '3':
                contact['email'] = input("Enter new email: ")
            elif field == '4':
                contact['address'] = input("Enter new address: ")
            else:
                print("Invalid input.")

            print("\nContact updated successfully!\n")
            return
    print("Contact not found.\n")


def delete_contact():
    search_input = input("Enter name or phone number of contact to delete: ").lower()

    for contact in contacts:
        if contact['name'].lower() == search_input or contact['phone'] == search_input:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (yes/no): ").lower()
            if confirm == 'yes':
                contacts.remove(contact)
                print("\nContact deleted successfully!\n")
            else:
                print("Deletion canceled.\n")
            return
    print("Contact not found.\n")


def menu():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Start the program
menu()
