import threading

import numpy as np
from SudokuCreate import *
from SudokuHide import *
from SudokuHint import *
from SudokuInput import *
from SudokuResult import *
from SudokuSound import *
from SudokuGUI import *

# 스도쿠 출처
# https://news.imaeil.com/page/view/2020070914362820732ㅎ
sudokuCorrectSample = np.array([
    [8, 1, 5, 9, 7, 2, 3, 4, 6],
    [2, 9, 6, 8, 3, 4, 5, 7, 1],
    [4, 7, 3, 6, 5, 1, 8, 9, 2],
    [1, 2, 4, 7, 8, 9, 6, 5, 3],
    [9, 6, 8, 3, 4, 5, 2, 1, 7],
    [5, 3, 7, 1, 2, 6, 4, 8, 9],
    [6, 8, 2, 5, 9, 7, 1, 3, 4],
    [7, 5, 1, 4, 6, 3, 9, 2, 8],
    [3, 4, 9, 2, 1, 8, 7, 6, 5]]
)

# 가입력용 스도쿠 샘플
#sudokuCeckerSample = np.array([
#    [[1, 2, 8], [2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0], [0], [2], [3], [4], [6]],
#    [[1, 2], [9], [6], [8], [3], [4], [0], [0], [1]],
#    [[4], [0], [0], [6], [5], [0], [8], [0], [2]],
#    [[0], [2], [4], [7], [8], [0], [0], [0], [0]],
#    [[9], [0], [8], [3], [4], [5], [2], [1], [0]],
#    [[5], [3], [7], [1], [2], [6], [4], [8], [9]],
#    [[6], [8], [0], [1, 2, 3, 4, 5, 6, 7, 8], [9], [0], [0], [0], [4]],
#    [[0], [0], [1], [4], [0], [3], [9], [0], [8]],
#    [[0], [0], [9], [0], [1], [0], [7], [0], [5]]], dtype=object
#)


sudokuChecker = np.array([
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0]]], dtype=object
)

sudokuChecker = np.empty((9, 9), dtype=object)
for i in range(9):
    for j in range(9):
        sudokuChecker[i, j] = []


# 새로운 스도쿠 생성
sc = SudokuCreate(sudokuCorrectSample)
correctSudoku = sc.createNewSudoku()

# 스도쿠 가리기
shide = SudokuHide()
sudokuAnswerSample = shide.hiddenSudoku(correctSudoku)

# sinput = SudokuInput()

# GUI 시작
sui = SudokuGUI(sudokuAnswerSample, sudokuChecker, correctSudoku)
sui.start()
