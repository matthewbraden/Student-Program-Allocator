## @file testCalc.py
#  @brief Preforms tests on previous modules
#  @author Matthew Braden
#  @date 1/17/2019
from ReadAllocationData import *
from CalcModule import *

def Equal(test, result, name):
    if test == result:
        print("Test passed, %s == %s, %s " % (test, result, name))
    else:
        print("Test failed, %s != %s, %s " % (test, result, name))
#Line 8-12 for Equal found from https://tinyurl.com/yavn3sao

def SortSameGpa():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 9.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.4,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 4.8, ['Software', 'Materials', 'Civil']})
    Equal(sort(readFile),({'patelh' , 'Harsh', 'Patel', 'male',  10.4,  ['Software', 'Chemical', 'EngPhys']},{'bradenm',  'Matthew', 'Braden', 'male', 9.0,  ['Software', 'Mechanical', 'Civil'] },{'barriosm', 'Michael', 'Barrios', 'male', 4.8, ['Software', 'Materials', 'Civil']}),
    "Sorting in descending order")
SortSameGpa()

def CalculatingMaleAvg():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 9.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']})
    Equal(average(readFile, "male"), 8.0, "Calculating male Average")
CalculatingMaleAvg()

def readStdntsTest():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 9.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']})
    Equal(readFile, [{'bradenm',  'Matthew', 'Braden', 'male', 9.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']}], "Checking if readStdnts works")
readStdntsTest()

def readFreeChoiceTest():
    readFile = readFreeChoice('bradenm',
                              'patelh')
    Equal(readFile, ['bradenm', 'patelh'] , "This is to test if the read free choice function works")
readFreeChoiceTest()

def readDepartmentsTest():
    readFile = readDeptCapacity({'Civil', '50',  'Chemical', '60', 'Electrical', '80', 'Mechanical', '75',  'Software', '90', 'Materials', '50', 'EngPhys', '60'})
    Equal(readFile, {'Civil': 50, 'Chemical': 60, 'Electrical': 80, 'Mechanical': 75, 'Software': 90, 'Materials': 50, 'EngPhys': 60}, "This is to test the readDeptCapacity")
readDepartmentsTest()

def noAverage():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 9.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']})
    Equal(average(readFile, "female"), 0, "Calculating female average with no females")
noAverage()

def Allocating():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 9.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']})
    readFree = readFreeChoice('bradenm','patelh')
    readDept = readDeptCapacity({'Civil', '3',  'Chemical', '2', 'Electrical', '3', 'Mechanical', '1',  'Software', '2', 'Materials', '2', 'EngPhys', '1'})
    Equal(allocate(readFile, readFree, readDept), {'Civil': [], 'Chemical': [], 'Electrical': [], 'Mechanical': [], 'Software': [{'macid': 'bradenm', 'fname': 'Matthew', 'lname': 'Braden', 'gender': 'male', 'gpa': 9.0, 'choices': ['Software', 'Mechanical', 'Civil']}, {'macid': 'patelh', 'fname': 'Harsh', 'lname': 'Patel', 'gender': 'male', 'gpa': 10.0, 'choices': ['Software', 'Chemical', 'EngPhys']},'Materials': [{'macid': 'barriosm', 'fname': 'Michael', 'lname': 'Barrios', 'gender': 'male', 'gpa': 5.0, 'choices': ['Software', 'Materials', 'Civil']}], 'EngPhys': []}, "Allocates the data")
Allocating()

def SortTwoEquals():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 10.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']})
    Equal(sort(readFile),{'bradenm',  'Matthew', 'Braden', 'male', 10.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  10.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']}, "This sorts two students with equal gpa")
SortTwoEquals()

def FemaleWithWrongSpell():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 10.0,  ['Software', 'Mechanical', 'Civil'] },
    {'browniea' , 'Alexandra', 'Brownie', 'Female',  10.0,  ['Software', 'Chemical', 'EngPhys']},
    {'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']})
    Equal(average(readFile, "female"), 0, "This test is for wrong spelling in genders")
FemaleWithWrongSpell()

def AllocateWith3GPA():
    readFile = readStdnts({'bradenm',  'Matthew', 'Braden', 'male', 10.0,  ['Software', 'Mechanical', 'Civil'] },{'patelh' , 'Harsh', 'Patel', 'male',  3.0,  ['Software', 'Chemical', 'EngPhys']},{'barriosm', 'Michael', 'Barrios', 'male', 5.0, ['Software', 'Materials', 'Civil']})
    readFree = readFreeChoice('bradenm', 'patelh')
    readDept = readDeptCapacity({'Civil', '3',  'Chemical', '2', 'Electrical', '3', 'Mechanical', '1',  'Software', '2', 'Materials', '2', 'EngPhys', '1'})
    Equal(allocate(readFile, readFree, readDept), {'Civil': [], 'Chemical': [], 'Electrical': [], 'Mechanical': [], 'Software': [{'macid': 'bradenm', 'fname': 'Matthew', 'lname': 'Braden', 'gender': 'male', 'gpa': 10.0, 'choices': ['Software', 'Mechanical', 'Civil']},'Software': [{'macid': 'barriosm', 'fname': 'Michael', 'lname': 'Barrios', 'gender': 'male', 'gpa': 5.0, 'choices': ['Software', 'Materials', 'Civil']}], 'EngPhys': []}, "Allocates the data")
AllocateWith3GPA()
