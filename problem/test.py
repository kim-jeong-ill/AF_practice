# 당첨번호를 랜덤으로 추출 하는 부분.
import random
lotto = []
while True:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)

    if len(lotto) == 6:
        break


# 당첨번호 미리보기 테스트 코드
# print("당첨번호=", lotto)

# ("내 로또번호 띄어쓰기로 입력 :")

inputStr = input("내 로또번호 띄어쓰기로 6개 입력 :").split(" ")
mine = []
for n in inputStr:
    mine.append(int(n))



# 내번호가 lotto 당첨번호 리스트에 포함되어 있냐 체크.

same = 0
for myN in mine:
    if myN in lotto:
        same += 1



# 당첨번호와 내번호가 같은지 눈으로 확인하는 테스트 코드

print("당첨번호=", lotto)
print("내번호 = ", mine)



# same 에 따라 인덱싱해서 등수 표기 및 당첨금 입력

score = [0, 6, 5, 4, 3, 2, 1]
prize = [1000, 5000, 50000, 100000, 10000000, 1000000000]
if same == 0:
    print("미당첨")
else:
    print(f" {same}개 맞음, {score[same]} 등 당첨!")
    print(f" {score[same]} 등 당첨금 : {prize[same - 1]}")