# random 모듈을 불러옵니다.
import random
# 게임을 계속 진행하기 위한 while 루프입니다
while True:
    # 컴퓨터가 1부터 10 사이의 랜덤한 숫자를 생성합니다
    computer_number = random.randint(1, 10)

    # 게임 시작 메시지를 출력합니다
    print("1과 10 사이의 숫자를 하나 정했습니다.")
    print("이 숫자는 무엇일까요?")
    
    # 정답을 맞출 때까지 반복하는 while 루프입니다
    while True:
        # 플레이어에게 숫자 입력을 요청합니다
        player_input = input("예상 숫자: ")

        # 입력된 값이 숫자인지 확인합니다(유효성검사)
        if player_input.isdigit():
            # 입력받은 문자열을 정수로 변환합니다
            player_number = int(player_input)

            # 입력한 숫자가 정답보다 큰 경우
            if player_number > computer_number:
                print("너무 큽니다. 다시 입력하세요.")
            # 입력한 숫자가 정답보다 작은 경우
            elif player_number < computer_number:
                print("너무 작습니다. 다시 입력하세요.")
            # 정답을 맞힌 경우
            else:
                print("정답입니다!")
                break  # 정답을 맞췄으므로 숫자 맞추기를 종료합니다
        # 입력된 값이 숫자가 아닌 경우
        else:
            print("숫자를 입력해주세요.")

    # 게임을 다시 할지 물어봅니다
    print("게임을 다시하시겠습니까? (y/n)")
    
    # 사용자의 선택을 입력받습니다
    play_again = input()

    # y가 아닌 다른 값을 입력하면 게임을 종료합니다
    if play_again.lower() != 'y':
        break  # 게임을 더 이상 진행하지 않고 완전히 종료합니다

# 게임 종료 메시지를 출력합니다
print('게임을 종료합니다. 즐거우셨나요? 또 만나요!')
