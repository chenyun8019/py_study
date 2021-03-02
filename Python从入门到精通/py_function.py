'''
author:chenyun
data:2021/1/12 22:32
functoin:''
'''
# a = '*'
# print('%5s'%a )

def set_name():
    '''
    这是一个自定义函数，用来设置姓名
    '''
    print('函数的定义和调用')
    a = 1+4
    print(a)
# 函数调用
set_name()

def business_card():
    uname = 'Tom'
    QQ = '283419440'
    phone = '137000000001'
    address = '北京市大兴区林校路街道'
    print("=" * 10 + '我的名片' + "=" * 10)
    print('姓名：' + uname)
    print('QQ：' + QQ)
    print('手机号：' + phone)
    print('地址：' + address)
    print("=" * 27)

business_card()

# 函数文档注释
help(set_name)
# set_name()
#     这是一个自定义函数，用来设置姓名

# 形参和实参
def say(word):
    print('hello,'+word)

say('python')
say('wolrd')


def add(a,b):
    print('a+b=',a+b)

add(10,20)

def business_card(uname,QQ,phone,address):
    print("=" * 10 + '我的名片' + "=" * 10)
    print('姓名：' + uname)
    print('QQ：' + QQ)
    print('手机号：' + phone)
    print('地址：' + address)
    print("=" * 27)

business_card('chenyun','23456789','13488888888','北京市朝阳区')

def add_1(a,b):
    return a+b

result = add_1(30,20)
print(result)

def max(a,b):
    if a>b:
        return a
    else:
        return b

res = max(80,90)
print(res)