def main():
    grocery()

def grocery():
    groceries = {}

    while True:
        try: 
            item = input("Enter item: ")
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            print(groceries)
            break


main()

