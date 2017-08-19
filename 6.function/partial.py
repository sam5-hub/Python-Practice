import functools

#偏函数
#所以，functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。
int2 = functools.partial(int, base = 2)

print(int2('10'))


def cmp_ignore_case(s1, s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0
	

sorted_ignore_case = functools.partial(sorted, key = str.upper,reverse=True)
#
print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])) 