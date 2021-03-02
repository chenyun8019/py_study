'''
author：chenyun
func：解包
'''


def get_name(a,b,c,d,e):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
    print('e=',e)

# name = ('孙悟空','唐僧','猪八戒','沙和尚','白龙马')
# get_name(*name)
a = ['赵','钱','孙','李','陈']
get_name(*a)