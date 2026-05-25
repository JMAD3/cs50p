def main():
    indoorVoice(input("Say something:"))

def indoorVoice(words):
    quietWords = words.lower()
    print(f"Shh! {quietWords}")

    return quietWords

main()
