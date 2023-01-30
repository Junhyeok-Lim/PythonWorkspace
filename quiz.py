##변수를 이용하여 다음 문장을 출력하시오

##변수명 : station

##변수값 : "사당", "신도림", "인천공항" 순서대로 입력

##출력 문장 : XX행 열차가 들어오고 있습니다.


# station_1="사당"
# station_2="신도림"
# station_3="인천공항"

# print(station_1+"행 열차가 들어오고 있습니다.")
# print(station_2+"행 열차가 들어오고 있습니다.")
# print(station_3+"행 열차가 들어오고 있습니다.")

#=====================================================================================

# 월 4회 스터디, 3번은 온라인 1번은 오프라인

# 조건1: 랜덤으로 날짜를 뽑아야 함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
# from random import randint

# print("오프라인 스터디 모임 날짜는 매월 {} 일로 선정되었습니다.".format(randint(4,28)))

#=========================================================================================
# 사이트별 비밀번호를 만들어주는 프로그램 작성

# 예)http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'개수 + '!'로 구성
#                  (nav)             (5)           (1)            (!)
# 예) 생성된 비밀번호 : nav51!

# site="http://naver.com"
# word=site[7:12]
# word_3=word[:3]
# count_word=len(word)
# count_e=word.count("e")

# password=word_3+str(count_word)+str(count_e)+"!"
# print(password)

# url="http://naver.com"
# my_str=url.replace("http://","")
# my_str=my_str[:my_str.index(".")]
# password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# print("{}의 비밀번호는 {}입니다.".format(url, password))
#==============================================================================================

# 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
# 조건1: 댓글은 20명이 작성, 아이디는 1~20이라 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle 과 samplpe을 활용

# from random import *


# users=list(range(1,21))

# shuffle(users)
# winners=sample(users,4)


# print("--당첨자 발표--")
# print("치킨 당첨자 : {}".format(winners[0]))
# print("커피 당첨자 :{}".format(winners[1:]))
# print("--축하합니다--")
#===========================================================================================

# 택시기사
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 조건1: 승객별 운행 소요 시간은 5~50분 사이의 난수
# 조건2: 소요 시간 5~15분 사이의 승객만 매칭해야 함
# from random import *
# customer=range(1,50)

# count=0
# i=0
# while i<51:
    
#     i+=1
#     time=randrange(5,51)
    
#     if time>=5 and time<=15 :
#         print("[0] {}번째 손님 (소요시간) : {}분".format(i, time))
#         count+=1
#     else :
#         print("[] {}번째 손님 (소요시간) : {}분".format(i, time))
    
# print("총 탑승 승객 : {}분".format(count))


#=====================================================================
# 표준 체중
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#         *함수명 : std_weight
#         *전달값 : 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# def std_weight(height, gender):
#     weight=0
#     if gender=='남자':
#         return height*height*22
#     else :
#         return height*height*21
# height=175
# gender='남자'
# weight=std_weight(height/100, gender)
# print("키 {}cm {}의 표준 체중은 {}kg입니다.".format(height,gender,weight))

#============================================================================
# 매주 1회 보고서 작성

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서파일을 만드는 프로그램

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듬

# for i in range(1,51):
#     with open(str(i)+'주차.txt','w',encoding='utf8') as report_file:
#         report_file.write("- {} 주차 주간보고 -".format(i))
#         report_file.write('부서 : \n')
#         report_file.write('이름 : \n')
#         report_file.write('업무 요약 : \n')

#==================================================================================================

# 총 3대의 매물
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location=location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price=price
#         self.completion_year=completion_year

#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price,self.completion_year)

# houses=[]
# house1=House('강남', '아파트','매매','10억','2010년')
# house2=House('마포','오피스텔','전세','5억','2007년')
# house3=House('송파','빌라','월세','500/50','2000년')
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
# print('총 {}대의 매물이 있습니다.'.format(len(houses)))

# for house in houses:
#     house.show_detail()

#=======================================================================================================
# chicken=10
# waiting=1 # 대기번호 1번

# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print('[남은 치킨] : {}'.format(chicken))
#         order=int(input('치킨 몇 마리 주문하시겠습니까?'))
#         if order>chicken:
#             print('재료가 부족합니다')
#         elif order<=0:
#             raise ValueError
        

#         else:
#             print('[대기번호 {}] {}마리 주문이 완료되었습니다.'.format(waiting, order))
#             waiting +=1
#             chicken -=order
#         if chicken==0:
            
#             raise SoldOutError
#     except ValueError:
#             print('잘못된 값을 입력하였습니다.')
#     except SoldOutError:
#         print('재고가 소진되어 더 이상 주문을 받지 않습니다.')
#         break

#========================================================================================================
# 프로젝트 내에 나만의 시그니처를 남기는 모듈

# 조건 : 모듈 파일명은 byme.py로 작성
import byme
byme.sign()