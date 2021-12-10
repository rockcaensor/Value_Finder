import os
filename = "D:\\Vivado_Projects\\IP_SRC\\IP_SRC.xpr"
directory = "D:\\Vivado_Projects\\IP_SRC"
FileList = []
filepath = ""

def compare(file_0, file_1):
    filename = [0, 0]
    filename[0] = file_0
    filename[1] = file_1

    lines = [0, 0]

    for i in range(2):
        file = open(filename[i], encoding="utf8", errors='ignore')
        lines[i] = file.readlines() # export lines to list "lines"
        file.close()

    for i in range (len(lines[0])):
        if lines[0][i] != lines[1][i]:
            continue
        else:
            continue
        """  print("\n\n\nLine ", i)
            print(lines[0][i])
            print(lines[1][i])"""
            

def FindInFile(filename, SearchingPart):
    lines = []
    IsFinded = False
    file = open(filename, encoding="utf8", errors='ignore' )
    lines = file.readlines() # export lines to list "lines"
    for i in range(len(lines)):
        if lines[i].find(SearchingPart) == -1:
            continue
        else:
            IsFinded = True
            print("\n"*4) 
            print(filename) 
            print(lines[i].find(SearchingPart))
            print(lines[i])
    return IsFinded


def FindInDirectory(directory, SearchingPart):
    FileList = []
    filepath = ""
    FindedFiles = []

    for root, dirs, files in os.walk(directory):
        for fl in files:
            filepath = str(root) + "\\" +str(fl)
            FileList.append(filepath)

    for fls in FileList:
        try:
            if FindInFile(fls, SearchingPart) == False:
                continue
            else:
                FindedFiles.append(fls)      
        except UnicodeDecodeError:
            print(fls)
        else:
            continue    
            

    return FindedFiles

   