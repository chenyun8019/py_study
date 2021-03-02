'''
author:chenyun
data:2021/1/12 9:18
functoin:
1、单行注释和多行注释
2、流程控制语句
'''
# 定义列表----单行注释
list_goods = [('苹果','20'),('香蕉','30'),('橘子','40')]
for goods in list_goods:
    print('商品名称为:'+goods[0]+';商品价格为:'+goods[1])
'''
通过while循环，使程序循环运行----多行注释
'''
while True:
    GoodsName = input('请输入商品名称:')
    GoodsNum = int(input('请输入商品数量:'))
    if GoodsName == '苹果':
        total_price = GoodsNum * 10
        print(total_price)
    elif GoodsName == '香蕉':
        total_price = GoodsNum * 20
        print(total_price)
    else:
        print('您输入的商品名称在系统中不存在，请重新输入')


