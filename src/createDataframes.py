import itertools
import warnings
import pandas as pd
import networkx as nx
import animation

warnings.simplefilter(action='ignore', category=FutureWarning)

currentProblem = {}
wait = animation.Wait()


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
    if ('dataProblem' not in currentProblem.keys()):
        print('Error in reading of data')
        return
    wait.start()
    confiltTable()
    wait.stop()
    data = pd.DataFrame.from_dict(currentProblem['conflictsTable'])
    density = float(data.values.sum()) / float(data.size)
    print('Problem info:')
    results = {'Exams': len(currentProblem['dataProblem'].keys()), 'Students': len(set(currentProblem['entries'])),
               'Entries': len(currentProblem['entries']),
               'Density': ("%.2f" % density)}
    print(results)


def calculateCost():
    sum = 0
    costTable = [0, 16, 8, 4, 2, 1]
    for i in currentProblem['pairs']:
        for pair in itertools.combinations(i, r=2):  # get all possible pairs example (1,2) and (2,1)
            difference = abs(currentProblem['solution'].get(int(pair[0].lstrip('0'))) - currentProblem['solution'].get(
                int(pair[1].lstrip('0'))))
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
    # print(sum / len(set(currentProblem['entries'])))
    currentProblem['solutionCost'] = sum / len(set(currentProblem['entries']))
    print("\n Cost of solution %.2f" % currentProblem['solutionCost'])


def colorGraph():
    if ('conflictsTable' not in currentProblem.keys()):
        print('No data selected')
        return
    data = pd.DataFrame.from_dict(currentProblem['conflictsTable'])
    data = data.to_dict()
    edges = []
    print('Creating solution')
    wait.start()
    for key, value in data.items():
        for insidekey, insidevalue in value.items():
            if insidevalue == 1:
                edges.append(tuple((int(insidekey), int(key))))
    graph = nx.Graph()
    graph.add_edges_from(edges)
    solution = nx.coloring.greedy_color(graph, strategy="smallest_last")
    wait.stop()
    print('Solution Created...')
    print('Calculating cost of solution')
    currentProblem['solution'] = solution
    wait.start()
    calculateCost()
    wait.stop()
    # nx.draw(graph, with_labels=True, node_size=5, font_weight='bold')
    # plt.show()

# start_time = time.time()
# readFile('../datasheets/problems/kfu-s-93.stu')
# print("--- %s seconds ---" % (time.time() - start_time))
# print(str(datetime.timedelta(seconds=time.time() - start_time)))

# readFile("../datasheets/problems/lse-f-91.stu")
