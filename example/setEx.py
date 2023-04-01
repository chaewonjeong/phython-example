# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1, 2, 3, 4, 5, 6, 6, 6}
print(my_set)

my_set2 = {1, 2, 3, 4}

# 교집합
print(my_set2 & my_set)
print(my_set2.intersection(my_set))

# 합집합
print(my_set | my_set2)
print(my_set.union(my_set2))

# 차집합
print(my_set - my_set2)
print(my_set.difference(my_set2))


# 집합에 원소추가
my_set.add(7)
print(my_set)


my_set2.remove(2)
print(my_set2)
