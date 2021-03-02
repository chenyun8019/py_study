'''
author:chenyun
data:2021/1/12 22:22
functoin:''不可以
1、int()将数据转换成数字 int(qwe)方式
2、float() 将数据转换成浮点数
3、str()将数据转换成字符串
'''
a = 123
b = '123'
print(str(a)+b)
print(a+int(b))
print(a+float(b))

a = True
print(int(a))