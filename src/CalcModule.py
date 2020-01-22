## @file CalcModule.py
#  @brief Preforms calculations on modules
#  @author Matthew Braden
#  @date 1/17/2019
from ReadAllocationData import *
## @brief Sorts students data
#  @details Sorts the students in reverse order
#  @param S List of the dictionaries from readStdnts
def sort(S):
    sortList = sorted(S, key = lambda i: i["gpa"], reverse = True)
    return sortList
#sorted line 10 was found from https://tinyurl.com/y9xdx4ep

## @brief Average of students data
#  @details Calculates the average of each genders gpa's
#  @param L List of the dictionaries from readStdnts
#  @param g Students gender
def average(L, g):
    maleStudents = 0
    femaleStudents = 0
    maleSum = 0
    femaleSum = 0
    for i in L:
        if (i["gender"] == "male"):
            maleStudents += 1
            maleSum += i["gpa"]
        else:
            femaleStudents += 1
            femaleSum += i["gpa"]
    if (g == "male"):
        return maleSum / maleStudents
    else:
        return femaleSum / femaleStudents



## @brief Allocates students
#  @details Sorts students into their selected choice of programs
#  @param S List of the dictionaries from readStdnts
#  @param F List of the dictionaries from readFreeChoice
#  @param C List of the dictionaries from readDeptCapacity
def allocate(S, F, C):
    allocations = {
    }
    Civil = 0
    Chemical = 0
    Electrical = 0
    Mechanical = 0
    Software = 0
    Materials = 0
    EngPhys = 0

    CivLst = []
    ChemLst = []
    ElecLst = []
    MechLst = []
    SoftLst = []
    MatLst = []
    PhysLst = []

    totalCiv = C["Civil"]
    totalChem = C["Chemical"]
    totalElec = C["Electrical"]
    totalMech = C["Mechanical"]
    totalSoft = C["Software"]
    totalMat = C["Materials"]
    totalPhys = C["EngPhys"]

    for i in S:
        if (i["gpa"] >= 4.0):
            for j in F:
                if (i["macid"] == j):
                    if (i["choices"][0] == "Civil"):
                        CivLst.append(i)
                        Civil += 1
                    elif (i["choices"][0] == "Chemical"):
                        ChemLst.append(i)
                        Chemical += 1
                    elif (i["choices"][0] == "Electrical"):
                        ElecLst.append(i)
                        Electrical += 1
                    elif (i["choices"][0] == "Mechanical"):
                        MechLst.append(i)
                        Mechanical += 1
                    elif (i["choices"][0] == "Software"):
                        SoftLst.append(i)
                        Software += 1
                    elif (i["choices"][0] == "Materials"):
                        MatLst.append(i)
                        Materials += 1
                    elif (i["choices"][0] == "EngPhys"):
                        PhysLst.append(i)
                        EngPhys += 1
            for k in F:
                if (i["macid"] != k):
                    for choice in i["choices"]:
                        if ((choice == "Civil") and (Civil != totalCiv)):
                            CivLst.append(i)
                            Civil += 1
                            break
                        elif ((choice == "Chemical") and (Chemical != totalChem)):
                            ChemLst.append(i)
                            Chemical += 1
                            break
                        elif ((choice == "Electrical") and (Electrical != totalElec)):
                            ElecLst.append(i)
                            Electrical += 1
                            break
                        elif ((choice == "Mechanical") and (Mechanical != totalMech)):
                            MechLst.append(i)
                            Mechanical += 1
                            break
                        elif ((choice == "Software") and (Software != totalSoft)):
                            SoftLst.append(i)
                            Software += 1
                            break
                        elif ((choice == "Materials") and (Materials != totalMat)):
                            MatLst.append(i)
                            Materials += 1
                            break
                        elif ((choice == "EngPhys") and (EngPhys != totalPhys)):
                            PhysLst.append(i)
                            EngPhys += 1
                            break

    allocations["Civil"] = CivLst
    allocations["Chemical"] = ChemLst
    allocations["Electrical"] = ElecLst
    allocations["Mechanical"] = MechLst
    allocations["Software"] = SoftLst
    allocations["Materials"] = MatLst
    allocations["EngPhys"] = PhysLst
    return allocations
