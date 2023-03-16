# 오버라이드(Override) : 같은 이름을 가진 메소드를 덮어 쓴다.

class father(): # parent class
    def handsome(self):
        print("Handsome")

class brother(father): #자식클래스(부모클래스) 아빠메소드를 상속받겠다
    '''아들'''

class sister(father):
    def pretty(self):
        print("Pretty")
    def handsome(self):
        self.pretty()

brother = brother()
brother.handsome()

sister = sister()
sister.handsome()