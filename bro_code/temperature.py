#python temperature conversion 
temp = float(input("enter your temperature: "))
con = input("convert to (C/F): ")
if con == "C":
    temp = 9 * temp/5 + 32
    print(f"the temperature is {temp}°F")
elif con == "F":
    temp = temp-32 * 5/9       #0°F − 32) × 5/9
    print(f"the temperature is {temp}°C")
else:
    print("invalid syntax")