#input = a function that prompts the user to enter data
#     returns the entered data as a string
name = input("what is your name?:")
print(f"my name is {name}")


#excercise 1: rectangle area calculation
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("enter the breadth of the rectangle: "))
area = length * breadth
print(f"the area of the given rectangle is:{area} cm²")

#numlock+alt+0178 for ²

#excercise 2: shoping cart problem
item = input("enter the item: ")
price = float(input("what is the price?: "))
quantity = int(input("how many would you like?: "))
total = price * quantity 
print(f"you have bought {quantity} x {item}/s")
print(total)