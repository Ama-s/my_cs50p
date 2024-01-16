my_dict = {}
#to create an empty list

while True:
    try:
        item = input().upper()
        if item not in my_dict:
            my_dict[item] = 1
            #to access the value of a key, i.e the meaning of a key, use []
        else:
            my_dict[item] += 1
            #if item is already on the list, increase that item's value by 1
    except (EOFError, KeyError):
        # Ctrl-D was pressed to end input
        break

sorted_dict = sorted(my_dict.keys())
#sorts the dictionary's keys in an alphabetical order

for item in sorted_dict:
    print(my_dict[item], item)
