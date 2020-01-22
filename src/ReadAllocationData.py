## @file ReadAllocationData.py
#  @brief Provides read opperations on files
#  @author Matthew Braden
#  @date 1/17/2019

## @brief Reads students data
#  @details Creates a dictionary of students from a file
#  @param s File of students data
def readStdnts(s):
    file = open(s, "r")
    students = file.read()
    students = students.replace("{", "")
    students = students.replace("\'", "")
    students = students.replace("}", "")
    students = students.replace(",", "")
    students = students.replace("[", "")
    students = students.replace("]", "")
    students = students.splitlines()
    file.close()
    studentlst = []
    for i in students:
        studenti = i.split()
        studentdict = {}
        for j in range(len(studenti)):
            if (j == 0):
                studentdict["macid"] = studenti[0]
            elif (j == 1):
                studentdict["fname"] = studenti[1]
            elif (j == 2):
                studentdict["lname"] = studenti[2]
            elif (j == 3):
                studentdict["gender"] = studenti[3]
            elif (j == 4):
                studentdict["gpa"] = float(studenti[4])
            elif (j == 5):
                choices = [studenti[5], studenti[6], studenti[7]]
                studentdict["choices"] = choices

        studentlst.append(studentdict)
    return (studentlst)

## @brief Reads students data
#  @details Creates a dictionary of students from a file for free choice
#  @param s File of students data

def readFreeChoice(s):
    file = open(s, "r")
    fstudent = file.read()
    fstudent = fstudent.replace("\'", "")
    file.close()
    return fstudent.splitlines()
## @brief Reads students data
#  @details Creates a dictionary from students in from a file
#  @param s File of departments data
def readDeptCapacity(s):
    file = open(s, "r")
    departments = file.read()
    departments = departments.replace("{", "")
    departments = departments.replace("\'", "")
    departments = departments.replace("}", "")
    departments = departments.replace(",", "")
    departments = departments.splitlines()
    file.close()
    for i in departments:
        departmenti = i.split()
        department = {}
        for j in range(len(departmenti)):
            if (j == 0):
                department["Civil"] = int(departmenti[1])
            elif (j == 1):
                department["Chemical"] = int(departmenti[3])
            elif (j == 2):
                department["Electrical"] = int(departmenti[5])
            elif (j == 3):
                department["Mechanical"] = int(departmenti[7])
            elif (j == 4):
                department["Software"] = int(departmenti[9])
            elif (j == 5):
                department["Materials"] = int(departmenti[11])
            elif (j == 6):
                department["EngPhys"] = int(departmenti[13])
    return department
