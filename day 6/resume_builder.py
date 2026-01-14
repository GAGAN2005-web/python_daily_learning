# Day 06 - Resume Builder using Python

resume = {
    "personal_info": {},
    "education": [],
    "skills": [],
    "project": []
}

print("HELLO JOBSEEKER! LET'S BUILD YOUR RESUME >>>>>")
print("Rules: you have to only enter the asked information in right format.")
print("-" * 20)

# Personal Information
print("Let's start with your personal information ;")
resume["personal_info"]["name"] = input("Enter your name here: ")
resume["personal_info"]["city"] = input("Enter your city here: ")
resume["personal_info"]["age"] = input("Enter your age here: ")
resume["personal_info"]["email"] = input("Enter your email here: ")
resume["personal_info"]["phone"] = input("Enter your phone number here: ")

print("-" * 20)

# Education
print("Great! We are done with personal information, now let's jump to education information >>>>>")
m = int(input("How many education records you want to add? "))

for i in range(m):
    degree = input("Enter degree (eg. B.Tech): ")
    year = input("Enter graduation year: ")
    grade = input("Enter grades: ")
    resume["education"].append((degree, year, grade))

print("-" * 20)

# Skills
print("YOOO! It's time to add your skills >>>>>")
n = int(input("How many skills you want to add? "))

for i in range(n):
    skill = input(f"Enter skill #{i+1}: ")
    resume["skills"].append(skill)

print("-" * 20)

# Projects
print("You are going great, now tell us about your crazy projects >>>>> ")
p = int(input("How many projects you want to add? "))

for i in range(p):
    title = input("Enter the title of your project: ")
    des = input("Enter a brief description of your project: ")
    resume["project"].append({"title": title, "description": des})

print("-" * 20)
print("FAM! WE ARE DONE WITH THE INFORMATION GATHERING.")
choose = input("Enter your choice (yes/no) to generate resume: ")

if choose.lower() == "yes":
    print("=" * 50)
    print("RESUME".center(50))
    print("=" * 50)

    print("\nPERSONAL INFORMATION >>>>>")
    print("-" * 30)
    info = resume["personal_info"]
    print("Name:".ljust(15), info["name"].title())
    print("City:".ljust(15), info["city"])
    print("Age:".ljust(15), info["age"])
    print("Email:".ljust(15), info["email"])
    print("Mobile:".ljust(15), info["phone"])

    print("\nSKILLS >>>>>")
    print("-" * 30)
    for skill in resume["skills"]:
        print("<>", skill.capitalize())

    print("\nEDUCATION >>>>>")
    print("-" * 30)
    for degree, year, grade in resume["education"]:
        print(f"{degree} ({year}) - Grade: {grade}")

    print("\nPROJECTS >>>>>")
    print("-" * 30)
    for project in resume["project"]:
        print(f"<> {project['title'].upper()}")
        print(f"   {project['description']}\n")

    print("=" * 50)
    print("RESUME CREATED SUCCESSFULLY!".center(50))
    print("=" * 50)

else:
    print("Invalid choice ❌")
