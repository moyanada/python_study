#반복문
for i in range(10):
    print(i)

for i in ["111", "2222", "3333"] :
    print(i)

sum = 0
for i in range(1, 11):
    sum += i
    print(sum)
    
i = 0
while i <= 3:
    print(i)
    i = i+1
    
exchange = {'달러':1112, '위안':171, '엔':1010}
# prices = input()
prices = '1001달러'
for exchange_item in exchange.keys():
    print(exchange[exchange_item])
    if prices[4:] == exchange_item:
        print (int(prices[:4]) * exchange[exchange_item], '원')





