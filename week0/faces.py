def main():
    convert(input("Give me a series of :) or :( inputs:)"))

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    print(text)

    return(text)
    
main()