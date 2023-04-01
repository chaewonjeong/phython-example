
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오
#
# 조건1: 승객별 운행 소요 시간은 5분~ 50분 사이의 난수로 정해진다.
# 조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 한다.
#
# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [0] 2번째 손님 (소요시간 : 50분)
# ...
# [0] 50번째 손님 (소요시간 : 5분)
#
# 총 탑승 승객 : 2 명

# 난수 생성
import random


count = 0

for i in range(50):
    boarding_time = random.randrange(5, 50+1)

    if (boarding_time >= 5 and boarding_time <= 15):
        count += 1
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i+1, boarding_time))
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i+1, boarding_time))

print("총 탑승 승객 : {0}".format(count))
