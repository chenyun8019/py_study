#无参数的函数
def fun1():
    print('a = ',1)
    name = 'wukong'
    print('欢迎',name,'光临')

#待参数的函数
def fun2(a,b):
    result = a + b
    return result

def fun3(a,b,*c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

def fun4(*a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

def fun5(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)


#以下为方法调用
# fun1()
# result = fun2(3,8)
# print(result)
# fun3(3,4,5,6,7)
# fun4(3,4,5,6,7,8,b=9,c=10)

t=(1,2,3,4)
fun5(*t)


