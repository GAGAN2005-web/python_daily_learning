# Day 07 - Daily Log Database System

db = {}

while True:
    print("\nWELCOME TO PYTHON DAILY LOG DATABASE")
    print("What kind of entries do you want to do today?")
    print("1. Daily Learning Log")
    print("2. Daily Fitness Log")
    print("3. Daily Activity Log")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3/4): "))
    print("=" * 30)

    if choice == 4:
        print("Exiting... Have a productive day! 👋")
        break

    date = input("Enter today's date (e.g. 2025-07-13): ")

    if date not in db:
        db[date] = []

    num = int(input("How many entries you want to add today? "))

    # 1. Learning Log
    if choice == 1:
        for i in range(num):
            topic = input("1. What topic did you learn today? ")
            difficulties = input("2. Where did you feel difficulty? ")
            doubts = input("3. Enter your doubts here: ")
            question = input("4. Write practice question here: ")

            log = {
                "Type": "Learning",
                "Topic": topic,
                "Difficulties": difficulties,
                "Doubts": doubts,
                "Question": question
            }

            db[date].append(log)

    # 2. Fitness Log
    elif choice == 2:
        for i in range(num):
            exercise = input("1. Which exercise did you hit today? ")
            difficult_weight = input("2. Which weight felt difficult? ")
            pr = input("3. Enter your PR: ")
            diet = input("4. What diet did you have today? ")

            log = {
                "Type": "Fitness",
                "Exercise": exercise,
                "Difficult_weight": difficult_weight,
                "PR": pr,
                "Diet": diet
            }

            db[date].append(log)

    # 3. Activity Log
    elif choice == 3:
        for i in range(num):
            activity = input("1. Which activity did you do today? ")
            feeling = input("2. How did you feel after activity? ")
            doubt = input("3. Any doubts or thoughts? ")

            log = {
                "Type": "Activity",
                "Activity": activity,
                "Feeling": feeling,
                "Doubt": doubt
            }

            db[date].append(log)

    else:
        print("Invalid choice ❌")

    print("=" * 30)
    print("TODAY'S DAILY LOG UPDATED SUCCESSFULLY ✅")
    print(db)
    print("=" * 30)
