#coding:utf8
my_list=['孙悟空','唐僧','猪八戒','沙和尚','白龙马','白骨精','蜘蛛精','铁扇公主']
# print(my_list)
# print(my_list[3])
# print(len(my_list))
# print(my_list[1:6:3])
# print(my_list.index('白龙马'))
# my_list[0]='sunwukong'
# print(my_list)
print('打印切片前的:',my_list[:4])
print('打印切片后的',my_list[5:])
print('复制切片列表',my_list[:])
print(len(my_list))
i=0
while(i < len(my_list)):
    print(my_list[i])
    i += 1

print('索引为负数:',my_list[-3])

my_list_add=['如来佛','观世音']
print(my_list_add*2)
print(my_list + my_list_add)

print('观世音' in my_list_add)
print('观世音' not in my_list_add)