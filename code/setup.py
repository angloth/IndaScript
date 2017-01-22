print("Which week?")
week = input()

weekFile = open("week.txt", "w")
weekFile.write(week)
weekFile.close()
print()
print("Current students:")
print()
studentFile = open("students.txt", "r")
for line in studentFile:
    print(line)

answered = False
while answered is False:
    print("Does this look good? y/n")
    answer = input().lower()
    if answer == "y":
        print("Dats chill")
        answered = True
    elif answer == "n":
        print("Well go fix it then what am I? Your servant?")
        answered = True
    else:
        print("Sorry mr robato no understato")
