def main():

    fuel()

def fuel():
    while True:
        try:
            gas = input("Enter a fraction formatted X/Y: ")
            gas = gas.split("/")
            x = int(gas[0])
            y = int(gas[1])
            percent = (x/y)*100

            if percent > 100:
                raise ValueError("Gas tank is over full.")
        
            if percent > 98:
                raise ValueError("F.")
        
            if percent < 2:
                raise ValueError("E")
        
        except ValueError as error:
            print(error)

        except ZeroDivisionError:
            print("Try again")

        else:
            print(f"{int(percent)}%")
            break
        
main()