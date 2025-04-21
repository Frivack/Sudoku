import datetime
import math
import threading
import time

time_laps = 0

def print_second():
    now = time.strftime('%H:%M:%S')                     # 현재 시간
    time_laps = math.floor(time.time() - start_time)    # 경과 시간 계산(소수점버림)
    return time_laps
    #print(f'{now} : {time_laps}초 경과')
    #threading.Timer(0.1,print_second).start()             # x초 마다 반복


start_time = time.time()				# 시작 시간 저장
#print_second()

