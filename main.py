menuOptions = ['Load data', 'Solve Problem', 'Check predefined solution', 'Solve all', 'Exit']
import src.createDataframes as mainFunctions


def printMainMenu():
    print("Select one option")
    for option in range(len(menuOptions)):
        print('[' + str(option + 1) + ']' + ' ' + menuOptions[option])


def loadData():
    import glob
    files = []
    for file in glob.glob("datasheets/problems/*.stu"):
        files.append(file)
    for file in range(len(files)):
        print('[' + str(file + 1) + ']' + ' ' + files[file].split('\\')[1])
    print('[' + str(len(files) + 1) + ']' + ' ' + 'Return to menu')
    selectedOption = input('Select file: \n')
    if selectedOption == str(len(files) + 1):
        printMainMenu()
    else:
        print('|||||||||||||Results||||||||||||||')
        print('Selected data: ' + files[int(selectedOption) - 1].split('\\')[1])
        mainFunctions.readFile(files[int(selectedOption) - 1])
        mainFunctions.problemInfo()
        print('||||||||||||||||||||||||||||||||||')
        input("Press Enter to continue...")



def solveProblem():
    print('|||||||||||||Results||||||||||||||')
    mainFunctions.colorGraph()
    print('||||||||||||||||||||||||||||||||||')


def checkPredefinedSolution():
    print('|||||||||||||Results||||||||||||||')
    mainFunctions.checkSolution()
    print('||||||||||||||||||||||||||||||||||')


def exit():
    import sys
    sys.exit()

def solveAllProblems():
    print('|||||||||||||Results||||||||||||||')
    mainFunctions.solveAll()
    print('||||||||||||||||||||||||||||||||||')

def selectOption(selectedOption):
    switcher = {
        1: loadData,
        2: solveProblem,
        3: checkPredefinedSolution,
        4: solveAllProblems,
        5: exit
    }
    func = switcher.get(int(selectedOption), lambda: 'Invalid')
    return func()


if __name__ == '__main__':
    while (True):
        printMainMenu()
        selectedOption = input()
        selectOption(selectedOption)
