# loops!

# while loop

i = 0
while i < 3:
    print("meow")
    i += 1

while True:
    n = int(input("What is n?"))
    if n > 0:
        break #return n
#return n

# for loop

for _ in (0,1,2):
    print("meow")

# or?

for _ in range(3):
    print("meow")

# or??

print("meow\n" * 3, end="")

studentsList = ["john", "jake", "jill"]

for student in studentsList:
    print(student)

# or 

for i in range(len(studentsList)):
    print(studentsList[i])

# dicts! Key:value

studentsDict = {
    "john":"senior",
    "jill":"sophomore",
    "jack":"freshman"
}

for student in studentsDict:
    print(student, studentsDict[student])

studentsDict = [
    {"name": "Jack", "grade": "freshman", "gender": "male"}
    {"name": "jill", "grade": None, "gender": "female"}
]