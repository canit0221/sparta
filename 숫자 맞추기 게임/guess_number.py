import random

# 게임종료후 y를 입력하면 처음부터 다시시작
while True:
    # 컴퓨터가 1부터 10 사이의 랜덤한 숫자를 생성
    컴퓨터_숫자 = random.randint(1, 10)
    print("1과 10 사이의 숫자를 하나 정했습니다.")
    print("이 숫자는 무엇일까요?")

    # 플레이어가 정답을 입력할때까지 반복
    while True:
        # 플레이어가 숫자를 입력
        플레이어_숫자_입력 = input("예상 숫자: ")
        # 입력이 숫자인지 확인(유효성검사)
        if 플레이어_숫자_입력.isdigit():
            플레이어_숫자 = int(플레이어_숫자_입력)
            # 입력한 숫자가 범위 내에 있는지 확인
            if 1 <= 플레이어_숫자 <= 10:
                break  # 유효한 입력, 다음 단계로 진행
            else:
                print("숫자를 1에서 10 사이로 입력해주세요.")
        else:
            print("숫자를 입력해주세요.")

    # 입력한 숫자가 큰지 작은지 힌트를 얻습니다.
    while True:
        if 플레이어_숫자 == 컴퓨터_숫자:
            print("정답입니다!")
            break  # 정답, 게임 종료
        elif 플레이어_숫자 > 컴퓨터_숫자:
            print("너무 큽니다. 다시 입력하세요.")
        else:
            print("너무 작습니다. 다시 입력하세요.")

        # 플레이어가 숫자를 입력
        플레이어_숫자_입력 = input("예상 숫자: ")
        # 입력이 숫자인지 확인(유효성검사)
        if 플레이어_숫자_입력.isdigit():
            플레이어_숫자 = int(플레이어_숫자_입력)
            # 입력한 숫자가 범위 내에 있는지 확인
            if 1 <= 플레이어_숫자 <= 10:
                continue  # 유효한 입력, 정답 확인 반복
            else:
                print("숫자를 1에서 10 사이로 입력해주세요.")
        else:
            print("숫자를 입력해주세요.")

    print("게임을 다시하시겠습니까? (y/n)")

    while True:
        play_again = input()

        if play_again.lower() not in ['y', 'n']:  # 플레이어가 y,n만 입력했는지 확인
            print("y 또는 n을 입력해주세요.")
            continue
        else:
            break

    if play_again.lower() == 'y':  # y를 입력하면 게임을 처음부터 다시실행.
        continue
    elif play_again.lower() == 'n':  # n을 입력하면 게임 종료
        print('게임을 종료합니다. 즐거우셨나요? 또 만나요!')
        break
