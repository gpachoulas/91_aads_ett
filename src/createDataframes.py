import itertools
import warnings
import pandas as pd
import networkx as nx
import animation
import glob

warnings.simplefilter(action='ignore', category=FutureWarning)

currentProblem = {}
wait = animation.Wait()


def readFile(filename):
    currentProblem['filename'] = (filename.split('\\')[1]).split('.')[0]
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
    # problemInfo()
    # colorGraph()


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


def calculateCost(solutionDict, pairs):
    sum = 0
    for i in pairs:
        for pair in itertools.combinations(i, r=2):  # get all possible pairs example (1,2) and (2,1)
            difference = abs(solutionDict.get(int(pair[0].lstrip('0'))) - solutionDict.get(
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
    return (sum / len(set(currentProblem['entries'])))


def colorGraph():
    if ('conflictsTable' not in currentProblem.keys()):
        print('No data selected')
        return
    data = pd.DataFrame.from_dict(currentProblem['conflictsTable'])
    data = data.to_dict()
    edges = []
    wait.start()
    for key, value in data.items():
        for insidekey, insidevalue in value.items():
            if insidevalue == 1:
                edges.append(tuple((int(insidekey), int(key))))
    graph = nx.Graph()
    graph.add_edges_from(edges)
    solution = nx.coloring.greedy_color(graph, strategy="smallest_last")
    currentProblem['solution'] = solution
    currentProblem['solutionCost'] = calculateCost(currentProblem['solution'], currentProblem['pairs'])
    wait.stop()
    periodsUsed = len(set(currentProblem['solution'].values()))
    print("\n Periods: " + str(periodsUsed) + ", Cost of solution: %.2f" % currentProblem['solutionCost'])
    exportSolution()
    # nx.draw(graph, with_labels=True, node_size=5, font_weight='bold')
    # plt.show()


def exportSolution():
    data = pd.DataFrame(list(currentProblem['solution'].items()), columns=['Lesson', 'Period'])
    data['Lesson'] = data['Lesson'].apply(str).str.zfill(4)
    cost = "{:.2f}".format(currentProblem['solutionCost'])
    data.to_csv('mySolutions/' + currentProblem['filename'] + '(' + cost + ').csv', index=False, sep=' ',
                header=False)


def checkSolution():
    if ('pairs' not in currentProblem.keys()):
        print('No data selected')
        return
    if ('solution' not in currentProblem.keys()):
        print('Please solve the problem first')
        return
    files = []
    for file in glob.glob("datasheets/solutions/" + currentProblem['filename'] + "*.sol"):
        files.append(file)
    data = pd.read_csv("datasheets/solutions/" + files[0].split('\\')[1], sep='\t', names=['Courses', 'Period'],
                       header=None)
    # data['Courses'] = data['Courses'].apply(str).str.zfill(4)
    data = dict(zip(data['Courses'].values.tolist(), data['Period'].values.tolist()))
    courses = set(data.keys())
    periods = len(set(data.values()))
    costs = calculateCost(data, currentProblem['pairs'])
    if courses == set(currentProblem['solution'].keys()):
        print('Courses is correct')
    else:
        print('Courses is not correct')
    conflicts = 0
    for i in currentProblem['pairs']:
        for pair in itertools.combinations(i, r=2):  # get all possible pairs example (1,2) and (2,1)
            difference = abs(data.get(int(pair[0].lstrip('0'))) - data.get(
                int(pair[1].lstrip('0'))))
            if difference == 0:
                conflicts = conflicts + 1
    if conflicts == 0:
        print('No conflicts detected')
    else:
        print('Conflicts detected')


def getCurrentProblem():
    return currentProblem


def solveAll():
    files = []
    for file in glob.glob("datasheets/problems/*.stu"):
        files.append(file)
    for file in files:
        readFile(file)
        confiltTable()
        colorGraph()
# start_time = time.time()
# readFile('../datasheets/problems/kfu-s-93.stu')
# print("--- %s seconds ---" % (time.time() - start_time))
# print(str(datetime.timedelta(seconds=time.time() - start_time)))

# readFile("../datasheets/problems/sta-f-83.stu")
# checkSolution()
# solveAll()
