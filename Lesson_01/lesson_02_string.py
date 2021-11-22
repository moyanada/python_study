some_string = "python"
#문자열 길이
print (len(some_string))

# """ """ 이걸로 문자열 여러줄 감싸짐
some_string = """
    zzzzz wow 
    zzzz
    ddd
    fff
    ggg
"""

print(some_string)
print(len(some_string))
#해당 변수중 문자열 갯수 세기
print(some_string.count("zzzz"));
print(some_string.count("z"));
#fff가 처음 나오는 인덱스 번호
print(some_string.find("fff"));
print(some_string[37])
#fff > replace 문자열로 변경
print(some_string.replace("fff", "replace"))
#some_string에 안넣어줬기 때문에 some_string은 replace전 문자열
print(some_string)

some_string = some_string.replace("fff", "replace")
print(some_string)

some_string = "python"

print(some_string[0])
print(some_string[1])
#뒤에서부터 샘
print(some_string[-5])
print(some_string[0:2])
print(some_string[1:2])

print(some_string + 'zz')