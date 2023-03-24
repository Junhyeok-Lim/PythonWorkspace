# def max_product(left_cards, right_cards):
    
#     max_product = left_cards[0] * right_cards[0]

#     for left in left_cards:
#         for right in right_cards:
#             max_product = max(max_product, left*right)

    
#     return max_product

# print(max_product([1, 6, 5], [4, 2, 3]))
# print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
# print(max_product([-1, -7, 3], [-4, 3, 6]))


from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
# def distance(store1, store2):
#     return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# # 가장 가까운 두 매장을 찾아주는 함수
# def closest_pair(coordinates):
#     pair = [coordinates[0], coordinates[1]]

#     for i in range(len(coordinates)-1):
#         for j in range(i+1, len(coordinates)):
#             store1, store2 = coordinates[i], coordinates[j]

#             if distance(pair[0], pair[1])>distance(store1, store2):
#                 pair=[store1, store2]

#         return pair

# # 테스트 코드
# test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# print(closest_pair(test_coordinates))

# def consecutive_sum(start, end):
#     if end == start:
#         return start
#     mid = (start + end) // 2

#     return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)

# def normal_sum(n):
#     total=0
#     for i in range(1, n+1):
#         total += i
#     return total
    
# print(normal_sum(10))
# print(normal_sum(100))



# # 테스트 코드
# print(consecutive_sum(1, 10))
# print(consecutive_sum(1, 100))
# print(consecutive_sum(1, 253))
# print(consecutive_sum(1, 388))

# def merge(list1, list2):
#     merged_list=[]
#     i=0
#     j=0

#     while i<len(list1) and j<len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i+=1
#         else:
#             merged_list.append(list2[j])
#             j+=1
#     merged_list = merged_list + list1[i:] + list2[j:]
#     return merged_list


# print(merge([1],[]))
# print(merge([],[1]))
# print(merge([2],[1]))
# print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
# print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
# print(merge([4, 7, 8, 9],[1, 3, 6, 10]))



# 두 요소의 위치를 바꿔주는 helper function
# def swap_elements(my_list, index1, index2):
#     temp = my_list[index1]
#     my_list[index1] = my_list[index2]
#     my_list[index2] = temp


# # 퀵 정렬에서 사용되는 partition 함수
# def partition(my_list, start, end):
#     # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
#     i = start
#     b = start
#     p = end

#     # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
#     while i < p:
#         # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
#         if my_list[i] <= my_list[p]:
#             swap_elements(my_list, i, b)
#             b += 1
#         i += 1

#     # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
#     swap_elements(my_list, b, p)
#     p = b

#     # pivot의 최종 인덱스를 리턴해 준다
#     return p


# # 테스트 코드 1
# list1 = [4, 3, 6, 2, 7, 1, 5]
# pivot_index1 = partition(list1, 0, len(list1) - 1)
# print(list1)
# print(pivot_index1)

# # 테스트 코드 2
# list2 = [6, 1, 2, 6, 3, 5, 4]
# pivot_index2 = partition(list2, 0, len(list2) - 1)
# print(list2)
# print(pivot_index2)



# def fib_memo(n, cache):
#     if n<=2:
#         return 1
    
#     if n in cache:
#         return cache[n]
    
#     cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)

#     return cache[n]


# def fib(n):
    
#     fib_cache = {}

#     return fib_memo(n, fib_cache)


# # 테스트 코드
# print(fib(10))
# print(fib(50))
# print(fib(100))



# def fib(n):
#     fibList=[1,1]
#     if n<=2:
#         return 1
#     for i in range(2, n):
#         fibList.append(fibList[i-1] + fibList[i-2])
#     return fibList

# print(fib(11))

# def max_profit_memo(price_list, count, cache):
#     # Base Case: 0개 혹은 1개면 부분 문제로 나눌 필요가 없기 때문에 가격을 바로 리턴한다
#     if count < 2:
#         cache[count] = price_list[count]
#         return cache[count]

#     # 이미 계산한 값이면 cache에 저장된 값을 리턴한다
#     if count in cache:
#         return cache[count]

#     # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
#     # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
#     # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
#     if count < len(price_list):
#         profit = price_list[count]
#     else:
#         profit = 0

#     # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
#     for i in range(1, count // 2 + 1):
#         profit = max(profit, max_profit_memo(price_list, i, cache) 
#                  + max_profit_memo(price_list, count - i, cache))

#     # 계산된 최대 수익을 cache에 저장
#     cache[count] = profit

#     return profit


# def max_profit(price_list, count):
#     max_profit_cache = {}

#     return max_profit_memo(price_list, count, max_profit_cache)


# # 테스트 코드
# print(max_profit([0, 100, 400, 800, 900, 1000], 5))
# print(max_profit([0, 100, 400, 800, 900, 1000], 10))
# print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))


# def max_profit(price_list, count):
#     # 개수별로 가능한 최대 수익을 저장하는 리스트
#     # 새꼼달꼼 0개면 0원
#     profit_table = [0]

#     # 개수 1부터 count까지 계산하기 위해 반복문
#     for i in range(1, count + 1):
#         # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정   
#         if i < len(price_list):
#             profit = price_list[i]
#         else:
#             profit = 0

#         # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
#         for j in range(1, i // 2 + 1):
#             profit = max(profit, profit_table[j] + profit_table[i - j])

#         profit_table.append(profit)

#     return profit_table[count]


# # 테스트 코드
# print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
# print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
# print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))




# def min_coin_count(value, coin_list):
#     count = 0

#     for coin in sorted(coin_list, reverse=True):
#         count += (value // coin)

#         value %= coin
#     return count

# # 테스트 코드
# default_coin_list = [100, 500, 10, 50]
# print(min_coin_count(1440, default_coin_list))
# print(min_coin_count(1700, default_coin_list))
# print(min_coin_count(23520, default_coin_list))
# print(min_coin_count(32590, default_coin_list))


# def max_product(card_lists):
#     product = 1

#     for card_list in card_lists:
#         product *= max(card_list)

#     return product



# # 테스트 코드
# test_cards1 = [[1, 6, 5], [4, 2, 3]]
# print(max_product(test_cards1))

# test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
# print(max_product(test_cards2))

# test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
# print(max_product(test_cards3))

# test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
# print(max_product(test_cards4))


# def min_fee(pages_to_print):
#     #인풋으로 받은 리스트를 정렬
#     sorted_list = sorted(pages_to_print)

#     # 총 벌금을 담을 변수
#     total_fee=0

#     for i in range(len(sorted_list)):
#         total_fee+=sorted_list[i]*(len(sorted_list)-i)

#     return total_fee


# # 테스트 코드
# print(min_fee([6, 11, 4, 1]))
# print(min_fee([3, 2, 1]))
# print(min_fee([3, 1, 4, 3, 2]))
# print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))



def course_selection(course_list):
    # 수업이 끝나는 순서로 정렬
    sorted_list = sorted(course_list, key=lambda x: x[1])

    #가장 먼저 끝나는 수업은 무조건 듣는다.
    my_selection = [sorted_list[0]]

    #이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# 테스트 코드
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

