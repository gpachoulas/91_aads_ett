menuOptions = ['Load data', 'Solve Problem', 'Exit']
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
    selectedOption = input()
    if selectedOption == str(len(files) + 1):
        printMainMenu()
    else:
        print('Selected data: ' + files[int(selectedOption) - 1].split('\\')[1])
        mainFunctions.readFile(files[int(selectedOption) - 1])
        mainFunctions.problemInfo()
        input("Press Enter to continue...")


def solveProblem():
    mainFunctions.colorGraph()


def exit():
    import sys
    sys.exit()


def selectOption(selectedOption):
    switcher = {
        1: loadData,
        2: solveProblem,
        3: exit
    }
    func = switcher.get(int(selectedOption), lambda: 'Invalid')
    return func()


if __name__ == '__main__':
    while (True):
        printMainMenu()
        selectedOption = input()
        selectOption(selectedOption)
