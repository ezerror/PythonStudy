#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
	return int(reduce(lambda x,y:x+y,s.replace('.','')))/pow(10,len(s)-s.index('.')-1)
print('str2float(\'123.456\') =', str2float('1253.456'))