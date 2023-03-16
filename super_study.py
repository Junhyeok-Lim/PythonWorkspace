class Father():
    def handsome(self):
        print("잘생겼다")

class Brother(Father):
    '''아들'''

class Sister(Father):
    def pretty(self):
        print("예쁘다")

    def handsome(self):
        return super().handsome() # super를 제거 할 시 girl의 handsome 출력 X

brother = Brother()
brother.handsome()

girl = Sister()
girl.handsome()
girl.pretty()