#네 번째 점
import sys
input = sys.stdin.readline

lx = []
ly = []
for _ in range(3):
    a,b = map(int, input().split())
    lx.append(a)
    ly.append(b)

if lx[0] == lx[1]:
    answerx = lx[2]
elif lx[0] == lx[2]:
    answerx = lx[1]
elif lx[1] == lx[2]:
    answerx = lx[0]
    
if ly[0] == ly[1]:
    answery = ly[2]
elif ly[0] == ly[2]:
    answery = ly[1]
elif ly[1] == ly[2]:
    answery = ly[0]
    
print(answerx, answery)