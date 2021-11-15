import sys
import datetime

filename = "in.txt"
if filename:
    start = datetime.datetime.now()
    infile = open(filename)
else:
    infile = sys.stdin
inf = infile.read().splitlines()

#主要程式開始
#本程式由 三重商工 資料處理科 林易民老師 撰寫

while len(inf) > 0:
    line = inf.pop(0)
    print(line)

#主要程式結束

if infile is not sys.stdin:
    infile.close()
    end = datetime.datetime.now()
    print("執行時間:", end - start, "秒")