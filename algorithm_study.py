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



# def course_selection(course_list):
#     # 수업이 끝나는 순서로 정렬
#     sorted_list = sorted(course_list, key=lambda x: x[1])

#     #가장 먼저 끝나는 수업은 무조건 듣는다.
#     my_selection = [sorted_list[0]]

#     #이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
#     for course in sorted_list:
#         # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
#         if course[0] > my_selection[-1][1]:
#             my_selection.append(course)

#     return my_selection


# # 테스트 코드
# print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
# print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
# print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))


# def sublist_max(profits):
#     max_profit=profits[0]

#     for i in range(len(profits)):
#         # i 부터 j 까지 profit 합을 보관
#         total = 0

#         for j in range(i, len(profits)):
#             total += profits[j]

#             # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
#             max_profit=max(max_profit, total)

#     return max_profit




# def power(x, y):
#     if y==0:
#         return 1
    
#     subresult=power(x,y//2)

#     if y%2==0:
#         return subresult*subresult
    
#     else:
#         return x*subresult*subresult


# print(power(3, 5))
# print(power(5, 6))
# print(power(7, 9))


# def select_stops(water_stops, capacity):
    
#     stop_list = []

#     prev_stop=0

#     for i in range(len(water_stops)):
#         # i 까지 갈 수 없으면, i-1 지점 약수터를 들른다.
#         if water_stops[i]-prev_stop>capacity:
#             stop_list.append(water_stops[i-1])
#             prev_stop=water_stops[i-1]
#     # 마지막 약수터는 무조건 간다.
#     stop_list.append(water_stops[-1])

#     return stop_list


# # 테스트 코드
# list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
# print(select_stops(list1, 4))

# list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
# print(select_stops(list2, 6))


# def find_same_number(some_list):
    
#     elements_seen = {}

#     for element in some_list:
#         # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴
#         if element in elements_seen:
#             return element

#         elements_seen[element] = True
    

# # 중복되는 수 ‘하나’만 리턴합니다.
# print(find_same_number([1, 4, 3, 5, 3, 2]))
# print(find_same_number([4, 1, 5, 2, 3, 5]))
# print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))


# def max_crossing_sum(profits, start, end):
#     # 여기에 코드를 작성하세요
#     mid = (start + end) // 2

#     left_sum = 0
#     left_max = profits[mid]

#     for i in range(mid, start -1, -1):
#         left_sum += profits[i]
#         left_max = max(left_max, left_sum)

#     right_sum = 0
#     right_max = profits[mid+1]

#     for i in range(mid+1, end+1):
#         right_sum += profits[i]
#         right_max = max(right_max, right_sum)

#     return left_max + right_max

# def sublist_max(profits, start, end):
#     if start == end:
#         return profits[start]
    
#     mid = (start + end) //2

#     max_left = sublist_max(profits, start, mid)
#     max_right = sublist_max(profits, mid+1, end)
#     max_cross = max_crossing_sum(profits, start, end)

#     return max(max_left, max_right, max_cross)
    

# # 테스트 코드
# list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
# print(sublist_max(list1, 0, len(list1) - 1))

# list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
# print(sublist_max(list2, 0, len(list2) - 1))

# list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
# print(sublist_max(list3, 0, len(list3) - 1))

# list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
# print(sublist_max(list4, 0, len(list4) - 1))

# def sublist_max(profits):
#     max_profit=profits[0]
#     max_check = profits[0]

    
#     for i in range(1, len(profits)):
        
        
#         max_check = max(max_check + profits[i], profits[i])

#         max_profit = max(max_profit, max_check)

        

#     return max_profit

# # 테스트 코드
# print(sublist_max([7, -3, 4, -8]))
# print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))


# #Brute Force 이용

# def max_profit(stock_list):
#     # 현재까지 최대 수익
#     max_profit_so_far = stock_list[1] - stock_list[0]

#     # 한 번 사고 파는 모든 조합을 본다.
#     for i in range(len(stock_list)-1):
#         for j in range(i+1, len(stock_list)):
#         # i에서 사고 j에 파는 것이 현재까지의 최대 수익이라면 max_so_far를 바꾼다.
#             max_profit_so_far = max(max_profit_so_far, stock_list[j]-stock_list[i])

#     return max_profit_so_far

# # 테스트 코드
# print(max_profit([7, 1, 5, 3, 6, 4]))
# print(max_profit([7, 6, 4, 3, 1]))
# print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
# print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))

# def max_profit(stock_list):
#     # 현재까지의 최대 수익
#     max_profit_so_far = stock_list[1] - stock_list[0]

#     # 현재까지의 최소 주식 가격
#     min_so_far = min(stock_list[0], stock_list[1])

#     # 주식 가격을 하나씩 확인
#     for i in range(2, len(stock_list)):
#         # 현재 파는 것이 좋은지 확인
#         max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_so_far)

#         # 현재 주식 가격이 최솟값인지 확인
#         min_so_far = min(min_so_far, stock_list[i])

#     return max_profit_so_far

# print(max_profit([7, 1, 5, 3, 6, 4]))
# print(max_profit([7, 6, 4, 3, 1]))
# print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
# print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))


# 출근하는 방법1
# def staircase(n):
#     a, b = 1, 1
#     for i in range(n):
#         a, b = b, a+b
#     return a

# print(staircase(0))
# print(staircase(6))
# print(staircase(15))
# print(staircase(25))
# print(staircase(41))


# ## 출근하는 방법2
# # 높이 n개의 계단을 올라가는 방법을 리턴
# def staircase(stairs, possible_steps):
#     # 계단 높이가 0 이거나 1 이면 올라가는 방법은 한 가지밖에 없음.
#     number_of_ways = [1,1]

#     for height in range(2, stairs + 1):
#         number_of_ways.append(0)

#         for steps in possible_steps:
#             #음수 계단은 존재하지 않기 때문에 무시
#             if height - steps>=0:
#                 number_of_ways[height] += number_of_ways[height - steps]

#     return number_of_ways[stairs]


# print(staircase(5, [1, 2, 3]))
# print(staircase(6, [1, 2, 3]))
# print(staircase(7, [1, 2, 4]))
# print(staircase(8, [1, 3, 5]))

