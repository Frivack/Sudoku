import numpy as np


# sudoku는 입력중인 스도쿠, checker는 가입력 되있는 스도쿠, correct는 정답 스도쿠
# 힌트 기능 구현

class SudokuHint:
    def __init__(self, correct):
        self.correct = correct

    def giveMeHint(self, x, y, value):
        correct_value = self.correct[x, y]
        if value == correct_value and value != 0:
            return f"정답입니다! 위치 ({x+1}, {y+1})의 값은 {value}입니다."
        else:
            return f"오답입니다. 위치 ({x+1}, {y+1})의 올바른 값은 {correct_value}입니다."
