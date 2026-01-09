# Day 04 - School Result System using Lists

list1 = [
    ["00", "none", 0.0],
    ["01", "AVI", 6.5],
    ["02", "DIYA", 3.5],
    ["03", "AAYUSH", 8.6],
    ["04", "ANSH", 9.5],
    ["05", "AARAV", 5.5],
    ["06", "AAROHI", 7.5],
    ["07", "AARUSH", 4.5],
    ["08", "AARYAN", 6.5],
    ["09", "AARYA", 8.5],
    ["10", "AASHISH", 9.5]
]

print("WELCOME TO LOINS SCHOOL RESULT ANNOUNCEMENT!")
print("Choose an option from below >>>")
print("1. MY RESULT")
print("2. RANK LIST")
print("3. AVERAGE RESULT OF SCHOOL")

choice = input("Enter your choice: ")

if choice == "1":
    num = int(input("Enter your roll number: "))
    print("Hello!", list1[num][1], "you got", list1[num][2], "CGPA.")

    if list1[num][2] > 4:
        print("And you are PASS ✅")
    else:
        print("And you are FAIL ❌")

elif choice == "2":
    print("Here is the rank list of our students!")
    list1.sort(key=lambda x: x[2], reverse=True)

    for roll, name, cgpa in list1:
        if roll != "00":
            print(name, "-", cgpa)

elif choice == "3":
    total = 0
    count = 0

    for roll, name, cgpa in list1:
        if roll != "00":
            total += cgpa
            count += 1

    avg = total / count
    print("The average result of school is:", round(avg, 2))

else:
    print("Invalid choice ❌")
