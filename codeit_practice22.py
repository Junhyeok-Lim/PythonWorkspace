# numbers=[19,13,2,5,3,11,7,17]

# new_list=sorted(numbers, reverse=True)
# print(new_list)

# # 원화(￦)에서 달러($)로 변환하는 함수
# def krw_to_usd(krw):
#     return krw/1000


# # 달러($)에서 엔화(￥)로 변환하는 함수
# def usd_to_jpy(usd):
#     return usd/8*1000


# # 원화(￦)으로 각각 얼마인가요?
# prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
# print("한국 화폐: " + str(prices))
 
# # prices를 원화(￦)에서 달러($)로 변환하기
# i=0
# while i<len(prices):
#     prices[i]=krw_to_usd(prices[i])
#     i+=1

# # 달러($)로 각각 얼마인가요?
# print("미국 화폐: " + str(prices))

# # prices를 달러($)에서 엔화(￥)으로 변환하기
# i=0
# while i<len(prices):
#     prices[i]=usd_to_jpy(prices[i])
#     i +=1

# # 엔화(￥)으로 각각 얼마인가요?
# print("일본 화폐: " + str(prices))

# # 빈 리스트 만들기
# numbers = []
# print(numbers)

# # numbers에 값들 추가
# numbers=[1,7,3,6,5,2,13,14]
# print(numbers)

# # numbers에서 홀수 제거
# i=0
# while i<len(numbers):
#     if numbers[i]%2==1:
#         del numbers[i]
#     else:
#         i+=1
# print(numbers)
# numbers.insert(0,20)
# # numbers의 인덱스 0 자리에 20이라는 값 삽입

# print(numbers)

# # numbers를 정렬해서 출력
# numbers.sort()
# print(numbers)

# numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] 


# # 인덱스와 원소 출력
# for i in range(len(numbers)):
#     print(i,numbers[i])



# greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

# i=0
# while i<len(greetings):
#     print(greetings[i])
#     i+=1

# for i in range(1,11):
#     print("{}^{}={}".format(2,i,2**i))

# for i in range(1,10):
#     for j in range(1,10):
#         print("{}*{}={}".format(i,j,i*j))

# for a in range(1,400):
#     for b in range(1,400):
#         c=400-a-b
#         if a*a+b*b==c*c and a<b<c:
#             print(a*b*c)

# numbers=[2,3,5,7,11,13,17,19]


# print("뒤집어진 리스트:" +str(numbers))
# numbers.reverse()
# print(str(numbers))

##사전 (dictionary)
##key-value pair(키-값 쌍)

# my_dictionary={
#     5:25,
#     2:4,
#     3:9
# }
# my_dictionary[9]=81
# print(my_dictionary[3])

# vocab={
#     "sanitizer":"살균제",
#     "ambition":"야망",
#     "conscience":"양심",
#     "civilization":"문명"
# }
# print(vocab)
# vocab["privilege"]="특권"
# vocab["principle"]="원칙"
# print(vocab)

# my_family={
#     "엄마":"김자옥",
#     "아빠":"이석진",
#     "아들":"이동민",
#     "딸":"이지영"
# }
# for key,value in my_family.items():
#     print(key,value)

# def reverse_dict(dict):
#     new_dict={}
#     for key,value in dict.items():
#         new_dict[value]=key


#     return new_dict

# vocab={
#     'sanitizer':'살균제',
#     'ambition':'야망',
#     'conscience':'양심',
#     'civilization':'문명',
#     'privilege':'특권',
#     'principle':'원칙'
# }

# print("영-한 단어장\n{}\n".format(vocab))

# reverse_vocab=reverse_dict(vocab)
# print("한-영 단어장\n{}".format(reverse_vocab))

# 투표 결과 리스트
# votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
# '최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
# '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# # 후보별 득표수 사전
# vote_counter = {}

# # 리스트 votes를 이용해서 사전 vote_counter를 정리하기
# for name in votes:
#     if name not in vote_counter:
#         vote_counter[name]=1
#     else:
#         vote_counter[name]+=1

# # 후보별 득표수 출력
# print(vote_counter)

# def sum_digit(num):
#     total=0
#     str_num=str(num)

#     for digit in str_num:
#         total+=int(digit)
#     return total

# digital_total=0
# for i in range(1,1001):
#     digital_total+=sum_digit(i)

# print(digital_total)


##sum_digit 함수 선언, total 값 선언 및 초기화, num를 string값으로 새로 선언
# def sum_digit(num):
#     total=0
#     str_num=str(num)

#     for digit in str_num:
#         total+=int(digit)
#     return total

# digital_total=0
# for i in range(1,1001):
#     digital_total+=sum_digit(i)

# print(digital_total)

# def mask_security_number(security_number):
#     return security_number[:-4]+"****"



# print(mask_security_number("880720-1234567"))
# print(mask_security_number("8807201234567"))
# print(mask_security_number("930124-7654321"))
# print(mask_security_number("9301247654321"))
# print(mask_security_number("761214-2357111"))
# print(mask_security_number("7612142357111"))

# def is_palindrome(word):
#     for left in range(len(word)//2):
#         right=len(word)-left-1
#         if word[left]!=word[right]:
#             return False
#     return True


# print(is_palindrome("racecar"))
# print(is_palindrome("stars"))
# print(is_palindrome("토마토"))
# print(is_palindrome("kayak"))
# print(is_palindrome("hello"))

# import random

# ANSWER=random.randint(1,20)
# NUM_TRIES=4

# guess=-1
# tries=0

# while guess != ANSWER and tries<NUM_TRIES:
#     guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
#     tries+=1

#     if ANSWER>guess:
#         print("UP")
#     elif ANSWER<guess:
#         print("DOWN")

# if guess==ANSWER:
#     print("축하합니다. {}번 만에 맞히셨습니다.".format(tries))
# else:
#     print("아쉽습니다. 정답은{}입니다.".format(ANSWER))


