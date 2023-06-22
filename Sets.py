#These are immutable, but you can add or remove items
#these are unordered and indexed so you can't say which order the items will appear in.

set1 = {"Paidric","Colm","Siobhan"}
set2 = {"Paidric","Colm"}

#you can intersect sets like this, and it will return only the common values between two sets
intersect = set1 & set2
print(intersect)

#you can also unite to sets
mod = set1 | set2
print(mod)

#you can also get the difference between two sets, the values which are unique different in each set
mod2 = set1 - set2
print(mod2)

#you can also check if a set contains all the values of another set, making it a superset-subset pairing
mod3 = set1 > set2
print(mod3)

print("Jenny" in set1)

#you can't use duplicate values in a set. Eg. you can't have two items with same value like "roger" and "roger"

