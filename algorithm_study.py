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

def consecutive_sum(start, end):
    if end == start:
        return start
    mid = (start + end) // 2

    return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)

def normal_sum(n):
    total=0
    for i in range(1, n+1):
        total += i
    return total
    
print(normal_sum(10))
print(normal_sum(100))



# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))