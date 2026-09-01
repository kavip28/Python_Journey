#Type Conversion

num = input("Enter a number: ")
print(num)
print("Type of input is: ", type(num))


#type conversion methods
# int()
# float()
# str()
# bool()

y = int(num) + 100
print(y)
print("Type of y is: ", type(y))


#falsy values - 0, "", None
print(bool(0))
print(bool(""))
print(bool(None))
print(bool(1))
print(bool("Hello"))