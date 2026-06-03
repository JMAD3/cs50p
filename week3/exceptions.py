def main():

    
    try: #try
        x = int(input("What is x? "))
    except ValueError: #if error
        print("x is not an integer")
    else: #if successful
        print(f"x is {x}")

    #or

    while True: #loop the try statement
        try: #try
            x = int(input("What is x? "))
        except ValueError: #if error
            print("x is not an integer")
        else: #if successful
            break
    
    print(f"x is {x}")

    #or

    while True: #loop the try statement
        try: #try
            x = int(input("What is x? "))
            return x
        except ValueError: #if error
            pass


main()