def main():
    math(input("Provide an expression formatted x y z: "))

def math(expression):
    x = int(expression.partition(" ")[0])
    y = expression.partition(" ")[1]
    z = int(expression.partition(" ")[2])

    match y:
        case "+":
            return(x + z)
        case "-":
            return(x - z)
        case "*":
            return(x * z)
        case "/":
            return(x / z)
        case _:
            print("Invalid operator")
        
main()