# elif = else if
# mostly review here

def main():
    matches(input("Enter a case number between 1 and 3. Cases 4, 5, ande 6 are grouped: "))


def is_even(n): # this is a cool method
    return True if n % 2 == 0 else False

# or

def is_even2(n):
    return (n % 2 == 0)

# match is similar to switch

def matches(case):
    match case:
        case "1":
            print("Case 1")
        case "2":
            print("Case 2")
        case "3":
            print("Case 3")
        case "4" | "5" | "6":
            print("Group 4, 5, 6")
        case _:
            print("Unhandled case")


main()