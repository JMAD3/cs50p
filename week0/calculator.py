
def main():
    x = input("Int1:")
    y = int(input("Int2:")) #nested functions work from inside -> out

    z = int(x) + y #can convert strings to ints in python

    print(z)

    a = float(input("Float1:"))
    b = float(input("Float2:"))

    print(round(a / b, 2))

    c = a / b

    print(f"{c:.2f}") # or with formatting

    return c #produces as an output of the function

main()