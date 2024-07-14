import os
import time

dirPath = 'C:/Users/kostas/Documents/pythonForGithub/TestFolder'
down = '|'

def printFolders(path, indent=0):
    dirList = os.listdir(path)
    for i, entry in enumerate(dirList):
        fullPath = createFullPath(path, entry)
        
        # Print current file or directory prefixed with indentation
        print(' ' * indent + entry)
        time.sleep(0.2)
        # If it's a directory, recurse into it
        if os.path.isdir(fullPath):
            print(' ' * indent + down)  # Only print down if it's a directory
            printFolders(fullPath, indent + 4)  # Increase indent for the next level
        elif i < len(dirList) - 1:
            print(' ' * indent + down)

# Creates the full path of each entry
def createFullPath(directoryPath, entry):
    return os.path.join(directoryPath, entry)

printFolders(dirPath)