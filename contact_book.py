import os

FILE_NAME = "contacts.txt"

# Function to add a contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully!\n")


# Function to view all contacts
def view_contacts():
    if not os.path.exists(FILE_NAME):
        print("No contacts found.\n")
        return

    with open(FILE_NAME, "r") as file:
        contacts = file.readlines()

        if not contacts:
            print("No contacts available.\n")
            return

        print("\n--- Contact List ---")
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            print(f"Name: {name}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            print("-" * 20)
    print()


# Function to search contact
def search_contact():
    search_name = input("Enter name to search: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("No contacts found.\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")

            if search_name in name.lower():
                print("\nContact Found:")
                print(f"Name: {name}")
                print(f"Phone: {phone}")
                print(f"Email: {email}")
                print("-" * 20)
                found = True

    if not found:
        print("Contact not found.\n")


# Main menu
def main():
    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()