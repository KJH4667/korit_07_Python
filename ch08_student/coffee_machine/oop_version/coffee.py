MENU = {
    '에스프레소': {
        '재료': {
            '물':50,
            '커피': 18,
        },
        '가격': 1.5,
    },
    '라떼': {
        '재료':{
            '물': 200,
            '우유': 150,
            '커피': 24,

        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유':  10,
            '커피': 24,
        },
        '가격': 3.0,
    },
}

profit = 0
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100
}

# 실행 예
# 카푸치노 에는 우유가 10ml가 들어갑니다.
# 라고 콘솔에 출력할수 있도록 카푸치노의 우유량을 추출하는 코드를 작성하시오.

# 에스프레소의 가격을 추출하시오.
print(MENU['에스프레소']['가격'])

# 라떼의 재료를 재료 이름만 출력하시오.
# 실행 예
# 물 우유 커피
for key in MENU['라떼']['재료']:    # dictionary 에서 반복문을 돌리게 되면 key가 나온다. 그리고 그 key를 이용해서 value 조회 가능
    print(key, end=' ')

print()

print(' '.join((MENU['라떼']['재료'].keys())) )

'''
38번 라인의 코드 작성 방식의 경우 key를 추출하여 dictionary의 value값에 접근할 수 있습니다. 그렇다면 연산이 가능하다는 의미도 됩니다.
43번 라인의 코드 작성 방식의 경우 value를 추출하는 것이 불가능하지만 한 줄에 간단하게 쓸수있다는 장점이 있습니다 (method를 아는 사람들에게만요)

에스프레소 / 라떼 / 카푸치노를 50잔씩 만든다고 가정했을때 필요한 커피 / 우유 / 물의 양은 얼마인가? 
2500 / 10000 / 12500

'''
print()
coffee = 0
water = 0
milk = 0
for key in MENU: # 결과괎 : 에스프레스 / 라떼 / 카푸치노
    for key_key in MENU[key]['재료']:
        print(MENU[key]['재료'][key_key])
        if key_key == '커피':
            coffee += MENU[key]['재료'][key_key]
        elif key_key == '물':
            water += MENU[key]['재료'][key_key]
        else:
            milk += MENU[key]['재료'][key_key]

print(coffee*50)
print(water*50)
print(milk*50)
'''
이상의 학습 과정에서 중요한 부분은 중첩적으로 이루어진 dictionary - JSON - 기타 collections들이 합쳐진 데이터에서 내가 필요한 부분을 어떻게 추출할수 있을까 입니다.

일반적으로는 list의 경우 index를 이용하기 때문에 반복문 쓰고 치우면 그만인데 반해 dictionary는 반복문을 돌리면 key가 나오게 되고, 그 key를 또 이용해야지만 value가 추출됩니다. 

그리고 그 value를 이용해서 연산을 하거나 로직을 작성해야 하죠.

근데 value가 또 dictionary거나 list거나 혹은 객체거나 한 경우에는 좀 복잡해보입니다. 이를 연습하기 위한 수업이었고, coffee.machine을 작성하면서 중첩 dictionary를 활용하도록 하겠습니다. 
'''


# # 1. 카푸치노의 우유량 추출 및 출력
# milk_amount = MENU['카푸치노']['재료']['우유']
# print(f"카푸치노 에는 우유가 {milk_amount}ml가 들어갑니다.")
#
# # 2. 에스프레소의 가격 추출
# espresso_price = MENU['에스프레소']['가격']
# print(f"에스프레소의 가격은 {espresso_price} 원 입니다.")
#
# # 3. 라떼의 재료 이름만 출력
# latte_ingredients = MENU['라떼']['재료'].keys()
# print("라떼의 재료는 다음과 같습니다:")
# for ingredient in latte_ingredients:
#     print(ingredient)   # -> 챗 지피티 풀이법.

