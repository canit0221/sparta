import random
# 게임종료후 y를 입력하면 처음부터 다시시작
while True:
  # 컴퓨터가 1부터 10 사이의 랜덤한 숫자를 생성
  computer_number = random.randint(1, 10)

  print("1과 10 사이의 숫자를 하나 정했습니다.")
  print("이 숫자는 무엇일까요?")
  #플레이어가 정답을 입력할때까지 반복
  while True:
      # 플레이어가 숫자를 입력
      player_input = input("예상 숫자: ")

      # 입력이 숫자인지 확인(유효성검사)
      if player_input.isdigit():
          player_number = int(player_input)

          # 입력한 숫자가 큰지 작은지 힌트를 얻습니다.
          if player_number > computer_number:
              print("너무 큽니다. 다시 입력하세요.")
          elif player_number < computer_number:
              print("너무 작습니다. 다시 입력하세요.")
          else:
              print("정답입니다!")
              break  # 플레이어가 숫자를 맞히면 게임 종료
      else:
          print("숫자를 입력해주세요.")

  print("게임을 다시하시겠습니까? (y/n)")

  play_again = input()

  if play_again.lower() != 'y':
    break  # y를 입력하면 게임을 처음부터 다시실행.


#게임 종료
print('게임을 종료합니다. 즐거우셨나요? 또 만나요!')
