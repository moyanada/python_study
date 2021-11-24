#리스트
location = ['서울시', '경기도', '인천시']
print(location)
#리스트 추가하기
location.append('부산시')
print(location)
print(location.pop())
print(location)
print(location.pop(1))
print(location)
#삭제 remove
location.remove('인천시')
print(location)
location.append('부산시')
print(location)
location.append('경기도')
print(location)
#삭제 del
del location[0]
print(location)
#삽입 insert
location.insert(0, "서울시")
print(location)
#수정
location[1] = '경기도'
location[2] = '부산시'
print(location)

#정렬
numbers = [2, 1, 4, 3]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#빈 리스트 정의 [] 해도 되지만 list() 이렇게 정의하라고 권장함
location = list()

#문자열 자르기
location = "python is easy"
print(location.split())
print(location)
location = location.split()
print(location)
location = "python, is, easy"
print(location.split(','))