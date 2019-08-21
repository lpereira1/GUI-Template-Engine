import fileinput


print("Text to search for:")
textToSearch = input("> ")

print("Text to replace it with:")
textToReplace = input("> ")

print("File to perform Search-Replace on:")
fileToSearch = input("> ")


def filereplace(filename, searchvarible, replacementtext):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(searchvarible, replacementtext), end='')
filereplace(fileToSearch, textToSearch, textToReplace)