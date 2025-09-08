'''
1. while 반복문
 while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨(조건문이 False가 될때까지)
 형식: while 조건식1:
    반복 실행문

당연히 특정 시점에 while 반복문이 종료될수 있도록 지정해두셔야 합니다.

'''

n1 = 1
while n1 < 11:
    print(n1)
    n1 += 1         # python에는 ++가 없습니다..


'''
기본 예제
10부터 1까지 역순으로 출력하시오

'''
n2 = 10
while n2 > 0:
    print(n2)
    n2 -= 1
    # print(n2)를 n2 -= 1 밑에 적으니깐, 9부터 0까지만 출력이 된다. 10은 출력이 안된다. 하지만 위에 print(n2)를 적으니깐 10부터 1까지 출력된다. 아 그럴만하네. print(n2)를 먼저 적으니깐 10이 먼저 출력되고, 그다음 밑에 n2 -= 1 조건식을 계산하는듯 하다. 반대로 적으니깐 계산 먼저 하고 나온다.


'''
중첩 while문 (while문 뿐만 아니라 내부에 if를 쓸 수도 있겠습니다)
중첩 while 및 f-string을 활용하여 

기본 예제
구구단 2단부터 9단까지 출력하는 프로그램을 작성하시오. (while 문 사용할것)
변수명은 dan / number로 하겠습니다. 
실행 예
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
9 x 8 = 72
9 x 9 = 81
'''

dan = 2
while dan < 10:
    number = 1
    while number < 10:
        result = dan * number
        print(f'{dan} X {number} = {result}')
        number += 1
    dan += 1

    print(number)


