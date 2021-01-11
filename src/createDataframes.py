import itertools
import warnings
import pandas as pd
import time
import datetime
import networkx as nx
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning)

currentProblem = {}  # Dictionary key,value ==> examCode, [array of students]


def readFile(filename):
    fileHandle = open(filename, "r")
    lineList = fileHandle.read().splitlines()
    fileHandle.close()
    entries = 0
    for student in range(len(lineList)):
        examsList = lineList[student].rstrip().split()
        for examcode in examsList:
            entries = entries + 1
            if examcode not in currentProblem.keys():
                currentProblem[str(examcode)] = [
                    student + 1]  # Επειδή η αρίθμηση ξεκινάει απο 0 προσθέτουμε + 1 για να δείχνουμε σωστά την θέση του φοιτητή
            else:
                currentProblem[str(examcode)].append(
                    student + 1)  # Επειδή η αρίθμηση ξεκινάει απο 0 προσθέτουμε + 1 για να δείχνουμε σωστά την θέση του φοιτητή
    print(currentProblem)
    problemInfo(lineList, currentProblem.keys(), entries)

    # ###############example of NetworkX lib######################
    # print(currentProblem)
    # g = nx.DiGraph(currentProblem)
    # d = nx.coloring.greedy_color(g, strategy="largest_first")
    # print(d)
    # ###############example of NetworkX lib######################


def conflictTable(linelist, courses):
    data = pd.DataFrame(0, index=courses,
                        columns=courses)  # Δημιουργώ ένα dataframe μηδενικό με γραμμές και στήλες όσες είναι τα μαθήματα
    for line in linelist:
        lineArray = line.rstrip().split()
        for pair in itertools.permutations(lineArray, r=2):  # get all possible pairs example (1,2) and (2,1)
            data.loc[[str(pair[0])], [str(pair[1])]] = 1
    density = float(data.values.sum()) / float(data.size)
    print(data.to_string())
    return ("%.2f" % density)


def problemInfo(lineList, courses, entries):
    density = conflictTable(lineList, courses)
    print('Problem info:')
    results = {'exams': len(courses), 'students': len(lineList), 'entries': entries, 'density': density}
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

# start_time = time.time()
# readFile('../datasheets/problems/car-f-92.stu')
# print("--- %s seconds ---" % (time.time() - start_time))
# print(str(datetime.timedelta(seconds=time.time() - start_time)))

elist = [(10, 20, 5.0), (10, 40, 3.0)]
G = nx.Graph()
G.add_weighted_edges_from(elist)
d = nx.coloring.greedy_color(G, strategy="largest_first")
nx.draw(G)
print(d)
plt.show()
