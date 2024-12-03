class Person:  # Person 클래스 생성
    def __init__(self):  # 클래스 초기 실행 함수
        self.name = input("이름: ")  # 이름 입력 및 저장
        
        # 나이 유효성 검사 반복문 시작
        while True:
            try: # 숫자만 입력받기
                age = int(input("나이: ")) # 나이 입력 받고 정수 변환
                if age > 0:  # 나이가 0보다 크면
                    self.age = age # 나이 저장
                    break # 반복문 종료
                else: # 나이가 0보다 작으면
                    print("유효하지 않은 나이입니다.") # 안내문
            except ValueError: # 숫자 외 입력 예외 처리
                print("숫자만 입력해주세요.") # 안내문
        
        while True:  # 성별 유효성 검사 반복문 시작
            gender = input("성별: ").lower()  # 성별 입력 후 소문자 변환
            if gender in ['male', 'female']:  # male 또는 female 입력 검사
                self.gender = gender  # 성별 저장
                break  # 반복문 종료
            print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")  # 안내문

    def display(self):  # 정보 출력 함수
        print(f"이름: {self.name}, 성별: {self.gender}\n나이: {self.age}")  # 저장된 정보 출력
    
    def greet(self):  # 인사 기능 함수
        if self.age < 14:  # 어린이 조건
            print(f"안녕하세요, {self.name} 어린이!")  # 어린이 인사말 출력 
        elif self.age < 20:  # 청소년 조건
            print(f"안녕하세요, {self.name} 학생!")  # 청소년 인사말 출력
        else:  # 성인 여부 확인
            print(f"안녕하세요, {self.name}님!")  # 성인 인사말 출력

p1 = Person()  # Person 클래스 객체 생성
p1.display()  # 객체 정보 출력
p1.greet()  # 인사말 출력


