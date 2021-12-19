age = input("나이는? ")
age_digit = int(age)

if age_digit >= 19 :
    print("당신은 19세 이상 성인입니다")
    
if age_digit != 0 and age_digit >= 19 :
    print("당신은 0살이상이고 19세 이상입니다")
    
if age_digit >= 0 and age_digit < 19 :
    print("당신은 미성년자입니다")
    
if age_digit == 19 or age_digit > 19:
    print("당신은 성인")
    
if not age_digit > 19 :
    print("not 19세보다 작네용")

if age_digit == 0 :
    print("0살 입니다")
elif age_digit == 19 :
    print("19살 입니다")
else :
    print("0살 이나 19살이 아닙니다")
    
