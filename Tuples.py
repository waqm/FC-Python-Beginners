#you can't add a tuple after it has been created without modifying the original data type. With lists you can use extend, remove or append arguments, but not here.
#tuples use parentheses instead of square brackets.
#these are also indexed.
names = ("Paul","Leto","Duncan","Gurney","Chani")

#you can create a new tuple by adding the values of previous tuple

newnames = names + ("Rabban","Baron","Jessica","Thufir","Stilgar")

print(newnames)

#they are quite similar to lists in other functionalities