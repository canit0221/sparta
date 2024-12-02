import random

while True:  # 전체 게임 루프
    # 게임 초기화
    컴퓨터_숫자 = random.randint(1, 10)
    print("1과 10 사이의 숫자를 하나 정했습니다.")
    print("이 숫자는 무엇일까요?")

    # 숫자 맞추기 루프
    while True:
        # 플레이어 입력 받기
        플레이어_입력 = input("예상 숫자: ")

        if not 플레이어_입력.isdigit():
            print("숫자를 입력해주세요.")
            continue

        플레이어_숫자 = int(플레이어_입력)

        if not (1 <= 플레이어_숫자 <= 10):
            print("숫자를 1에서 10 사이로 입력해주세요.")
            continue

        # 숫자 비교
        if 플레이어_숫자 == 컴퓨터_숫자:
            print("정답입니다!")
            break
        elif 플레이어_숫자 > 컴퓨터_숫자:
            print("너무 큽니다. 다시 입력하세요.")
        else:
            print("너무 작습니다. 다시 입력하세요.")

    # 게임 재시작 확인
    while True:
        play_again = input("게임을 다시하시겠습니까? (y/n): ").lower()
        if play_again in ['y', 'n']:
            break
        print("y 또는 n을 입력해주세요.")

    if play_again == 'n':
        print('게임을 종료합니다. 즐거우셨나요? 또 만나요!')
        break
