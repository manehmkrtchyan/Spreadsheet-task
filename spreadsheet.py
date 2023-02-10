from numpy import full
from cell import Cell

class Spreadsheet:
    def __init__(self, row, col):
        self.spreadsheet = full((row, col), Cell())

    def setCellAt(self, row, col, cell):
        self.spreadsheet[row][col] = cell

    def getCellAt(self, row, col):
        return self.spreadsheet[row][col]
    
    def addRow(self, idx):
        newls = list(self.spreadsheet)
        newls.insert(idx, [Cell()]*self.col)
        self.spreadsheet = newls
        
    def removeRow(self, idx):
        newls = (list(self.spreadsheet))
        newls.pop(idx)
        self.spreadsheet = newls
        
    def addColumn(self, idx):
        new = []
        lst = list(self.spreadsheet)
        for i in lst:
            ls = list(i)
            ls.insert(idx, Cell())
            new.append(ls)
        self.spreadsheet = new
    
    def removeColumn(self, idx):
        new = []
        lst = list(self.spreadsheet)
        for i in lst:
            ls = list(i)
            ls.pop(idx)
            new.append(ls)
        self.spreadsheet = new
    
    def swapRows(self, idx1, idx2):
        tmp1 = list(self.spreadsheet)[idx1]
        tmp2 = list(self.spreadsheet)[idx2]
        self.removeRow(idx1)
        self.addRow(idx2)
        self.removeRow(idx2) 
        self.addRow(idx1)

    def swapColumn(self, idx1, idx2):
        tmp1 = list(self.spreadsheet)[idx1]
        tmp2 = list(self.spreadsheet)[idx2]
        self.removeColumn(idx1)
        self.addColumn(idx2)
        self.removeColumn(idx2) 
        self.addColumn(idx1)