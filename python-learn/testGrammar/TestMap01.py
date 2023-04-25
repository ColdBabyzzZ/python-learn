alen = {"name":"coldBaby","age":18,"like":["play","ball","game"]}
print(alen["like"])
alen["phone"] = "156123123"
print(alen)
del alen["age"]
print(alen)

for key,value in alen.items():
    print(value)

