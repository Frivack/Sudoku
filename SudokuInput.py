import numpy as np


class SudokuInput:
    def inputCorrect(self, sudoku):
        # x, y 는 스도쿠상의 좌표, value는 스도쿠에 입력할 값
        # 좌표나 값이 유효한지(입력 가능한지)는 sudoku 행렬 참조하여 처리
        x = 0
        y = 0
        value = 0

        return x, y, value

    def inputChecker(self, sudoku, checker):
        # sudoku는 정답을 입력중인 스도쿠, checker는 가입력 스도쿠
        # checker는 3차원 배열로 마지막 리스트([-][-][*])에는 1~9까지의 숫자가 겹치지 않게 들어가야 한다.
        # 이하 inputCorret와 동일
        x = 0
        y = 0
        value = 0

        return x, y, value
