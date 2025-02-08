x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "orange"
x = tuple(y)
print(x)



thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)