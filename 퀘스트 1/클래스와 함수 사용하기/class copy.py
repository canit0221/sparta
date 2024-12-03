class Person:
    """사람의 기본 정보를 저장하고 관리하는 클래스"""
    
    def __init__(self):
        """
        Person 클래스의 생성자
        이름, 나이, 성별을 입력받아 초기화
        """
        self.name = input("이름: ")
        self.age = self.validate_age()
        self.gender = self.validate_gender()

    def validate_age(self):
        """
        나이 입력값의 유효성을 검사하는 메서드
        Returns:
            int: 유효한 나이 값
        """
        while True:
            try:
                age = int(input("나이: "))
                if age > 0:
                    return age
                else:
                    print("유효하지 않은 나이입니다.")
            except ValueError:
                print("숫자만 입력해주세요.")

    def validate_gender(self):
        """
        성별 입력값의 유효성을 검사하는 메서드
        Returns:
            str: 'male' 또는 'female'
        """
        while True:
            gender = input("성별: ").lower()
            if gender in ['male', 'female']:
                return gender
            print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.")

    def display(self):
        """사용자 정보를 화면에 출력하는 메서드"""
        print(f"이름: {self.name}, 성별: {self.gender}\n나이: {self.age}")

    def greet(self):
        """
        나이에 따라 다른 인사말을 출력하는 메서드
        14세 미만: 어린이
        14-19세: 학생
        20세 이상: 성인
        """
        if self.age < 14:
            print(f"안녕하세요, {self.name} 어린이!")
        elif self.age < 20:
            print(f"안녕하세요, {self.name} 학생!")
        else:
            print(f"안녕하세요, {self.name}님!")

# Person 클래스의 인스턴스 생성 및 메서드 호출
p1 = Person()
p1.display()
p1.greet()


