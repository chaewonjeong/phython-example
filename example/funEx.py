def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance+money


def withdraw(balance, money):  # 출금
    if (balance >= money):
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance-money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance


# 값 2개 리턴하기
def withdraw_night(balance, money):
    commission = 0.05
    return commission, balance - commission * money


balance = 1000  # 잔액

balance = deposit(balance, 100)
print(balance)

print()

balance = withdraw(balance, 100)
balance = withdraw(balance, 1000)
balance = withdraw(balance, 1000)

print()


balance = deposit(balance, 1000)
print()
print(balance)

commisson, balance = withdraw_night(balance, 1000)
print(balance)
print(commisson)


# function annotation(주석달기)
def func(arg1: str, arg2: 1+2, arg3: str) -> bool:
    print('this is function annotation')

# annotation 의 가장 큰 특징은 바로 강제성이 없다는 것이다.
# 즉, annotation 이라는 말그대로 주석일 뿐이며 해당 code 자체에는 어떠한 영향도 미치지 않는다.
