from random import randint

def generate_numbers():
    numbers = []

    while len(numbers)<3:
        num=randint(0,9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    while len(new_guess)<3 :
        new_num=int(input("{}번째 숫자를 입력하세요:".format(len(new_guess))))

        if new_num<0 or new_num>9:
            print("범위를 벗어났습니다")

        elif new_num in new_guess:
            print("중복되는 숫자입니다.")
        else:
            new_guess.append(new_num)
    
    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i]==solution[i]:
            strike_count += 1
        if guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 테스트 코드
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)
