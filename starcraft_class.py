class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): ## super로 다중상속시 앞에있는 클래스만 호출
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship=FlyableUnit()

def function():
    pass

def function2():
    pass