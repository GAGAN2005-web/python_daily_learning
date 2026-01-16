# Day 08 - Student Daily Performance Tracker

students = {}

while True:
    print("\n===== STUDENT PERFORMANCE SYSTEM =====")
    print("1. Add Student Record")
    print("2. View Student Record")
    print("3. Show Rank List")
    print("4. Show Class Average")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks (out of 10): "))

        students[roll] = {"Name": name, "Marks": marks}
        print("Record added successfully ✅")

    elif choice == "2":
        roll = input("Enter Roll Number to view: ")
        if roll in students:
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found ❌")

    elif choice == "3":
        print("\n--- Rank List ---")
        sorted_list = sorted(students.items(), key=lambda x: x[1]["Marks"], reverse=True)

        rank = 1
        for roll, data in sorted_list:
            print(rank, ".", data["Name"], "-", data["Marks"])
            rank += 1

    elif choice == "4":
        total = 0
        for data in students.values():
            total += data["Marks"]

        if len(students) > 0:
            avg = total / len(students)
            print("Class Average:", round(avg, 2))
        else:
            print("No records to calculate average.")

    elif choice == "5":
        print("Exiting... Keep Learning Daily 🔥")
        break

    else:
        print("Invalid choice ❌")
