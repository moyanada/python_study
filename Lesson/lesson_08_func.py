
def func_1():
    print('func이니??')
    
func_1()

def func_2(pParam1, pParam2):
    print(pParam1 + pParam2)

func_2('hellow', 'world!!');

def func_3(pParam):
    pParam = 20
    return pParam

result_func = func_3(40)
print(result_func)

#멀티 리턴도 되나요?
def func_4(pParam1):
    b = pParam1 + 1
    return pParam1, b

#리스트로 안나오고 ()로 나오네 ?? 괄호는 머냥? 
result_func = func_4(40)
print(result_func)