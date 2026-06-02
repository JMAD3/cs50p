def main():
    print(twttr())

def twttr():
    text = input("Enter a string: ")
    result = ""

    for i in text:
        if i not in "AEIOUaeiou":
            result += i
    return result

    

main()