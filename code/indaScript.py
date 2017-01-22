import random
import webbrowser

print("Which week is it?")
week = input()

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

            print(firstName, lastName, "has been selected")

            url = "https://gits-15.sys.kth.se/inda-16/" + git  + "-week-" + week + "/"
            webbrowser.open(url)

    elif answer == "n":
        print("Then my purpose is finito")
        coolRunnings = False

    else:
        print("Mr robato no understato")
