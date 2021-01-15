import itertools
import warnings
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning)

currentProblem = {}  # Dictionary key,value ==> examCode, [array of students]


def readFile(filename):
    fileHandle = open(filename, "r")
    lineList = fileHandle.read().splitlines()
    fileHandle.close()
    for student in range(len(lineList)):
        examsList = lineList[student].rstrip().split()
        for examcode in examsList:
            if examcode not in currentProblem.keys():
                currentProblem[str(examcode)] = [
                    student + 1]  # Επειδή η αρίθμηση ξεκινάει απο 0 προσθέτουμε + 1 για να δείχνουμε σωστά την θέση του φοιτητή
            else:
                currentProblem[str(examcode)].append(
                    student + 1)  # Επειδή η αρίθμηση ξεκινάει απο 0 προσθέτουμε + 1 για να δείχνουμε σωστά την θέση του φοιτητή
    problemInfo(currentProblem)


def confiltTable(currentProblem):
    entries = [item for sublist in currentProblem.values() for item in sublist]
    pairs = []
    data = pd.DataFrame(0, index=currentProblem.keys(), columns=currentProblem.keys())
    for i in set(entries):
        temp = []
        for key, values in currentProblem.items():
            if i in values:
                temp.append(key)
        pairs.append(temp)
    pairs = [x for x in pairs if len(x) > 1]
    for i in pairs:
        for pair in itertools.permutations(i, r=2):  # get all possible pairs example (1,2) and (2,1)
            data.loc[[str(pair[0])], [str(pair[1])]] = 1
    return data


def problemInfo(currentProblem):
    entries = [item for sublist in currentProblem.values() for item in sublist]
    data = confiltTable(currentProblem)
    density = float(data.values.sum()) / float(data.size)
    print(greedyAlgorith(data))
    print('Problem info:')
    results = {'exams': len(currentProblem.keys()), 'students': len(set(entries)), 'entries': len(entries),
               'density': ("%.2f" % density)}
    print(results)


def show_graph_with_labels(adjacency_matrix):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    graph = nx.Graph()
    graph.add_edges_from(edges)
    d = nx.coloring.greedy_color(graph, strategy="largest_first")
    print(d)
    # nx.draw(gr, node_size=500)
    # plt.show()


def greedyAlgorith(data):
    s = data.to_numpy()
    show_graph_with_labels(s)


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
# readFile('../datasheets/problems/kfu-s-93.stu')
# print("--- %s seconds ---" % (time.time() - start_time))
# print(str(datetime.timedelta(seconds=time.time() - start_time)))

# elist = [(10, 20, 5.0), (10, 40, 3.0)]
# G = nx.Graph()
# G.add_weighted_edges_from(elist)
# d = nx.coloring.greedy_color(G, strategy="largest_first")
# nx.draw(G)
# print(d)
# plt.show()

