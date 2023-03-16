class JSS:
    def __init__(self):
        self.name=input("이름 : ")
        self.age=input("나이 : ")
    def show(self):
        print("내 이름은 {}, 나이는 {}".format(self.name, self.age))

# a = JSS()
# a.show()

class JSS2(JSS):
    def __init__(self): #기존의 JSS의 init을 덮어쓰기
        super().__init__() #JSS의 init을 쓰고 싶을 떄
        self.gender=input("성별 : ")
    
    def show(self):
        print("내 이름은 {}, 나이는 {} 성별은 {}".format(self.name, self.age, self.gender))
        
a=JSS2()
a.show()

