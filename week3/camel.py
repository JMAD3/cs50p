def main():
    print(case())

def case():
    camel = input("Enter a variable name in camel case:")
    snake = ""

    for _ in camel: # iterate
        if _.isupper() == True: # find uppercase
            snake += "_" + _
        else:
            snake += _ 
        
    snake = snake.replace(" ", "")
    snake = snake.lower()
    return snake

main()

# sherry mcgraw 