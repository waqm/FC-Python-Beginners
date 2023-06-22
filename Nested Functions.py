#functions can be nested inside other functions. This is useful when nested function has no other use outside the function it is nested in.

# def Calculate_Eligibility():
#     getAge = int(input("What's your age? "))

#     def check():
#         if getAge >= 18:
#             print("You're good to go!")
#         else:
#             print("I'm sorry, but you're underage for this establishment.")
#     check()

# Calculate_Eligibility()

# def num1(x):
#     def num2(y):
#        return x * y
#     return num2
# res = num1(10)

# print(res(5))

# phrase = "This is a test phrase to check the split function."

# split = phrase.split()

# for n in split:
#     print(n)

def counter():
    count = 0
    print(count)
    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter()

counter()

print(increment())#1
print(increment())#2
print(increment())#3