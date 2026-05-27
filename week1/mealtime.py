def main ():
    convert(input("What time is it? (in 24hr time)"))
    

def convert(time):
    hour = time.split(":")[0]
    minute = time.split(":")[1]

    if hour == "7":
        print("breakfast time")
    elif hour == "12":
        print("lunch time")
    elif hour == "18":
        print("dinner time")

    #I dont see the point in running the conversion for 
    #this problem, but it would look something like this

    conversion = (float(hour) + (float(minute) / 60))
    print(conversion)

    

if __name__ == "__main__":
    main()