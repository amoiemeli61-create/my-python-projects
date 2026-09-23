contacts = []
while True:
    name = input("Enter name?")
    phone = input("please enter your phone number?")
    sticker = input("Enter a sticker:")
    display = name + sticker
    print(display, "\t", phone)
    save = [name, phone]
    contacts.append(save)
    for i in contacts:
        print(i)
    search = input("please search?")
    found = False
    for i in contacts:
        if search == i[0] or search == i[1]:
            found = True
            break
    if found == True:
        print("Found!")
    else:
        print("not found")
    Delete = input("which contact do you want to Delete?")
    found = False
    for i in contacts:
        if Delete == i[0] or Delete == i[1]:
            contacts.remove(i)
            found = True
            break
    if found == True:
        print("Deleted!")
    else:
        print("not Deleted!")
    choice = input("Edit name or phone?")
    Edit = input("which one?")
    found = False
    for i in contacts:
        if choice == "name":
            if Edit == i[0]:
                found = True
                new_name = input("Enter new name?")
                i[0] = new_name
                break
        elif choice == "phone":
            if Edit == i[1]:
                found = True
                new_phone = input("Enter new phone?")
                i[1] = new_phone
                break
    if found == True:
        print("Edited!")
    else:
        print("not Edited!")
    close = input("Do you want exit?")
    if close == "Yes":
        break
