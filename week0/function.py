# variable == value assignment
# function == a method for doing something
# input == python provided function for obtaining user input
# str == string. sequence of values that can be really anything
# formatted strings == special formatting in python for strings.

def main():
    name = input("whats your name?")
    hello(name)
    dog()

def dog():
    dog = input("What is your favorite dog?")
    dog = dog.strip() #remove whitespace
    dog = dog.capitalize() #it might capitalize words. not sure though.
    print(f"Your favorite dog is: {dog}")

def hello(to="world"): #pass a defualt value
    print("hello,", to)

main()