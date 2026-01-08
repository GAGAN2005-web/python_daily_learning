# Day 03 - Python Bank System using Nested Dictionary

dic = {
    "GAGAN": {
        "ACCOUNT_NO": ["2310045255"],
        "BALANCE": ["546587 RS"],
        "LOAN_BALANCE": ["5478999 RS"],
        "INSURANCE_FUND": ["0 RS"]
    },

    "VISHU": {
        "ACCOUNT_NO": ["2310045260"],
        "BALANCE": ["12541527 RS"],
        "LOAN_BALANCE": ["5425459 RS"],
        "INSURANCE_FUND": ["1251555 RS"]
    },

    "NONI": {
        "ACCOUNT_NO": ["2310045265"],
        "BALANCE": ["41527 RS"],
        "LOAN_BALANCE": ["25459 RS"],
        "INSURANCE_FUND": ["51555 RS"]
    }
}

print("WELCOME TO PYTHON BANK !!")
name = input("Enter your name: ").upper()

if name in dic:
    print("HELLO", name, "what task do you want to perform today?")
    print("1. ACCOUNT NUMBER")
    print("2. BALANCE")
    print("3. LOAN BALANCE")
    print("4. INSURANCE FUND")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        print("Your bank account number is:", dic[name]["ACCOUNT_NO"])

    elif choice == "2":
        print("Your bank balance is:", dic[name]["BALANCE"])

    elif choice == "3":
        print("Your loan balance is:", dic[name]["LOAN_BALANCE"])

    elif choice == "4":
        print("Your insurance fund is:", dic[name]["INSURANCE_FUND"])

    else:
        print("Invalid choice ❌")

else:
    print("User not found ❌")
