import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")

def is_valid(s):
     valid_size = size(s)
     valid_zeros = zeros(s)
     valid_special_characters = special_characters(s)
     valid_middle_numbers = middle_numbers(s)

     return valid_size & valid_zeros & valid_special_characters & valid_middle_numbers

def size(s):
    return 2 <= len(s) <= 6
    
def zeros(s):
    if s[0] == 0:
        return False
    else: 
        return True
    
def special_characters(s):
    result = ""

    for i in s:
        if i in string.punctuation:
            return False
        else:
            return True
        

def middle_numbers(s):
    mid = len(s) // 2

    if any(c.isdigit() for c in s[:mid]) is True:
        return False
    elif any(c.isdigit() for c in s[mid:]) is True & s[-1].isalpha() is True:
       return False
    else:
      return True



# no numbers in the middle of the plate

main()