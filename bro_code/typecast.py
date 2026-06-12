#typecasting = the process of converting one variable to another
#             str(),int(),bool(),float()

name = "brocode"
age = 25
is_stud = True
weight = 65.52

print(type(age))
print(int(weight))

age += 1
print(age)

age = str(age)
age += "1"
print(age)

name = bool(name)
print(name)
name = ""
name = bool(name)
print(name)