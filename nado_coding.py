# dictionary

# cabinet={3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet.get(100))
# print(cabinet.get(5, "사용 가능"))

# print(cabinet.items())

## Tuple
# menu=("돈까스", "치즈까스")
# print(menu[0])

# name,age,hobby="김종국",20,"코딩"

## 집합(set)
## 중복 안됨, 순서 없음

# my_set={1,2,3,3,3}
# print(my_set)

# java={"유", "김", "양"}
# python=set(["유","박"])

# #교집합
# print(java&python)
# print(java.intersection(python))
# #합집합
# print(java|python)
# print(java.union(python))
# #차집합
# print(java-python)
# print(java.difference(python))


##function
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {}입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance, money):
#     if balance>money:
#         print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 불가합니다. 잔액은 {}원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission=100#수수료
#     return commission, balance-money-commission

# open_account()
# balance=0
# balance=deposit(balance,1000)
# # balance=withdraw(balance, 500)
# commission, balance=withdraw_night(balance, 500)
# print("수수료 {}원이며, 잔액은 {}원입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {}\t 나이:{}\t 주 사용 언어:{}".format(name, age, main_lang))


# profile("유재석",20,'파이썬')
# profile("김태호",20,'자바')

##같은 학교, 같은 학년, 같은 반, 같은 수업 -> 이름만 다르지 나머지는 다 똑같음 ->기본값을 사용!!
# def profile(name, age=17, main_lang='파이썬'):
#     print("이름 : {}\t 나이:{}\t 주 사용 언어:{}".format(name, age, main_lang))

# profile("손흥민")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name='유', main_lang='python',age=20)



##가변인자
# def profile(name, age, *language):
#     print('이름:{}\t 나이:{}\t'.format(name,age),end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile('유',20,'python','Java','C','C++','C#','JavaScript')
# profile('김',25,'Kotlin','Swift')


##지역번수, 전역변수
# gun=10

# def checkpoint(soldiers):   #경계근무 나가는 군인들의 수
#     global gun ##전역 공간에 있는 gun을 사용하겠다
#     gun=gun-soldiers
#     print("[함수 내] 남은 총 : {}".format(gun))


# def checkpoint_return(gun, soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총 : {}".format(gun))
#     return gun

# print("전체 총 : {}".format(gun))
# # checkpoint(2)
# gun=checkpoint_return(gun, 2)
# print("남은 총 : {}".format(gun))

## 표준 입출력
# import sys
# print('Python','Java',file=sys.stdout)
# print('Python','Java',file=sys.stderr)

# scores={"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4),sep=":") ## 8칸을 확보하고 왼쪽 정렬, 4칸을 확보하고 오른쪽 정렬, :로 separate

# #은행 대기순번표
# #001, 002, 003, ...
# for num in range(1,20):
#     print('대기번호 : '+str(num).zfill(3)) #0으로 채움, 3크기만큼, 값이 없는 공간을 0으로 채움

# answer = input("아무 값이나 입력하세요 : ") ##input으로 값을 받으면 문자열로 받게 됨
# print(type(answer))
# # print("입력하신 값은 {}입니다.".format(answer))


#===============================================================================================================================
## 파일 입출력

# score_file=open('score.txt','w',encoding='utf8')
# print('수학 : 0', file=score_file)
# print('영어 : 50', file=score_file)
# print('과학 : 80', file=score_file)
# print('음악 : 60', file=score_file)
# score_file.close()

# score_file=open('score.txt','r',encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file=open('score.txt','w',encoding='utf8')
# print(score_file.readline()) ## 한줄만 읽어오고 커서를 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file=open('score.txt','r',encoding='utf8')
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line,end='')
# score_file.close()

# score_file=open('score.txt','r',encoding='utf8')
# lines=score_file.readlines()
# for line in lines:
#     print(line, end='')
# score_file.close()

## pickle
# 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장
# import pickle
# profile_file=open('profile.pickle','wb') # b는 binary -> pickle을 쓸 때 항상 wb
# profile={'이름': '박','나이' : 30, '취미' :['축구','골프','코딩']}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file=open('profile.pickle','rb')
# profile=pickle.load(profile_file) ## file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


## with
# import pickle

# with open('profile.pickle','rb') as profile_file:
#     print(pickle.load(profile_file))

# with open('study.txt','w',encoding='utf8') as study_file:
#     study_file.write('python study')

# with open('study.txt','r',encoding='utf8') as study_file:
#     print(study_file.read())



# # 예외 처리
# try:
#     print('나누기 전용 계산기입니다.')
#     # num1=int(input('첫 번째 숫자 입력 : '))
#     # num2=int(input('두 번째 숫자 입력 : '))
#     nums=[]
#     nums.append(int(input('첫 번째 숫자를 입력 : ')))
#     nums.append(int(input('두 번째 숫자를 입력 : ')))
#     nums.append(int(nums[0]/nums[1]))
#     print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
#     # print('{} / {} = {}'.format(num1, num2, int(num1/num2)))
# except ValueError:
#     print('에러! 잘못된 값 입력.')
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print('알 수 없는 오류 발생.')


## 사용자 정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg=msg

#     def __str__(self):
#         return self.msg

# try:
#     print('한 자리 숫자 나누기 전용 계산기')
#     num1=int(input('첫 번째 숫자를 입력 : '))
#     num2=int(input('두 번째 숫자를 입력 : '))
#     if num1>=10 or num2>=10:
#         raise BigNumberError('입력값 : {}, {}'.format(num1, num2))
#     print('{} / {} = {}'.format(num1, num2, int(num1/num2)))
# except ValueError:
#     print('잘못된 값 입력. 한자리 숫자만 입력하세요.')
# except BigNumberError:
#     print('에러 발생. 한 자리 숫자만 입력하세요.')
    
# except ZeroDivisionError as err:
#     print(err)
# finally:
#     print('계산기를 이용해 주셔서 감사합니다.')


## module // 타이어, 범퍼처럼 고장난 곳만 고치면 되게끔

# import theater_module
# theater_module.price(3) ##3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv ## 별명 붙이기
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(4)


