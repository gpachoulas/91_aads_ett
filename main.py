menuOptions = ['Load data', 'Check solution', 'Exit']
import src.createDataframes as test


def printMainMenu():
    print("Select one option")
    for option in range(len(menuOptions)):
        print('[' + str(option + 1) + ']' + ' ' + menuOptions[option])


def loadData():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    import glob
    os.chdir("datasheets/problems/")
    files = []
    for file in glob.glob("*.stu"):
        files.append(file)
    for file in range(len(files)):
        print('[' + str(file + 1) + ']' + ' ' + files[file])
    print('[' + str(len(files) + 1) + ']' + ' ' + 'Return to menu')
    selectedOption = input()
    if selectedOption == str(len(files) + 1):
        printMainMenu()
    else:
        print(files[int(selectedOption) - 1])
        test.readFile(files[int(selectedOption) - 1])
        printMainMenu()


def two():
    print('tete')


def exit():
    import sys
    sys.exit()


def selectOption(selectedOption):
    switcher = {
        1: loadData,
        2: two,
        3: exit
    }
    func = switcher.get(int(selectedOption), lambda: 'Invalid')
    return func()


if __name__ == '__main__':
    # while (True):
    printMainMenu()
    selectedOption = input()
    selectOption(selectedOption)
