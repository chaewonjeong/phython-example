# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in range(0, 10, 3):
    print("대기번호 : {0}".format(waiting_no))


# for 반복무니 리스트와 범위 조합하기
array = [27, 11, 25, 126, 45, 75, 23]

for i in array:
    print(i)
print("\n")

# for반복문: 반대로 반복하기
# 1) range()함수의 매개변수를 세개 사용하는 방법

for i in range(10, 0-1, -1):
    print(i)
print("\n")
# 2) reversed() 함수 이용하기

for i in reversed(range(10+1)):
    print(i)
print("\n")

output = ""

for i in range(1, 10):
    for j in range(0, i):
        output += "*"
    output += "\n"

print(output)
print("\n")


output2 = ""

for i in range(1, 11):
    for j in range(10, i, -1):
        output2 += " "
    for k in range(0, 2*i-1):
        output2 += "*"
    output2 += "\n"

print(output2)
