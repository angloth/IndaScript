import random
import webbrowser

print("Which week is it? (Type week nr + 'pal' if you want palinda)")
inp = []
inp = input().split(' ', 1)
week = inp[0].lower()
palinda = False
if (len(inp) == 2):
    if (inp[1] == "pal"):
        palinda = True


studentFile = open("students.txt", "r")

studentList = []
for line in studentFile:
    student = line.strip('\n').split(' ')
    studentList.append(student)

coolRunnings = True

while coolRunnings:
    print("Select a student? y/n")
    answer = input().lower()
    if answer == "y":
        if len(studentList) == 0:
            print("Sorry yer out of students :^)")
            coolRunnings = False

        else:
            selectedStudent = studentList.pop(random.randint(0, len(studentList)-1))
            git = selectedStudent[0]
            firstName = selectedStudent[1]
            lastName = selectedStudent[2]
            weekType = ""
            if (palinda):
                weekType = "-palinda-"
            else:
                weekType = "-week-"

            print(firstName, lastName, "has been selected")

            url = "https://gits-15.sys.kth.se/inda-16/" + git  + weekType + week + "/"

            webbrowser.open(url)

    elif answer == "n":
        print("Initiating self destruct...")
        coolRunnings = False

    else:
        print("Mr robato no understato")
