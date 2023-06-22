#dictionaies are data storage types where each value is paired with a key that can be used to retrieve that value
chars = {"main" : "Paul", "anti" : "Baron Harkonnen", "support" : "Stilgar", "li" : "Chani","mother" : "Jessica"}
#while keys are immutable in dict, values paired with them can be changed like this
chars["support"] = "Gurney"

print(chars["main"])
print(chars.get("anti2", "Feyd-Rautha"))

#pop function can be used to delete specific values pairs from the dict
print(chars.popitem()) #this delets the last item that was inserted into the dictionary
print(chars)

#to check if a key is contained in the dictionary you can use the in arugment
print("anti" in chars)

#we can also get the list of keys or values in the dicionary using this:
print(chars.keys())
print(chars.values()) #or
print(list(chars.keys()))
print(list(chars.values())) #or you can get all items from the dict by replacing values with items

#to add a new key-pair to the dict:
chars["dad"] = "Leto"

#to delete items
del chars["dad"]
print(chars)