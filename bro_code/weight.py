#python weight convertor

weight = float(input("enter your weight: "))
unit = input("unit of weight you want(K/L): ")
if unit == "K":
    print(weight * 2.20462)
else:
    print(weight / 2.20462)

