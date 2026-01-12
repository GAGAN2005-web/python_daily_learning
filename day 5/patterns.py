print("What kind of pattern you want to print today?")
print("1. Half pyramid pattern of numbers")
print("2. Full pyramid pattern of *")
print("3. Half pyramid with string")
print("4. Hollow Heart with *")

choice = int(input("Choose your pattern (1/2/3/4): "))

# 1. Half pyramid of numbers
if choice == 1:
    print("Welcome to choice 1!")
    row = int(input("Enter number of rows: "))

    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# 2. Full pyramid of stars
elif choice == 2:
    print("Welcome to choice 2!")
    r = 3
    k = 2

    for i in range(r):
        for j in range(1, r - i):
            print(" ", end="")
        for j in range(1, k + i):
            print("*", end="")
        k += 1
        print()

    r = 2
    k = 4
    for i in range(r):
        for j in range(1, i + 2):
            print(" ", end="")
        for j in range(1, k):
            print("*", end="")
        k -= 2
        print()

# 3. Half pyramid with string
elif choice == 3:
    s = input("Write your string: ")
    lg = len(s)

    for i in range(lg):
        for j in range(i + 1):
            print(s[j], end="")
        print()

# 4. Hollow Heart pattern
elif choice == 4:
    r = 3
    k = 2

    for i in range(r):
        for j in range(1, r - i):
            print(" ", end="")
        for j in range(1, k + i):
            print("* ", end="")
        for j in range(1, 2 * (r - i)):
            print(" ", end="")
        for j in range(1, k + i):
            print("* ", end="")
        k += 1
        print()

    k = 12
    for i in range(r):
        for j in range(1, i + 1):
            print(" ", end="")
        for j in range(1, k):
            print("* ", end="")
        k -= 2
        print()

else:
    print("Invalid choice ❌")
