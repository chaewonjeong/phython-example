from random import *


class Unit:
    # __init__ : 생성자
    def __init__(self, name, hp, speed):
        # 멤버변수 : 클래스 내에서 정의된 변수
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입없습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        else:
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage,):
        # 일반 유닛에서 만들어진 생성자를 호출해서 name과 hp를 정의
        Unit.__init__(self, name, hp, speed)
        # 추가로 공격력을 정의
        self.damage = damage

    # location 은 self없이 사용 -> 전달받은 값을 사용한다는 뜻
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(
            self.name, location, self.damage))


# 날 수 있는 기능을 가진 클래스


class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 마린


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (Hp 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        super().__init__("탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False

        else:
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True


def seize_mode_upgrade():
    Tank.seize_developed = True
    print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()


attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)


# 전군 이동

for unit in attack_units:
    unit.move("1시")

seize_mode_upgrade()

# 공격모드 준비
for unit in attack_units:
    # 지금 만들어진 객체가 어디 class의 객체인지 확인하는것
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 유닛 피해
for unit in attack_units:
    unit.damaged(randint(5, 51))


game_over()
