from one_cal import OneCal
from two_cal import TwoCal

one_cal = OneCal(4, 2)
print("one_cal.add : ", one_cal.add())
two_cal = TwoCal(5, 2)
print("two_cal.add : ",two_cal.add())
print("two_cal.minus : ",two_cal.minus())

from custom_class import CustomClass

print(CustomClass.add_instance_method(None, 3, 5))
# print(CustomClass.add_class_method(CustomClass, 3, 5))
print(CustomClass.add_class_method(3, 5))
print(CustomClass.add_static_method(3, 5))

from language_test import *
a = KoreanLanguage.static_my_language()
b = KoreanLanguage.class_my_language()
a.print_language()
b.print_language()