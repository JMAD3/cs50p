def main():
    print(math(input("Provide an expression formatted x y z: ")))

def math(expression):
    x = float(expression.split()[0])
    y = expression.split(" ")[1]
    z = float(expression.split(" ")[2])

    match y:
        case "+":
            return(round(x + z, 1))
        case "-":
            return(round(x - z, 1))
        case "*":
            return(round(x * z, 1))
        case "/":
            return(round(x / z, 1))
        case _:
            return("Invalid operator")
        
main()