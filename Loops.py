# Loops

count = 0
while count < 10:
    print("The condition is true")
    count += 1


items = ['a','b','c','d']
for n in items:
    print(n)
items = ['a','b','c','d']
for index, n in enumerate(items):
    print(index, n)

for b in range(4):
    print(b)

des = [1,2,3,4]
for x in des:
    if x ==3:
        #continue
        break
    print(x)