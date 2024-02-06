shopping = ["bread", "Donuts", "Cereal", "Chips"]

shopping.append("milk")#Add milk at the end.
print(shopping)

shopping.remove("bread")#Removes bread.
print(shopping)

shopping.insert(2, 'oranges')#Insert orange after 2nd item
print(shopping)

if "apples" in shopping:#Checks if "apples" is in the shopping list
    print("True")
else:
    print("False")
print(shopping)
