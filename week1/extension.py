def main():
    extension(input("Enter a file with its extension: "))

def extension(string):
    ext = string.partition(".")[2] or string
    
    match ext:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("image/pdf")
        case "txt":
            print("note/txt")
        case "zip":
            print("comp/zip")
        case _:
            print("application/octet-stream")

main()