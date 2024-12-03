import random # random 라이브러리 불러오기

while True:  # 게임을 계속 반복
    computer_number = random.randint(1, 10)  # 컴퓨터가 1부터 10 까지의 숫자를 랜덤으로 선택
    print("1과 10 사이의 숫자를 하나 정했습니다.") # 입력 안내 문구 출력
    print("이 숫자는 무엇일까요?") # 입력 안내 문구 출력

    while True:  # 플레이어가 숫자를 맞출 때까지 반복
        player_input = input("예상 숫자: ")  # 플레이어로부터 숫자 입력 받기

        if not player_input.isdigit():  # 입력이 숫자가 아닌 경우 (유효성검사)
            print("숫자를 입력해주세요.") # 안내 문구를 출력
            continue  # 루프문으로 처음으로 돌아감

        player_number = int(player_input)  # 입력을 정수로 변환

        if not (1 <= player_number <= 10):  # 입력이 1에서 10 사이가 아닌 경우 (유효성검사)
            print("숫자를 1에서 10 사이로 입력해주세요.") # 안내 문구를 출력
            continue # 루프문으로 처음으로 돌아감


        if player_number == computer_number:  # 플레이어가 숫자를 맞춘 경우 (유효성검사 통과 후)
            print("정답입니다!") # 해당문구를 출력
            break # 숫자맞추기 반복 종료후 다음루프로
        elif player_number > computer_number:  # 입력한 숫자가 큰 경우
            print("너무 큽니다. 다시 입력하세요.") # 안내 문구를 출력하고 루프
        else:  # 입력한 숫자가 작은 경우
            print("너무 작습니다. 다시 입력하세요.") # 안내 문구를 출력하고 다시 루프

    while True:  # 게임을 다시 할지 물어봄
        play_again = input("게임을 다시하시겠습니까? (y/n): ").lower() # 플레이어로 부터 계속할지 입력받기
        if play_again in ['y', 'n']:  # 입력이 y,n인지 확인 (유효성검사)
            break # 입력이 y거나 n이면 유효성검사 루프 탈출
        print("y 또는 n을 입력해주세요.") # 입력이 y,n중에 없으면 안내 문구 출력

    if play_again == 'n':  # 입력값이 n이면 게임 종료, y였다면 맨처음 루프로 이동해서 게임 다시 반복
        print('게임을 종료합니다. 즐거우셨나요? 또 만나요!')
        break # 입력값이 n이면 게임반복루프 탈출후 게임종료
