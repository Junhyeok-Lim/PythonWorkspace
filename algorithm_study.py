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
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    p = end

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
    swap_elements(my_list, b, p)
    p = b

    # pivot의 최종 인덱스를 리턴해 준다
    return p


# 테스트 코드 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 코드 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
