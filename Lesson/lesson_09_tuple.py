

#튜플
data = (1, 2, 3)
data = tuple((1, 2, 3))
print(type(data))

for i in data :
    print("tuple : ", i)

#튜플은 삭제나 추가가 불가능함
print(data[1])
data[1] = 99
print(data[1])

def mul_return(a, b):
    return a, b

data = mul_return(1, 2)
print(data[0])

#독특한 +, *
data1 = (1,2,3)
data2 = (4,5,6)
data3 = data1 + data2
print(data1 + data2)
print(data1 * 3)
print(data3)

#변수값을 바꿀때

#일반적인 방법
x = 1
y = 2
print(x, y)

tmp = x
x = y
y = tmp
print(x, y)

#튜플이용 방법
x, y = y, x #요게 튜플로 생각하고 뒤집어줌
print(x, y)

#리스트와 튜플은 변환이 가능함

data = (1,2,3)
data_list = list(data)
print(type(data_list))

data_tuple = tuple(data_list)
print(type(data_tuple))
