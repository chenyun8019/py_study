# coding = utf-8
'''
作者：chenyun
日期：2020-08-05
功能：I/O基本操作
r'路径1\路径2'
pip install xlrd
'''
# ..代表从当前目录跳出来，返回到上一级目录，返回几级，写几个.
import os
file_name = '../config/sample.txt'
# file_name = 'C:\\Users\\chenyun\Desktop\\2020-08-07-11-49-45.png'
# obj = open(file_name)
# text=obj.read()
# print(text)
# obj.close()
# text=obj.read() 关闭的文件不可读取

# 捕获异常方式
#读取二进制文件
# with open(file_name,'rb') as oo:
#     chunk = 1024 * 20
#     t = oo.read(chunk)
#     print(t[0])

#读取txt文件
# try:
#     with open(file_name,mode='w',encoding='utf-8') as obj:
#
#         text = '锄禾日当午\n' \
#                '汗滴禾下土\n' \
#                '谁知盘中餐\n' \
#                '粒粒皆辛苦'
#         # print(obj.read())
#         # print(obj.read(5))
#         obj.write(text)
#         obj.close()
# except FileNotFoundError:
#     print(f'{file_name} 文件不存在')
#
#
# file_path = os.path.dirname(os.path.abspath('.'))
# print(file_path)

#读取excel文件
# import xlrd
#
# data = xlrd.open_workbook(r'C:\Users\chenyun\Desktop\test_xlrd.xls')
# table1 = data.sheet_by_index(0)
# # print(table1.cell_value(0,2))
# # print(table1.cell(0,2))
# # print(table1.ncols)
# # print(table1.nrows)
# count = 0
# for i in range(1,table1.nrows):
#     count =count +1
#
#     tr_data = table1.cell_value(i,1)
#     print('第',count,'行的值是：'+tr_data)

#读取诗歌

# with open(file_name,encoding='utf-8') as uu:

    # while True:
    #     content = uu.read(5)
    #     print(content,end='')
    #     print()
    #     print('当前读到了的位置为:',uu.tell())
    #     if not content:
    #         break

    # uu.seek(12)
    # c = uu.read(3)
    # print(c)

#获取到该路径下目录结构，默认路径为. 当前目录
r = os.listdir()
# r = os.path.curdir
# os.mkdir('reer')
# os.rmdir('reer')
os.rename('流程控制语句.py','11流程控制语句.py')
r = os.listdir()

print(r)



