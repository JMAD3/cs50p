def main():
    print(pay())

def pay():
    change = 0
    slot = 0
    
    while change < 50:
        slot = int(input("Insert a coin: "))
        

        match slot:
            case 1| 5| 10| 25:
                change += slot
            case _:
                print("Not a real coin")

        print(f"Total: {change}")

    return change - 50


main()