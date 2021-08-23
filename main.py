import sqlite3

conn = sqlite3.connect("Schedule.db")
cur = conn.cursor()
print("Database opened successfully")


# Create a new entry into the database
# TODO: Error handling
def createNewEntry():
    assignment = input("Enter assignment name: ")
    classcode = input("Enter class code: ")
    duedate = input("Enter the due date: ")
    note = input("Enter any notes: ")

    cur.execute("INSERT INTO assignments (assignment_name, class, due_date, completion, notes) VALUES (?,?,?,'FALSE',?)", (assignment, classcode, duedate, note))
    conn.commit()
    print("Entry Successful\n")


# Deletes an entry from the database
# TODO: Error handling
def deleteEntry():
    delSel = input("Enter the ID of the row: ")
    cur.execute("DELETE FROM assignments WHERE ID = (?)", (delSel,))
    conn.commit()
    print("Entry deleted\n")


# Show all of the database entries to the user
# TODO: Error handling
def showAllEntries():
    print("\n")
    cur.execute("SELECT * FROM assignments ORDER BY due_date")
    allrows = cur.fetchall()
    print("%-5s %-30s %-15s %-15s %-15s %s" % ("ID", "Assignment Name", "Class", "Due Date", "Completed?", "Notes"))    # Formatting for columns
    print("%-5s %-30s %-15s %-15s %-15s %s" % ("", "---------------", "-----", "-----", "-----", "-----"))
    for row in allrows:
        print("%-5d %-30s %-15s %-15s %-15s %s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
    print("\n")


# Mark an entry as complete, updating the "Completed?" field to TRUE
# TODO: Implement a way to undo the completion
# TODO: Error handling
def markEntryComplete():
    comSel = input("Enter ID of complete assignment: ")
    cur.execute("UPDATE assignments SET completion = 'TRUE' WHERE ID = (?)", comSel)
    conn.commit()
    print("Entry marked as complete\n")


def menu():
    print("1. Create an entry")
    print("2. Delete entry")
    print("3. Display all rows")
    print("4. Mark entry as complete")
    print("0. Exit the program")
    # TODO: Implement a way to filter selections via class?


def main():
    menu()
    selection = int(input("Enter your selection: "))

    while selection != 0:
        if selection == 1:
            createNewEntry()
            pass
        elif selection == 2:
            deleteEntry()
            pass
        elif selection == 3:
            showAllEntries()
            pass
        elif selection == 4:
            markEntryComplete()
            pass
        else:
            print("Error")

        menu()
        selection = int(input("Enter your selection: "))


if __name__ == "__main__":
    main()
    conn.close()
    print("Database closed")
