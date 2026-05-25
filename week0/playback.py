def main():
    text = input("Say something, preferrably with spaces: ")
    playback(text)
    
    
def playback(script):
    newScript = script.replace(" ", "...")
    print(newScript)
    return(newScript)

main()