# data = input("주민번호는?")

# print(data.split("-")[0][1])
# print (data.split("-")[1][0])

code = '         000660            '
print(code)
print(code.strip())

#공백하고 #이 둘다 없어짐
code = '         000660#            '
print (code.strip(' #'))

code = '         000660#^&            '
print (code.strip(' #^&'))