'''
외부 패키지의 설치 # 1 : settings 를 통한 방법
좌측상단 메뉴버튼 -> file -> settings(혹은 alt + ctrl + s)
좌측 리스트에서 project: 프로젝트명 으로 되어있는 부분 클릭
-> python interperter 클릭
-> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 설치

외부 패키지의 설치 # 2 : 터미널을 이용하는 방법
alt + f12 눌러서 터미널 연다.
pip install prettytable

'''
from prettytable import PrettyTable

from pokemon_data import pokemon_data

# PrettyTable 의 객체 생성
table = PrettyTable()
table.field_names = [ '번호', '이름', '타입']

print(pokemon_data)
table.field_names = [ '번호', '이름', '타입']
table.add_row(pokemon_data[0])
table.add_row(pokemon_data[1])
table.add_row(pokemon_data[2])
table.add_row(pokemon_data[3])
table.add_row(pokemon_data[4])
print(table)


table.field_news = [ '이름', '나이', '주소' ]
table.add_row(("김일", 21, "서웉특별시 마포구"))
print(pokemon_data[3][2])
table.add.row(pokemon_data[0][0], pokemon_data[0][1], pokemon_data[0][2])
print(pokemon_data[25])
print(table)


# print(table)



#for pokemon in pokemon_data:
#   table.add_row(pokemon)

# table.add_row((pokemon_data)

print(table)

