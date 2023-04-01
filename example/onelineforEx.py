list_a = []
for i in range(10):
    list_a.append(i)

print(list_a)
'''간단한 리시트를 만들거나 간단하가 append 같은걸 할 때 보통 위와 같이한다.'''

list_a = [i for i in range(10)]

'''리스트 안에 for문 자체를 넣는 방법이다.'''


# for문을 이중으로 사용하는 경우에도 한 줄쓰기가 가능하다.

# 2차원 배열 선언
list_b = [[0 for j in range(4)] for i in range(5)]

# 2차원 배열 출력
for i in list_b:
    for j in i:
        print(j, end=" ")
    print()

print(list_b)


# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "groot"]
print(students)
students = [len(i) for i in students]
print(students)
