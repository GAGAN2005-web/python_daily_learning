print( "enter the itemi name")
nam= input()

print("enter the item1 price")
price= input()

print("enter the numbers of items1")
num= input()

total_cost= int(price) * int(num)

print("enter the item2 name")
nam2= input()

print("enter the item2 price")
price2= input() 

print("enter the numbers of items2")
num2= input()

total_cost2= int(price2)* int(num2)

print("You purchased total", num+ " amount of", nam+ " each with", price+ "rs." )

print("And your Grand total is", total_cost)

print("You purchased total", num2+ " amount of", nam2+ " each with", price2+ "rs." )

print("And your Grand total is", total_cost2)

print("AND YOUR GREAT GRAND TOTAL IS", total_cost + total_cost2)
