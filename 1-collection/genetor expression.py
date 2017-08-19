
#数组
o_list = [1,5,6,2,57,7,4]
a_list = [a for a in o_list if a > 2]

#filter
b_list = list(filter(lambda x: x >= 0, o_list))

print(b_list)

#字典
dict = {"key1": 1, "key2": 2, "key3": 30}
dictM = {k:v for k,v in dict.items() if v < 10}
print(dictM)
#Set

set = {1,3,10,20023,2}
setM = {a for a in set if a  > 2}
print(setM)

