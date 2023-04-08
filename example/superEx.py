class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class AttackUnit(Unit):
    def __init__(self):
        super().__init__()


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()  # 다중 상속시 문제 발생
        Unit.__init__(self)
        Flyable.__init__(self)


a = AttackUnit()
b = FlyableUnit()
