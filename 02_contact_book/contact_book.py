contacts = {
    "Sengül": "0472455653",
    "Princia": "0489906747",
    "Seyda": "0489906715",
    "Sophiane": "0487806715"
}

def add_contact(name, number):
    contacts[name] = number
    print(f"Contact {name} added!")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted!")
    else:
        print("Contact not found.")

def show_contacts():
    if contacts:
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

running = True

while running:
    print("1. Add contact\n2. Search contact\n3. Delete contact\n4. Show all contacts\n5. Exit")
    choice = int(input("Make a choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == 2:
        search_contact(input("Enter name: "))
    elif choice == 3:
        delete_contact(input("Enter name: "))
    elif choice == 4:
        show_contacts()
    elif choice == 5:
        running = False