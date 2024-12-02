import random

while True:  # 게임을 계속 반복
    computer_number = random.randint(1, 10)  # 컴퓨터가 1부터 10 사이의 숫자를 선택
    print("1과 10 사이의 숫자를 하나 정했습니다.")
    print("이 숫자는 무엇일까요?")

    while True:  # 플레이어가 숫자를 맞출 때까지 반복
        player_input = input("예상 숫자: ")  # 플레이어로부터 숫자 입력 받기

        if not player_input.isdigit():  # 입력이 숫자가 아닌 경우
            print("숫자를 입력해주세요.")
            continue

        player_number = int(player_input)  # 입력을 정수로 변환

        if not (1 <= player_number <= 10):  # 입력이 1에서 10 사이가 아닌 경우
            print("숫자를 1에서 10 사이로 입력해주세요.")
            continue

        if player_number == computer_number:  # 플레이어가 숫자를 맞춘 경우
            print("정답입니다!")
            break
        elif player_number > computer_number:  # 입력한 숫자가 큰 경우
            print("너무 큽니다. 다시 입력하세요.")
        else:  # 입력한 숫자가 작은 경우
            print("너무 작습니다. 다시 입력하세요.")

    while True:  # 게임을 다시 할지 물어봄
        play_again = input("게임을 다시하시겠습니까? (y/n): ").lower()
        if play_again in ['y', 'n']:  # 유효한 입력인지 확인
            break
        print("y 또는 n을 입력해주세요.")

    if play_again == 'n':  # 'n'을 입력하면 게임 종료
        print('게임을 종료합니다. 즐거우셨나요? 또 만나요!')
        break
