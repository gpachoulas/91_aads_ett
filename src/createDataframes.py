import itertools
import warnings
import pandas as pd
import time

import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)

currentProblem = {}


def readFile(filename):
    fileHandle = open(filename, "r")
    lineList = fileHandle.read().splitlines()
    fileHandle.close()
    for student in range(len(lineList)):
        examsList = lineList[student].rstrip().split()
        for examcode in examsList:
            if examcode not in currentProblem.keys():
                currentProblem[str(examcode)] = [student + 0]
            else:
                currentProblem[str(examcode)].append(student + 0)
    problemInfo(lineList, currentProblem.keys())


def conflictTable(linelist, courses):
    data = pd.DataFrame(0, index=courses, columns=courses)
    for line in linelist:
        lineArray = line.rstrip().split()
        for pair in itertools.permutations(lineArray, r=2):  # get all possible pairs
            data.loc[[str(pair[0])], [str(pair[1])]] = 1
    density = float(data.values.sum()) / float(data.size)
    return ("%.2f" % density)


def problemInfo(lineList, courses):
    density = conflictTable(lineList, courses)
    print('Problem info:')
    results = {'exams': len(courses), 'entries': len(courses), 'students': len(lineList)-1, 'density': density}
    print(results)


# def readFile(filename):
#     fileHandle = open(filename, "r")
#     lineList = fileHandle.read().splitlines()
#     fileHandle.close()
#     counter = 0
#     courses = np.array([])
#     for line in lineList:
#         lineArray = line.rstrip().split()
#         for i in lineArray:
#             counter = counter + 1
#             if i not in courses:
#                 courses = np.append(courses, [i], axis=0)
#     density = conflictTable(lineList, courses)
#     results = {'exams': len(courses), 'entries': counter, 'students': len(lineList), 'density': density}
#     print(results)
#     return results

start_time = time.time()
readFile('../datasheets/pur-s-93.stu')
print("--- %s seconds ---" % (time.time() - start_time))
