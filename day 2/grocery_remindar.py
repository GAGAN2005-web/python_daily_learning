essentialgrocery =("Fruits","Oats","Dryfruits", "Beans","Vegetables", "Milk") #tuple
surprisegrocery= ["Curd","Yogurt","Breads","Cookies","Ketchup","Icecream", "Coldrinks","Eggs", "Chocolates", "Potato", "Tomato"] #list

print("HELLO SHOPPER, HERE'S YOUR TODAY'S GROCERY REMINDAR!")
startindex = int(input("choose a random number for surprise grocery from 0 to 10! "))

print("ESSENTIALS GROCERY:", essentialgrocery)
print("SURPISE GROCERY:", surprisegrocery[startindex: ]) #list slicing