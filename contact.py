def display_contact(contact):
    print("Name\t\t Contact Number")
    for name, phone in contact.items():
        print("{}\t\t{}".format(name, phone))

def update_contact(contact):
    edit_contact = input("Enter the contact to be edited: ")
    if edit_contact.lower() in contact:
        new_phone = input("Enter the new phone number (10 digits only): ")
        if len(new_phone) == 10 and new_phone.isdigit():
            contact[edit_contact.lower()] = new_phone
            print(f"The phone number of {edit_contact} has been updated to {new_phone}.")
            display_contact(contact)
        else:
            print("Invalid phone number format. Please enter 10 digits only.")
    else:
        print("Name is not found in the contact list.")

def delete_contact(contact):
    delete_contact = input("Enter the contact to be deleted: ")
    if delete_contact.lower() in contact:
        confirm = input(f"Do you want to delete {delete_contact}? (y/n): ")
        if confirm.lower() == "y":
            del contact[delete_contact.lower()]
            print(f"{delete_contact} has been deleted from the contact list.")
            display_contact(contact)
    else:
        print("Name is not found in the contact list.")

contact = {}

while True:
    print("\nMenu:")
    print("1. Add new contact")
    print("2. Search contact")
    print("3. Display contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ").lower()
        phone = input("Enter the phone number (10 digits only): ")
        if len(phone) == 10 and phone.isdigit():
            contact[name] = phone
            print("Contact added successfully.")
        else:
            print("Invalid phone number format. Please enter 10 digits only.")

    elif choice == "2":
        search_name = input("Enter the name to search: ").lower()
        if search_name in contact:
            print(f"{search_name.capitalize()}'s phone number is {contact[search_name]}.")
        else:
            print("Name not found in the contact list.")

    elif choice == "3":
        if contact:
            display_contact(contact)
        else:
            print("Contact list is empty.")

    elif choice == "4":
        update_contact(contact)

    elif choice == "5":
        delete_contact(contact)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
