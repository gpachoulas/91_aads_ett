import itertools
import warnings
import pandas as pd

import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)

currentProblem = {}


def readFile(filename):
    fileHandle = open(filename, "r")
    lineList = fileHandle.read().splitlines()
    fileHandle.close()
    print(lineList)
    for student in range(len(lineList)):
        examsList = lineList[student].rstrip().split()
        for examcode in examsList:
            if examcode not in currentProblem.keys():
                currentProblem[str(examcode)] = [student + 1]
            else:
                currentProblem[str(examcode)].append(student + 1)
    print(currentProblem)


readFile('datasheets/car-f-92.stu')
