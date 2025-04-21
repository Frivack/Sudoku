import tkinter as tk
from tkinter import messagebox
import numpy as np
import time

import rrun
from SudokuHint import *
from result import *


class SudokuGUI:
    def __init__(self, sudoku, cadsudoku, correct):
        self.correct = correct
        self.shint = SudokuHint(correct)
        self.sresult = SudokuResult()

        self.window = tk.Tk()

        self.window.title("Sudoku")
        self.window.geometry("720x620+100+100")
        self.window.resizable(False, False)

        # 전체 게임 프레임
        self.gameFrame = tk.Frame(self.window)
        self.gameFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 스도쿠 그리드 프레임
        self.mainFrame = tk.Frame(self.gameFrame, relief="solid", bd=2)
        self.mainFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.sections = [[None for _ in range(3)] for _ in range(3)]

        self.sudoku = sudoku
        self.cadsudoku = cadsudoku

        self.inputMode = "answer"

        # 버튼 생성
        self.numberButtons = [[None for _ in range(9)] for _ in range(9)]  # 9x9 버튼 리스트 초기화

        # 선택된 버튼의 위치 변수
        self.selectedRow = -1
        self.selectedCol = -1

        # 선택된 버튼 저장용 변수
        self.selectedCanvas = None  # 선택된 캔버스를 저장할 변수

        # 각 섹션별로 프레임 생성
        for i in range(3):
            for j in range(3):
                self.sectionFrame = tk.Frame(self.mainFrame, bd=2, relief="ridge")
                self.sectionFrame.grid(row=i, column=j, sticky="nsew")

                # 캔버스 생성 및 배치
                for k in range(9):
                    rowNum = i * 3 + k // 3
                    colNum = j * 3 + k % 3

                    canvas = tk.Canvas(self.sectionFrame, bg="white", width=60, height=60, bd=0, highlightthickness=0)
                    canvas.grid(row=k // 3, column=k % 3, sticky="nsew", padx=(2, 0), pady=(2, 0))
                    canvas.bind("<Button-1>", lambda event, x=rowNum, y=colNum: self.selectCell(x, y, event.widget))

                    # 정답 표시
                    value = self.sudoku[rowNum, colNum]
                    if value != 0:
                        canvas.create_text(30, 30, text=str(value), font=("Arial", 16), tags="answer")

                    # 후보 숫자 표시
                    candidates = self.cadsudoku[rowNum, colNum]
                    if 0 not in candidates:
                        candidate_text = ' '.join(map(str, candidates))
                        canvas.create_text(50, 10, text=candidate_text, font=("Arial", 8), anchor="ne",
                                           tags="candidate")

                    self.numberButtons[rowNum][colNum] = canvas

                # 각 프레임에 weight 설정
                for m in range(3):
                    self.sectionFrame.rowconfigure(m, minsize=50, weight=1)
                    self.sectionFrame.columnconfigure(m, minsize=50, weight=1)

                    self.sections[i][j] = self.sectionFrame

        # 메인 프레임의 행과 열에 weight 설정
        for i in range(3):
            self.mainFrame.rowconfigure(i, weight=1)
            self.mainFrame.columnconfigure(i, weight=1)

        # 하단에 모든 버튼과 입력 칸을 포함하는 프레임
        self.controlFrame = tk.Frame(self.window)
        self.controlFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

        # 숫자 입력/후보 숫자 전환 버튼
        self.toggleInputModeButton = tk.Button(self.controlFrame, text="정답 입력 모드",
                                               command=self.toggleInputMode)
        self.toggleInputModeButton.pack(side=tk.LEFT, padx=5)

        # 입력 칸
        self.inputVar = tk.StringVar()
        self.inputVar.trace_add("write", self.limitInputSize)
        self.inputEntry = tk.Entry(self.controlFrame, textvariable=self.inputVar)
        self.inputEntry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # 엔터키 이벤트 바인딩
        self.inputEntry.bind("<Return>", self.confirmInputEvent)

        # 입력 확인 버튼
        self.confirmInputButton = tk.Button(self.controlFrame, text="입력 확인", command=self.confirmInput)
        self.confirmInputButton.pack(side=tk.LEFT, padx=5)

        # 힌트 버튼 1
        self.hintButton1 = tk.Button(self.controlFrame, text="힌트", command=self.hint1)
        self.hintButton1.pack(side=tk.LEFT, padx=5)

        # 힌트 버튼 2
        # self.hintButton2 = tk.Button(self.controlFrame, text="힌트 2", command=self.hint2)
        # self.hintButton2.pack(side=tk.LEFT, padx=5)

        # 타이머와 검사 버튼을 포함하는 프레임
        self.rightFrame = tk.Frame(self.gameFrame)
        self.rightFrame.pack(side=tk.LEFT, fill=tk.Y)

        # 타이머 레이블
        self.timerLabel = tk.Label(self.rightFrame, text="00:00:00", font=("Arial", 14))
        self.timerLabel.pack(side=tk.TOP, padx=10, pady=10)
        self.updateTimer()

        # 스도쿠 검사 버튼
        self.checkButton = tk.Button(self.rightFrame, text="정답 확인", command=self.answerButton)
        self.checkButton.pack(side=tk.TOP, padx=10, pady=10)

    def start(self):
        self.window.mainloop()

    # 스도쿠 숫자 클릭시 이벤트
    def selectCell(self, row, col, canvas):
        if self.selectedCanvas:
            self.selectedCanvas.config(bg="white")
        self.selectedCanvas = canvas
        if self.inputMode == "answer":
            self.selectedCanvas.config(bg="lightblue")
        else:
            self.selectedCanvas.config(bg="lightgreen")

        self.selectedRow = row
        self.selectedCol = col

    # 입력 모드 변환 (숫자 입력/후보 숫자 입력)
    def toggleInputMode(self):
        if self.inputMode == "answer":
            self.inputMode = "candidate"
            self.toggleInputModeButton.config(text="후보 숫자 모드")
        else:
            self.inputMode = "answer"
            self.toggleInputModeButton.config(text="정답 입력 모드")
        self.selectCell(self.selectedRow, self.selectedCol, self.selectedCanvas)

    def confirmInputEvent(self, event):
        self.confirmInput()

    # 입력 버튼 이벤트
    def confirmInput(self):
        value = self.inputEntry.get()
        if self.selectedRow >= 0 and self.selectedCol >= 0 and self.selectedCanvas and value != '':

            if self.inputMode == "answer":
                # 셀에 정답 입력
                self.sudoku[self.selectedRow][self.selectedCol] = int(value)
                self.selectedCanvas.delete("answer")  # 기존 내용 삭제
                self.selectedCanvas.create_text(30, 30, text=value, font=("Arial", 16), tags="answer")
            else:
                # 후보 숫자 목록 업데이트
                candidate_value = int(value)
                candidates = self.cadsudoku[self.selectedRow][self.selectedCol]  # 직접 리스트 접근
                if candidate_value in candidates:
                    candidates.remove(candidate_value)  # 값이 이미 존재하면 제거
                else:
                    candidates.append(candidate_value)  # 값이 존재하지 않으면 추가

                # 후보 숫자 표시 업데이트
                candidates_text = ' '.join(map(str, sorted(candidates)))
                self.selectedCanvas.delete("candidate")
                self.selectedCanvas.create_text(50, 10, text=candidates_text, font=("Arial", 8), anchor="ne",
                                                tags="candidate")

            # 입력 칸 초기화
            self.inputEntry.delete(0, tk.END)

    def hint1(self):
        if self.selectedRow >= 0 and self.selectedCol >= 0:
            value = self.sudoku[self.selectedRow][self.selectedCol]
            hintMessage = self.shint.giveMeHint(self.selectedRow, self.selectedCol, value)
            tk.messagebox.showinfo("힌트", hintMessage)
        else:
            tk.messagebox.showinfo("힌트", "셀을 선택해주세요.")

    def hint2(self):
        # 힌트 2 메소드
        pass

    def answerButton(self):
        # 스도쿠 검사 결과
        isCorrect = self.sresult.compareSudoku(self.sudoku)
        if isCorrect:
            tk.messagebox.showinfo("정답 확인", "정답입니다!")
        else:
            tk.messagebox.showinfo("정답 확인", "오답입니다!")

            if tk.messagebox.askyesno("정답 공개", "정답을 공개하시겠습니까?"):
                # 모든 후보 숫자 지우기
                for i in range(9):
                    for j in range(9):
                        self.cadsudoku[i][j] = [0]

                # 화면에 정답 스도쿠 업데이트
                self.sudoku = self.correct.copy()
                self.updateSudoku(self.correct)

    def limitInputSize(self, *args):
        value = self.inputVar.get()
        if len(value) > 1:  # 최대 입력 길이를 1로 제한
            self.inputVar.set(value[:1])

    def updateCell(self, row, col, value):
        # 스도쿠 배열 업데이트 로직, 예를 들어:
        # self.sudoku[row][col] = value
        # 화면에 업데이트
        self.numberButtons[row][col].config(text=value)

    def updateTimer(self):
        time_laps = rrun.print_second()
        self.timerLabel.config(text=f'{time_laps:04d}초 경과')
        self.window.after(1000, self.updateTimer)

    # 전체 스도쿠 업데이트용 메소드
    def updateSudoku(self, sudoku):
        for i in range(9):
            for j in range(9):
                self.numberButtons[i][j].delete("answer")  # 기존 텍스트 삭제
                value = sudoku[i][j]
                if value != 0:
                    self.numberButtons[i][j].create_text(30, 30, text=str(value), font=("Arial", 16), tags="answer")
