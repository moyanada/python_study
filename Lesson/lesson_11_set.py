data_set = set()
data_set = set({'apple', 'dell', 'samsung', 'lg'})
print(type(data_set))

#셋 추가
data_set.add('hp')
print(data_set)
#셋 삭제
data_set.remove('hp')
print(data_set)

#집합에 apple 이 있니?
print('apple' in data_set)

if 'apple' in data_set:
    print('잇다');

data1 = {'apple', 'samsung', 'lg'}      #스마트폰 생산 업체
data2 = {'samsung', 'lg', 'xaiomi'}    #TV 생산 업체

#교집합 스마트폰과 tv생산을 둘다하는 업체
print(data1 & data2)

#합집합
print(data1 | data2)

#차집합
print(data1 - data2)

#교집합을 뺀 나머지
print(data1 ^ data2)

#중복 제거
data_set = set({'apple', 'dell', 'samsung', 'lg','apple', 'dell', 'samsung', 'lg','apple', 'dell', 'samsung', 'lg'})

print(data_set)