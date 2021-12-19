
#딕셔너리

data_list = list() #리스트
data_tuple = tuple() #튜플
data_dict = dict() #딕셔너리 or data_dict = {}

data_dict = {'한국': 'KR', '일본': 'JP', '중국': 'CN'}
data_dict = dict({'한국': 'KR', '일본': 'JP', '중국': 'CN'})
print(data_dict['한국'])

#추가
data_dict['미국'] = 'US'
print("미국 : ", data_dict)
data_dict['미국'] = 'AS'
print("미국 : ",data_dict)
#삭제
del data_dict['일본']
print(data_dict)
#수정
data_dict['한국'] = 'GOOD'
print(data_dict)
#키는 수정못하니 키삭제하고 넣으세요

#키만 추출하고싶을때
print(data_dict.keys())

for key in data_dict.keys():
    print("키 : ", key)

#값만 추출하고싶을때
print(data_dict.values())

for value in data_dict.values():
    print("값 : ",value)

#item으로 가져오기
print(data_dict.items())

for data in data_dict.items():
    print("타입 : ", type(data))
    print(data[0])

