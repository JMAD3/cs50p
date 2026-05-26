def main():
    print(thought())

def thought():
    answer = input("What is the meaning of life?")

    return True if answer == "42" else False
    
main()