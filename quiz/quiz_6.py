# 표준 체중을 구하는 프로그램을 작성하시오
#
# * 표준 체중: 각 개인의 키에 적당한 체중
#
# (성별에 따른 공식)
# 남자: 키 x 키 x 22
# 여자: 키 x 키 x 21
#
# 조건1: 표준 체중은 별도의 함수 내에서 계산
# * 함수명: std_weight
# * 전달값: 키, 성별
#
# 조건2: 표준 체중은 소수점 둘째자리까지 표기
#
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, sex):
    if sex == '남자':
        return height, sex, height * height * 22
    elif sex == '여자':
        return height, sex, height * height * 21
    else:
        print('잘못된 성별입니다')


man = std_weight(1.75, '남자')

# round(x, n) : 소수점 처리

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(
    man[0], man[1], round(man[2], 2)))
