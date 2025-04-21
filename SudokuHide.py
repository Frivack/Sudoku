import numpy as np
import random


class SudokuHide:
    def __init__(self):
        self.hid = None
        self.difficulty = 0
        self.leftNums = 0

    def hiddenSudoku(self, sudoku):
        # hid 행렬을 가려진 스도쿠로 만들어서 reutrn
        # 가려진 부분은 0으로 표기
        # ex) [0, 0, 0, 1, 2, 0, 0, 0, 0]... << 첫 줄에 1과 2만 보이는 스도쿠
        if self.difficulty == 0:
            self.leftNums = 20
        elif self.difficulty == 1:
            self.leftNums = 26
        elif self.difficulty == 2:
            self.difficulty = 32

        self.hid = sudoku.copy()
        # 가려질 숫자의 위치를 저장할 집합
        positions = set()

        # 가릴 숫자의 총 개수 계산 (전체 칸 수 - 남겨둘 숫자의 개수)
        hidNums = 81 - self.leftNums

        while len(positions) < hidNums:
            # 무작위 위치 선택
            pos = (random.randint(0, 8), random.randint(0, 8))

            # 중복되지 않는 위치만 추가
            if pos not in positions:
                positions.add(pos)

        # 선택된 위치의 숫자를 가림
        for row, col in positions:
            self.hid[row, col] = 0

        return self.hid

    def setDifficulty(self, df):
        self.difficulty = df