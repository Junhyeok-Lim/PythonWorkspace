# print(len([ x for x in range(10000) if '8' not in str(x) ]))

# count=0
# for i in range(1,10001):
#     a=list(str(i))
#     if "8" not in a:
#         count+=1
# print(count)

# sum(list([x for x in range(1000) if x%3==0 or x%5==0]))

# print(str(list(range(1,10001))).count('8'))


# def stringCompress_rec(string):
#     ans = ''
#     count = 1
#     string = string + '\0'
#     for i in range(1, len(string)):
#         if string[i - 1] == string[i]:
#             count += 1
#         else:
#             ans += string[i - 1] + str(count) + stringCompress_rec(string[i:])
#             break
#     return ans

# # 한글 처리 in Atom 1.21.1 + Anaconda(Python 3.6.3)
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# # 다음 입사문제 중에서
# # 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

# import random
# # points = list({1, 3, 4, 8, 13, 17, 20})
# points = list(set(list([random.randint(1,100) for i in range(10)])))
# points.sort()
# print("수직선 위 점들은 ", points)

# # 최소 거리의 점쌍을 모음
# distances = [[points[0], points[1], points[1]-points[0]]]
# for p1 in range(1,len(points)-1):
#     left = points[p1]
#     right = points[p1+1]
#     distance = right - left
#     if distances[0][2] > distance:
#         distances = [[left, right, distance]]
#     elif distances[0][2] == distance:
#         distances += [[left, right, distance]]

# print("가장 짧은 거리는", distances[0][2], ": ", end='')
# for i in range(len(distances)):
#     if i == len(distances)-1:
#         print(distances[i][0],"~",distances[i][1],end='')
#     else:
#         print(distances[i][0],"~",distances[i][1],end=', ')


# nums = [4,-7,9,1,-1,8,-6]
# half_of_nums=[x/2 for x in nums]
# half_of_positive_nums=[x/2 for x in nums if x>=0]


def do(alist):
    return print([x for x in alist if x < 0] + [x for x in alist if x >= 0])

do([-1, 1, 3, -2, 2])