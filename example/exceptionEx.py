# 예외처리

# try:
#    print("나누기 전용 계산기입니다.")
#    nums = []
#    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#    # nums.append(int(nums[0]/nums[1]))
#
#    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#    print("에러 : 잘못된 값을 입력하였습니다.")
#
# except ZeroDivisionError as err:
#    print(err)
#
# except Exception as err:
#    print(err)


# 에러 발생시키키
# 한 자리 숫자 나누기 전용 계산기

# 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))

    if nums[0] >= 10 or nums[1] >= 10 or nums[0] < 1 or nums[1] < 1:
        raise BigNumberError("입력값 : {0}, {1}".format(nums[0], nums[1]))
    nums.append(int(nums[0]/nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except BigNumberError as err:
    print("에러 : 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
    print(err)

# finally
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
