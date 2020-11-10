import itertools
import warnings
import pandas as pd

import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)


def readFile(filename):
    fileHandle = open(filename, "r")
    lineList = fileHandle.read().splitlines()
    fileHandle.close()
    counter = 0
    courses = np.array([])
    for line in lineList:
        lineArray = line.rstrip().split()
        for i in lineArray:
            counter = counter + 1
            if i not in courses:
                courses = np.append(courses, [i], axis=0)
    density = conflictTable(lineList, courses)
    results = {'exams': len(courses), 'entries': counter, 'students': len(lineList) - 1, 'density': density}
    print(results)
    return results


def conflictTable(linelist, courses):
    data = pd.DataFrame(0, index=courses.tolist(), columns=courses.tolist())
    for line in linelist:
        lineArray = line.rstrip().split()
        for pair in itertools.permutations(lineArray, r=2):  # get all possible pairs
            data.loc[[str(pair[0])], [str(pair[1])]] = 1
    density = float(data.values.sum()) / float(data.size)
    # print("%.2f" % density)
    return ("%.2f" % density)


readFile('../datasheets/rye-s-93.stu')
