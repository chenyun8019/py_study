'''
author:chenyun
data:2021/1/12 11:23
functoin:''
1、关键字
2、定义标识符时，不可使用关键字
3、格式化输出方式
'''
# import keyword
# keyword_list = keyword.kwlist
# print(keyword_list)
# uname = '孙悟空'
# age = 1000
# print('我是%s' %uname)
# print(f'我是{uname}')
#
# print('姓名为：%s 年龄为：%d' %(uname,age))
# print(f'姓名为：{uname} 年龄为：{age}')
#
# PI = 3.1415926
# print('这是圆周率:%f' %PI)
# print('这是圆周率:%.f' %PI)
# print('这是圆周率:%.2f' %PI)
uname = 'Tom'
QQ = '283419440'
phone = '137000000001'
address = '北京市大兴区林校路街道'
print("="*10+'我的名片'+"="*10)
print('姓名：'+uname)
print('QQ：'+QQ)
print('手机号：'+phone)
print('地址：'+address)
print("="*27)

print("="*10+'我的名片'+"="*10)
print('姓名：%s'%uname)
print('QQ：%s'%QQ)
print('手机号：%s'%phone)
print('地址：%s'%address)
print("="*27)

a = input('请输入您的姓名：')
print('您输入的姓名为：'+a)  # input函数获取的值都是字符串类型