'''
상속

형식:
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스):
    본문
'''
class Person:
    def __init__(self, name, age):
        self.name = name

    def eat(self, food):
        print(f'{self.name}이 {food}를 먹습니다.')

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(f'{self.name}은 {self.school}에서 공부를 합니다.')


    def eat(self, food):
        super().eat(food)


# 객체 생성
potter = Student('헤리 포터', '호그와트')
potter.eat('감자')
potter.study()

'''
1. 서브 클래스의 __init__()
    서브 클래스는 슈퍼클래스가 없으면 존재할 수 없습니다. 그래서 서브 클래스의 생성자를 구현할 때는 '반드시 슈퍼클래스의 생성자를 먼저 호출'하는 코드를 작성해야만 합니다. 
    
    super(). 에서 super -> 슈퍼 클래스를 의미.즉 이상의 코드에서 Student 의 생성자를 호출할려면 super().__init__(name)에 의해서 슈퍼클래스인 Person의 생성자가 먼저 호출되면 '슈퍼클래스'의 객첵 먼저 생성됩니다.
    이후에 슈퍼클래스에서 생성된 인스턴스 변수인 name이 서브클래스로 전달되고, 이후에 서브클래스 에서 school 인스턴스 변수를 선언 및 초기화하여 저장하면서 서브 클래스의 인스턴스가 생성됩니다. 
   
    
2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스 
    하지만 서브 클래스의 인스턴스는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스 
    Student 클래스이 객체는 Student의 인스턴스 이면서 Person의 인스턴스
    
    Java를 기준으로 instanceof 연산자 역할을 하는 함수가 python에도 있는데 -> isinstance() : 다 소문자 입니다. 
    
    형식: 
        isinstance(객체명, 클래스명) -> boolean
'''
print(isinstance(potter, Person))   # 결과값: True
print(isinstance(potter, Student))


'''
지시 사항
1. 다음과 같은 슈퍼클래스 Car를 가지고 있는 Hybird 클래스를 구현하시오.
2. 서브 클래스 Hybird는 다음과 같은 특지을 지니고 있습니다.
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량을 초과할수 없고, 0보다 작은 값으로 충전할수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할수 있는 Hybird_info() 메서드가 있습니다. 
    
    
3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil=0, amount=0)
car.add_oil(100)
car.charge(50)
car.Hybrid_info()


실행 예

하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30
'''

class Car:
    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유 상태: {self.oil}')

class Hybrid(Car):
    pass

car = Hybrid(0)
car.add_oil(100)
car.cahrge(50)
car.hybrid_info()

'''
지시시항 
1. 슈퍼클래스 Shape를 정의하시오.
    -생성자에 name을 인스턴스 변수로 설정
    -draw() 메서드를 정의하여 self.name을 출력하시오(call1() 유형)
2. Shape 클래스를 상속 받는 서브 클래스 Circle를 정의하시오.
    -Circle은 radius(반지름) 속성을 추가로 가집니다.
    -생성자에서 radius도 추가할 것.
    -area() 메서드를 정의하여 원의 넓이를 계산하고 return 할 것.
        (넓이 = 3.14 * radius * radius)
3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의하시오.
    -Rectangle은 width / height를 초기화 할것
    -area() 메서드를 정의하여 사각형의 넓이를 계산하고 return 할 것
        (넓이 = 너비 * 높이)
4. Circle과 Rectangle의 draw() 메서드를 오버라이딩 하여 각각의 넓이를 출력할 것. 

circle = Circle('원', 5)
circle.draw()
print(f'원의 넓이: {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직 사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5억인 원1이 생성되었습니다.
이르밍 원1인 원의 넓이는 ____ 입니다.
원의 넓이: ___
너비가 10, 높이가 9인 직사각형1이 생성되었습니다. 
이름이 직사각형1인 직사각형의 넓이는 ___입니다.
직사각형 넓이: ___

'''
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(self.name)


class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f'반지름이 {self.radius}인 원이 생성되었습니다.')

    def draw(self):
        super().draw()
        print(f'원의넓이: {self.area}인 원이 넓이는 {self.area()}입니다.')

    def area(self):
        return (self.radius**2)*3.14


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f'너비가{self.width}, 높이가인 원이 생성되었습니다.')


    def draw(self):
        print(f'이름이{self.width}')

