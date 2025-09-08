print ("Hello World")

# 주석 (comment) - 한 줄 주석 / 파이썬 인터프리터가 코드로 인식하지 않음


# 사후 주석 -> 컨트롤 + /
# ```
# 다중주석처리
# ```

print(1) # 숫자 자료형
print('1') # 문자열 자료형

print(1+2)  # 결과값: 3
print('1'+'2') # 결과값: 12

print(type('1'))  # 결과값: <class 'str'>
print(type(1))   # 결과값: <class 'int'>
print(type(1.1)) # 결과값 : <class 'float'>



'''
print(): 콘솔에 출력하는 함수
type(): 소괄호 내에 있는 데이터(argument)가 어떤 자료형인지 알려주는 명령어
  -JS에서는 typeof가 함수가 아니라 연산자였습니다.
'''
'''
print('python 수업을 시작했습니다. 파이팅')
print(```
이렇게 다중으로 작성하고 싶을때는\'\'\'\'\'\' 으로 작성하는 방법도 있습니다.
Java에서는 줄 넘어갈때 마다 + 연결해줘야 했는데 그런점은 편합니다.
)
'''

'''
이상에서 알수있는 점은 print()가 System.out.println()처럼 자동 개행이 된다는 점 입니다.

변수(Variable) : 데이터를 저장하는 바구니
'''

# 변수 선언 및 초기화
# 변수명 = 데이터
name = '김일'
age = 20
print('안녕하세요' + name + '입니다. 나이는' + str(age)+ '살 입니다')

'''
python은 좀 까탈스러워서 Java나 JS할때 처럼 맨 처음이 str이면 뒤의 int/float을 알아서 바꿔주는 짓을 안합니다. 

그때 사용하는 형변환 함수 (conversion)가 있는데 
str() : 다른 데이터를 문자열 자료형으로 바꿔주는 함수
int() : 문자열/실수 자료형을 정수형으로 바꿔주는 함수 / Java : (int) "1.3";
float() : 실수 자료형으로 바꿔주는 함수


근데 귀찮다. 
그래서 f-string 개념이 도입됐습니다. 
'''

print(f'안녕하세요 제 이름은 {name}이고, 나이는 {age}살 입니다.')

'''
혹시 기억하신다면 JS에서 비슷한 개념을 배웠다는 것을 알겁니다. '안녕하세요, 제 이름은 &{name}이고, 나이는 &{age}살 입니다.'); 의 파이썬 판이라고 생각하시면 됩니다. 20250828 md 파일 보면 안다???


Java에서의 scanner 같은 기능을 하는 함수 : input()
'''

name2 = input('이름을 입력하세요>>>')
print(name2)



'''
for 반복문: 
원래 파이썬의 default for문의 경우 enhanced for 가 기본이기는 한데, 저희는 Java / JS 때 일반 반복문을 기준으로 한것부터 학습했기 때문에
동일한 방식으로 나가겠습니다. 

이때 좀 중요한게 rang()라는 함수입니다.
1
2
3
'''
'''
10
출력하는 for 문 작성
'''
'''
for i in range(10):
print(i+1)

이상에서 중요한 것은 마찬가지로 i가 0부터 시작한다는 점입니다. 
이를 Java / JS로 풀면
for (int i = 0; i < 10; i++) {
    System.out.print(i);
}


range(): 몇 번 반복할 것인가를 지정하는 함수 -> 특히 for문과 함께 연계돼서 쓰이는 편입니다. 

range(): 함수의 응용 :
    range((시작값), 종료값, (증감값))
    
시작값:  생략 가능, 생략하면 0부터 시작
종료값: 명시하지않으면 끝까지 진행
증감값: 생략 가능, 생략할 경우에 1씩 증가


for 반복문
형식: 
for i(아무거나 사용가능) in range( 시작값, 종료값, 증감값) :
    반복실행문
'''
for  i in range( 1, 10, 1): # 중요한 점은 종료값 할때 '미만'으로 적용된다는 점입니다. Java 배웠으니까 이부분은 별 문제가 안될것이라고 생각합니다.
    print(i)


'''
 전체 합쳐서 생각했을 때는 그러면 range() 내에 있는 부분이 Java 상에서의 for()의 ()내에 있는 부분을 지정하는 것이라고 볼 수 있겠습니다.
 for( int i =  1; i < 10; i++)   
'''

str_example = '안녕하세요'
for i in str_example:
    print(i)

'''
근데 range()가 필수라는것은 아니고, default 형태로 작성했을때의 형식은 다음과 같습니다.

형식: 
for 변수명 in iterable(반복가능객체):
    반복실행문
    
range() 함수를 쓸 필요 없이 반복 가능 객체(list / tuple / string / set 등)의 처음 부터 끝까지 돌아갑니다. enhanced - for 문과 유사하다고 할수 있습니다. 추후 python collections 수업 후에 적극적으로 응용해서 작성하겠습니다.
'''

num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(1, end='')  # println이 아니라 한 줄에 쓰기 위해서 사용하는 방식 : 추후 수업 예정

print()
print(6)
# print() 함수는 자동 개행이기 때문에 마무리를 사용자화 하고 싶다면 end = 키워드를 쓸수 있습니다. 제 수업때는 별로 안쓸겁니다.


# reeborg's world hurdle # 1
'''python
def turn_right():
    for i in range(3):
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_left()
    
    
while not at_goal():
    if front_is_clear():
        move()
       else:
        jump()
'''


# 이상의 과제에서 수업으로 직접 말하지 않았지만 알수있는점



