import numpy as np
import random


class SudokuCreate:
    def __init__(self, sudoku: np.ndarray):
        self.newSudoku = sudoku

    def createNewSudoku(self):
        for i in range(3):
            self.__swapColumn(i)
            self.__swapRow(i)
        for i in range(3):
            self.__swapColumBlock()
            self.__swapRowBlock()
        for i in range(3):
            self.__rotateSudoku()
            self.__flipSudoku()
        for i in range(3):
            self.__swapNumber()
        return self.newSudoku

    # 열 단위 교환
    def __swapColumn(self, loc):
        r = random.randrange(0, 6)
        t1 = list(self.newSudoku[:, loc * 3])
        t2 = list(self.newSudoku[:, loc * 3 + 1])
        t3 = list(self.newSudoku[:, loc * 3 + 2])
        if r == 0:
            return
        elif r == 1:
            self.newSudoku[:, loc * 3 + 1] = t3
            self.newSudoku[:, loc * 3 + 2] = t2
        elif r == 2:
            self.newSudoku[:, loc * 3] = t2
            self.newSudoku[:, loc * 3 + 1] = t1
        elif r == 3:
            self.newSudoku[:, loc * 3] = t2
            self.newSudoku[:, loc * 3 + 1] = t3
            self.newSudoku[:, loc * 3 + 2] = t1
        elif r == 4:
            self.newSudoku[:, loc * 3] = t3
            self.newSudoku[:, loc * 3 + 1] = t1
            self.newSudoku[:, loc * 3 + 2] = t2
        elif r == 5:
            self.newSudoku[:, loc * 3] = t3
            self.newSudoku[:, loc * 3 + 2] = t1

    # 행 단위 교환
    def __swapRow(self, loc):
        r = random.randrange(0, 6)
        t1 = list(self.newSudoku[loc * 3, :])
        t2 = list(self.newSudoku[loc * 3 + 1, :])
        t3 = list(self.newSudoku[loc * 3 + 2, :])
        if r == 0:
            return
        elif r == 1:
            self.newSudoku[loc * 3 + 1, :] = t3
            self.newSudoku[loc * 3 + 2, :] = t2
        elif r == 2:
            self.newSudoku[loc * 3, :] = t2
            self.newSudoku[loc * 3 + 1, :] = t1
        elif r == 3:
            self.newSudoku[loc * 3, :] = t2
            self.newSudoku[loc * 3 + 1, :] = t3
            self.newSudoku[loc * 3 + 2, :] = t1
        elif r == 4:
            self.newSudoku[loc * 3, :] = t3
            self.newSudoku[loc * 3 + 1, :] = t1
            self.newSudoku[loc * 3 + 2, :] = t2
        elif r == 5:
            self.newSudoku[loc * 3, :] = t3
            self.newSudoku[loc * 3 + 2, :] = t1

    # 열 블럭 단위 교환
    def __swapColumBlock(self):
        r = random.randrange(0, 6)
        t1 = self.newSudoku[:, 0:3].copy()
        t2 = self.newSudoku[:, 3:6].copy()
        t3 = self.newSudoku[:, 6:9].copy()
        if r == 0:
            return
        elif r == 1:
            self.newSudoku[:, 3:6] = t3
            self.newSudoku[:, 6:9] = t2
        elif r == 2:
            self.newSudoku[:, 0:3] = t2
            self.newSudoku[:, 3:6] = t1
        elif r == 3:
            self.newSudoku[:, 0:3] = t2
            self.newSudoku[:, 3:6] = t3
            self.newSudoku[:, 6:9] = t1
        elif r == 4:
            self.newSudoku[:, 0:3] = t3
            self.newSudoku[:, 3:6] = t1
            self.newSudoku[:, 6:9] = t2
        elif r == 5:
            self.newSudoku[:, 0:3] = t3
            self.newSudoku[:, 6:9] = t1

    # 행 블럭 단위 교환
    def __swapRowBlock(self):
        r = random.randrange(0, 6)
        t1 = self.newSudoku[0:3, :].copy()
        t2 = self.newSudoku[3:6, :].copy()
        t3 = self.newSudoku[6:9, :].copy()
        if r == 0:
            return
        elif r == 1:
            self.newSudoku[3:6, :] = t3
            self.newSudoku[6:9, :] = t2
        elif r == 2:
            self.newSudoku[0:3, :] = t2
            self.newSudoku[3:6, :] = t1
        elif r == 3:
            self.newSudoku[0:3, :] = t2
            self.newSudoku[3:6, :] = t3
            self.newSudoku[6:9, :] = t1
        elif r == 4:
            self.newSudoku[0:3, :] = t3
            self.newSudoku[3:6, :] = t1
            self.newSudoku[6:9, :] = t2
        elif r == 5:
            self.newSudoku[0:3, :] = t3
            self.newSudoku[6:9, :] = t1

    # 스도쿠 회전
    def __rotateSudoku(self):
        r = random.randrange(4)
        self.newSudoku = np.rot90(self.newSudoku, r)

    # 스도쿠 반전
    def __flipSudoku(self):
        r = random.randrange(4)
        if r == 0:
            self.newSudoku = np.fliplr(self.newSudoku)
        elif r == 1:
            self.newSudoku = np.flipud(self.newSudoku)
        elif r == 2:
            self.newSudoku = np.transpose(self.newSudoku)
        elif r == 3:
            self.newSudoku = np.transpose(np.flipud(self.newSudoku))

    # 숫자 1대1 교환
    def __swapNumber(self):
        r1 = random.randrange(1, 10)
        r2 = random.randrange(1, 10)
        while r1 == r2:
            r2 = random.randrange(1, 10)
        temp1 = self.newSudoku == r1
        temp2 = self.newSudoku == r2

        self.newSudoku[temp1] = r2
        self.newSudoku[temp2] = r1
