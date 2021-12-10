import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from gui import Ui_MainWindow
from FileCompare import *

class MainApp(QMainWindow, Ui_MainWindow):

    InputSearch = ''
    directory = ''

    def __init__ (self):
        super().__init__() 
        self.UIRender()

    def UIRender(self):
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.BrowseButton.clicked.connect(self.browse_folder)
        self.ui.SearchButton.clicked.connect(self.DirFind)
        self.show()

    def DirFind(self):
        self.ui.LogWindow.addItem("Searching. Please wait...")   
        self.InputSearch = self.ui.SearchInput.toPlainText()            
        self.FindInDirectory(self.directory, self.InputSearch)
        self.ui.LogWindow.addItem("Done")

    def browse_folder(self):
        self.ui.FolderView.clear()        
        self.directory = QFileDialog.getExistingDirectory(self, "Выберите папку")

        if self.directory:
            self.ui.FolderView.addItem(self.directory)

    def compare(self, file_0, file_1):
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
                

    def FindInFile(self, filename, SearchingPart):        
        lines = []
        IsFinded = False
        file = open(filename, encoding="utf8", errors='ignore' )
        lines = file.readlines() # export lines to list "lines"
        for i in range(len(lines)):
            if lines[i].find(SearchingPart) == -1:
                continue
            else:
                IsFinded = True
                self.ui.LogWindow.addItem("\n")                
                self.ui.LogWindow.addItem(filename) 
                val = lines[i].find(SearchingPart)
                self.ui.LogWindow.addItem(str(val))
                self.ui.LogWindow.addItem(str(lines[i]))
        return IsFinded


    def FindInDirectory(self, directory, SearchingPart):
        FileList = []
        filepath = ""
        FindedFiles = []

        for root, dirs, files in os.walk(directory):
            for fl in files:
                filepath = str(root) + "\\" +str(fl)
                FileList.append(filepath)

        for fls in FileList:
            try:
                if self.FindInFile(fls, SearchingPart) == False:
                    continue
                else:
                    FindedFiles.append(fls)      
            except UnicodeDecodeError:
                self.ui.LogWindow.addItem(fls)
            else:
                continue    
                

        return FindedFiles        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec_())
