from random import *

##일반 유닛 (부모 클래스)
class Unit:
    def __init__(self, name, hp, speed) :
        self.name=name
        self.hp=hp
        self.speed=speed
        print('{} 유닛이 생성되었습니다.'.format(name)) #self.name 적어도 상관 X

        # self.damage=damage
    def move(self, location):
        print('[지상유닛이동]')
        print('{} : {} 방향으로 이동합니다. [속도{}]'.format(self.name, location, self.speed))

    def damaged(self, damage):
        print('{} : {} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp= self.hp-damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp<=0 :
            print('{} : 파괴되었습니다.'.format(self.name))
        

class AttackUnit(Unit):  #AttackUnit은 Unit을 상속 (자식 클래스)
    def __init__(self, name, hp,speed, damage):
        # self.name=name
        # self.hp=hp  상속 받았기 때문에 필요 x
        Unit.__init__(self,name,hp, speed)
        self.damage=damage

    def attack(self, location):
        print('{} : {} 방향으로 공격합니다. [공격력{}]'.format(self.name, location,self.damage))

    def damaged(self, damage):
        print('{} : {} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp= self.hp-damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp<=0 :
            print('{} : 파괴되었습니다.'.format(self.name))
        
class Marine: #스팀팩
    def __init__(self):
        AttackUnit.__init__(self,'마린',40,1,5)
    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print('{} : 스팀팩을 사용합니다. (HP 10 감소'.format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩 사용 불가".format(self.name))
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,'탱크',150,1,35)
        self.seize_mode=False
    
    def set_seize_mode(self):
        if Tank.seize_developed==False:
            return
        
        #현재 시즈모드가 아닐 때
        if self.seize_mode==False:
            print("{} : 시즈모드 전환".format(self.name))
            self.damage *=2
            self.seize_mode=True
        else:
            print('{} : 시즈모드 해제'.format(self.name))
            self.damage /=2
            self.seize_mode=False
class Wraith:
    def __init__(self):
        FlyableAttackUnit.__init__(self,'레이스',80,20,5)
        self.clocked=False

    def clocking(self):
        if self.clocked == True: ## 클로킹 모드 -> 모드 해제
            print("{} : 클로킹 모드 해제".format(self.name))
            self.clocked=False
        else:
            print('{} : 클로킹 모드 설정'.format(self.name))
            self.clocked=True      

class Flyalbe:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print('{} : {} 방향으로 날아갑니다. [속도 {}]'.format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyalbe): ## 다중상속 AttackUnit과 Flyable 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp,0, damage) ## 지상 스피드 = 0
        Flyalbe.__init__(self,flying_speed)
    
    def move(self, location):
        print('[공중유닛이동]')
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name,hp,0) ## super를 통해서 init하면 super뒤에 () 쓰고, self 인자 쓰지 않음
        self.location=location


supply_depot=BuildingUnit('서플라이 디폿', 500, '7시')


def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('Player : GG')
    

#실제 게임 진행
game_start()

m1=Marine()
m2=Marine()
m3=Marine()

t1=Tank()
t2=Tank()

w1=Wraith()

## 유닛 일괄 관리
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
# for unit in attack_units:
    # unit.move('1시')

#탱크 시즈모드 개발
Tank.seize_developed=True
print('[알림] 탱크 시즈 모드 개발 완료')

#공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹 모드)
for unit in attack_units:# 이 객체가 클래스의 인스턴스인지 확인
    if isinstance(unit, Marine): 
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack('1시')

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음 (5~20)

# 게임 종료
game_over()







# valkyrie=FlyableAttackUnit('발키리',200,6,5)
# valkyrie.fly(valkyrie.name,'3시')

# vulture=AttackUnit('벌쳐',80,10,20)

# battle_cruiser=FlyableAttackUnit('배틀크루저',500,25,3)

# vulture.move('11시')
# # battle_cruiser.fly('배틀크루저','9시')
# battle_cruiser.move('9시')







# firebat1=AttackUnit('파이어뱃',50,16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)







# marine1=Unit('마린',40,5)
# marine2=Unit('마린',40,5)
# tank=Unit('탱크',150,35)

# wraith1= Unit('레이스',80,5)
# print('유닛 이름 : {}, 공격력 : {}'.format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤
# wraith2=Unit('빼앗은 레이스',80,5)
# wraith2.clocking=True

# if wraith2.clocking==True:
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name)) ##Unit class 내에 clocking이란 변수가 없지만 외부에서 생성 가능