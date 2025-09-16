import time

contact_list = {}

def add_to_contact(phone_book, name, phone_no):


    if name not in phone_book:
        phone_book[name] = [phone_no]
        print("Contact added successfully")
        time.sleep(1)
    else:
        phone_book[name].append(phone_no)
        print("Contact added successfully")
        time.sleep(1)


def search_in_contact(phone_book, name):
    if name in phone_book:
        print(f"Contact number of {name} is: {phone_book[name]}")
        time.sleep(1)
    else:
        print("Contact not found")
        time.sleep(1)


def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Deleted the contact {name} successfully")
        time.sleep(1)
    else:
        print("Please enter a valid name.")
        time.sleep(1)


def view_contact(phone_book):
    for name,phone_no in phone_book.items():
        print(f"""Name: {name}     :       Mobile No: {phone_no}""")


def main():
    print("""===========Menu===========
1.) Add a new contact press 1
2.) Search a contact press 2
3.) Delete a contact
4.) View Contacts""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone_no = input("Enter Phone No: ")


        add_to_contact(phone_book=contact_list, name=name, phone_no=phone_no)
        print(contact_list)

    if choice == 2:

        name = input("Enter name: ")
        search_in_contact(phone_book=contact_list, name=name)

    if choice == 3:

        name = input("Enter name: ")
        delete_contact(phone_book=contact_list, name=name)

    if choice == 4:

        view_contact(phone_book=contact_list)

while True:
    main()