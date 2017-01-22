import random
import webbrowser

weekFile = open("week.txt", "r")
week = weekFile.read()
weekFile.close()

print(week)

studentFile = open("students.txt", "r")

studentList = []
for line in studentFile:
    student = line.strip('\n').split(' ')
    studentList.append(student)

selectedStudent = studentList[random.randint(0, len(studentList)-1)]
print(selectedStudent)
git = selectedStudent[0]
firstName = selectedStudent[1]
lastName = selectedStudent[2]

print(firstName, lastName, "has been selected")

url = "https://gits-15.sys.kth.se/inda-16/" + git  + "-week-" + week + "/"

webbrowser.open(url)
