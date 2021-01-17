import itertools
import warnings
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from netwulf import visualize

warnings.simplefilter(action='ignore', category=FutureWarning)

currentProblem = {}


def readFile(filename):
    dataProblem = {}  # Dictionary key,value ==> examCode, [array of students]
    fileHandle = open(filename, "r")
    lineList = fileHandle.read().splitlines()
    fileHandle.close()
    for student in range(len(lineList)):
        examsList = lineList[student].rstrip().split()
        for examcode in examsList:
            if examcode not in dataProblem.keys():
                dataProblem[str(examcode)] = [
                    student + 1]  # Επειδή η αρίθμηση ξεκινάει απο 0 προσθέτουμε + 1 για να δείχνουμε σωστά την θέση του φοιτητή
            else:
                dataProblem[str(examcode)].append(
                    student + 1)  # Επειδή η αρίθμηση ξεκινάει απο 0 προσθέτουμε + 1 για να δείχνουμε σωστά την θέση του φοιτητή
    currentProblem['dataProblem'] = dataProblem
    problemInfo()
    # print(currentProblem)


def confiltTable():
    entries = [item for sublist in currentProblem['dataProblem'].values() for item in sublist]
    currentProblem['entries'] = entries
    pairs = []
    data = pd.DataFrame(0, index=currentProblem['dataProblem'].keys(), columns=currentProblem['dataProblem'].keys())
    for i in set(entries):
        temp = []
        for key, values in currentProblem['dataProblem'].items():
            if i in values:
                temp.append(key)
        pairs.append(temp)
    pairs = [x for x in pairs if len(x) > 1]
    currentProblem['pairs'] = pairs
    for i in pairs:
        for pair in itertools.permutations(i, r=2):  # get all possible pairs example (1,2) and (2,1)
            data.loc[[str(pair[0])], [str(pair[1])]] = 1
    currentProblem['conflictsTable'] = data.to_dict()


def problemInfo():
    confiltTable()
    data = pd.DataFrame.from_dict(currentProblem['conflictsTable'])
    density = float(data.values.sum()) / float(data.size)
    colorGraph()
    # print('Problem info:')
    # results = {'exams': len(currentProblem['dataProblem'].keys()), 'students': len(set(currentProblem['entries'])),
    #            'entries': len(currentProblem['entries']),
    #            'density': ("%.2f" % density)}
    # print(results)


def calculateCost():
    sum = 0
    costTable = [0, 16, 8, 4, 2, 1]
    for i in currentProblem['pairs']:
        for pair in itertools.combinations(i, r=2):  # get all possible pairs example (1,2) and (2,1)
            difference = abs(currentProblem['solution'].get(int(pair[0].lstrip('0'))) - currentProblem['solution'].get(
                int(pair[1].lstrip('0'))))
            print(difference)
            if difference == 1:
                sum = sum + 16
            elif difference == 2:
                sum = sum + 8
            elif difference == 3:
                sum = sum + 4
            elif difference == 4:
                sum = sum + 2
            elif difference == 5:
                sum = sum + 1
    print(sum / len(set(currentProblem['entries'])))


def colorGraph():
    correctSolutions = {}
    s = pd.DataFrame.from_dict(currentProblem['conflictsTable']).to_numpy()
    rows, cols = np.where(s == 1)
    edges = zip(rows.tolist(), cols.tolist())
    graph = nx.Graph()
    graph.add_edges_from(edges)
    solution = nx.coloring.greedy_color(graph, strategy="smallest_last")
    for key, value in solution.items():
        correctSolutions[key + 1] = value
    currentProblem['solution'] = correctSolutions
    calculateCost()
    # nx.draw(graph, with_labels=True, node_size=5, font_weight='bold')
    # plt.show()
    # visualize(d)


# start_time = time.time()
# readFile('../datasheets/problems/kfu-s-93.stu')
# print("--- %s seconds ---" % (time.time() - start_time))
# print(str(datetime.timedelta(seconds=time.time() - start_time)))

readFile("../datasheets/problems/lse-f-91.stu")
