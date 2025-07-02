# Contact Management System
contacts = []

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email (optional): ").strip()

        if not name or not phone:
            print("Error: Name and phone are required!")
            continue

        contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found!")
            continue

        print("\nAll Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

    elif choice == "3":
        search = input("Enter name to search: ").lower().strip()
        found = [c for c in contacts if search in c["name"].lower()]

        if not found:
            print("No matching contacts found!")
            continue

        print("\nMatching Contacts:")
        for contact in found:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")

    elif choice == "4":
        name = input("Enter name to update: ").strip()
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print(f"\nCurrent details: {contact['phone']} - {contact['email']}")
                contact["phone"] = input("Enter new phone (leave blank to keep): ") or contact["phone"]
                contact["email"] = input("Enter new email (leave blank to keep): ") or contact["email"]
                print("Contact updated!")
                break
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
