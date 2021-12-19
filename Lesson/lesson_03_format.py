#문자열포멧
print("i like {}, i have a {}".format("car", "money"))
print("i like {1}, i have a {0}".format("car", "money"))
print("i like {1}, i have a {1}".format("car", "money"))

print("i like %s, i see %s" % ("pen", "apple"))
# %s - string
# %c - character
# %d - int
# %f - float
# 잘안씀

#포멧
interest = 100.097
print (format(interest, ".2f"))