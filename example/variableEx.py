gun = 10


def checkpoint(soldiers):
    global gun  # 전역 공간에 있는 gun사용
    gun -= soldiers
    print("남은 총 : {}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("남은 총 : {}".format(gun))
    return gun


checkpoint(2)
checkpoint_ret(gun, 2)
