import math
test_h=int(input("Enter the hight of wall or object"))
test_w=int(input("enter the widths of wall or object"))
coverage=5
cal=math.ceil((test_w*test_h)/coverage)
print(f"{cal} can needs to cover a objet of length {test_w*test_h} Square meter")