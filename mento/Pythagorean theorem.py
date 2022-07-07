a = input("a")
b = input("b")

while a.isnumeric() != True :
    print("a재입력")
    a = input("a")

while b.isnumeric() != True :
    print("b재입력")
    b = input("b")

c = int(a) ** 2 + int(b) ** 2
print(int(c) ** 0.5)
