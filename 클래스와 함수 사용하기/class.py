class Person:  # Person 클래스 생성
    def __init__(self):  # 클래스 초기 실행 함수
        self.name = input("이름: ")  # 이름 입력 및 저장
        self.age = int(input("나이: "))  # 나이 입력 후 정수 변환
        
        while True:  # 반복문 시작
            gender = input("성별: ").lower()  # 성별 입력 후 소문자 변환
            if gender in ['male', 'female']:  # male 또는 female 입력 검사
                self.gender = '남성' if gender == 'male' else '여성'  # 영문 성별의 한글 변환
                break  # 반복문 종료
            print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")  # 잘못된 입력 메시지 출력

    def display(self):  # 정보 출력 함수
        print(f"이름: {self.name}, 성별: {self.gender}\n나이: {self.age}")  # 저장된 정보 출력
    
    def greet(self):  # 인사 기능 함수
        if self.age >= 20:  # 성인 여부 확인
            print(f"안녕하세요, {self.name}! 성인이시군요!")  # 성인 인사말 출력
        else:  # 미성년자 조건
            print(f"안녕하세요, {self.name}! 미성년자시군요!")  # 미성년자 인사말 출력

p1 = Person()  # Person 클래스 객체 생성
p1.display()  # 객체 정보 출력
p1.greet()  # 인사말 출력


