# def hello(name):
#     print("Hello, " + name)

 

#parameters are the values accepted by the function inside the function definition
#arguments are values that are passed to the function when it is called
#an argument can have a default value if it is not specified. Like this:

def whatup(name="amigo?"):
    print("What's up, " + name + "?")

whatup(input("What's your name amigo? "))
