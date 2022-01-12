from random import randint


def generate_numbers():
    numbers = []

    while True :
        numbers.append(randint(0,9))
        if len(set(numbers)) == 3:
            numbers = list(set(numbers))
            break

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

print(generate_numbers())