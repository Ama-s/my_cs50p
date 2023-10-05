var_name = input("camelCase: ")
for i in var_name:
    if i.isupper():
        i = i.lower()
        print("_", end = "")
    print(i, end = "")
print()
