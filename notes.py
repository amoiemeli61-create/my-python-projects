
nots = []
import calendar

while True:
    print(
        "====Calender====",
        "\n" "1.Calender" "\n" "2.Days in month",
        "\n" "3.Leap year",
        "\n" "4.Notes" "\n",
        "5.Exit",
    )
    choice = input("Enter your choice:")

    if choice[0] == "1" or choice[0] == "C" or choice[0] == "c":
        year = int(input("Enter Year:"))
        month = int(input("Enter Month:"))
        print(calendar.month(year, month))

    if choice[0] == "2" or choice[0] == "D" or choice[0] == "d":
        year = int(input("Enter year:"))
        month = int(input("Enter month:"))
        month_days = calendar.monthrange(year, month)
        month_name = calendar.month_name[month]
        print(year, month_name, month_days[1])

    if choice[0] == "3" or choice[0] == "l" or choice[0] == "L":
        year = int(input("Enter year:"))
        leap_year = calendar.isleap(year)
        if leap_year == True:
            print("Leap year")
        else:
            print("No Leap year")

    if choice[0] == "4" or choice[0] == "N" or choice[0] == "n":
        print(
            "====Nots===="
            "\n"
            "1.Add note"
            "\n"
            "2.show notes"
            "\n"
            "3.Delete note"
            "\n"
            "4.Edit note"
            "\n"
            "5.search note"
        )
        note = input("Enter your not:")

        if note[0] == "1" or note[0] == "A" or note[0] == "a":
            Note = input("Enter note:")
            nots.append(Note)

        if note[0] == "2" or note[0] == "S" or note[0] == "s":
            for i in nots:
                print(i)

        if note[0] == "3" or note[0] == "D" or note[0] == "d":
            delete = input("which note do you want to delete:")
            deleted = False
            for i in nots:
                if delete == i:
                    deleted = True
                    nots.remove(i)
                    break
            if deleted == True:
                print("Note deleted successfully")
            else:
                print("Note not found")

        if note[0] == "4" or note[0] == "E" or note[0] == "e":
            edit = input("Which note do you want to edit? ")
            Edited = False
            for i in nots:
                if edit == i:
                    Edited = True
                    new_edit = input("Enter the new note?")
                    n = nots.index(edit)
                    nots[n] = new_edit
                    break
            if Edited == True:
                print("Note edited successfully")
            else:
                print("Failed to edit note")

        if note[0] == "5" or note[0] == "F" or note[0] == "f":
            search = input("Please search: ")
            found = False
            for i in nots:
                if search == i:
                    found = True
                    break
            if found == True:
                print("Found!")
            else:
                print("No Found!")

    if choice == "5":
        break