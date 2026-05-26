def main():
    print(h(input("Enter a greeting: ")))

def h(greeting):
    greeting = greeting.strip()
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("h"):
        return 20
    else:
        return 0

main()