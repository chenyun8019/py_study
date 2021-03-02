#if语句

age=12
if age>18:
    print('你的年龄不满18岁')
else:
    print('你的年龄满了18岁')

# i=1
# while (i<5):
#     j = 1
#     while (j < i+1):
#         print("*",end='')
#         j += 1
#     print()
#     i += 1
#
# i=1
# while (i<5):
#     j = 1
#     while (j < 5):
#         print("*",end='')
#         j += 1
#     print()
#     i += 1
# from time import time
#
# stime=time()
# i=2
# while (i<100):
#     flag = True
#     j=2
#     while(j <= i ** 0.5):
#         if (i % j ==0):
#             flag =False
#             # break;
#         j += 1
#     if flag:
#         pass
#         # print(i)
#     i += 1
# etime=time()
# print("用时:",(etime-stime),"秒钟")

#流程语句
#coding=UTF-8

#if语句
# age = input("请输入年龄:")
# if age >18:
#     print("年龄大于18岁")
# else:
#     print("年龄小于18岁")

# #if...else语句
# score=input("请输入您的分数:")
# if score >= 90:
#     print("优良")
# elif 80 < score <= 90:
#     print("优良")
# elif 70 < score <= 80:
#     print("中等")
# else:
#     print("分数不及格")

# while循环
# i=1
# result = 0
# while (i <= 3):
#     result += i
#     i += 1
# print(result)

i=0
while (i<8):
    j = 1
    while (j < 4):
        print("*",end='')
        j += 1
    print()
    i += 1


'''
print('—'*20,'欢迎光临《唐僧大战白骨精》','—'*20)
print("请选择您的身份:")
print( '\t 1、唐僧')
print( '\t 2、白骨精')

player_choose= input("请选择(1-2):")
print( '—'*66)
if player_choose == '1':
    print("你已经选择:唐僧,恭喜你以 唐僧的身份进行游戏！")
elif player_choose == '2':
    print("你已经选择 白骨精,系统分配以 唐僧的身份进行游戏！")
else:
    print("您输入的角色有误，系统自动分配以 唐僧的身份进行游戏！")
#玩家生命力和攻击力
player_life = 2
player_attack = 2

#boss生命力和攻击力
boss_life = 10
boss_attack = 10

print(f'唐僧,您的生命力为{player_life},您的攻击力为{player_attack}')

while True:
    print('—'*66)
    print("请选择您要做的操作:")
    print( '\t 1、练级')
    print( '\t 2、打Boss')
    print( '\t 3、逃跑')
    st1= input("请选择(1-3):")

    if st1 == '1':
        player_life += 2
        player_attack += 2
        print(f'唐僧,您的生命力为{player_life},您的攻击力为{player_attack}')
    elif st1 == '2':
        boss_life -= player_attack
        print(f'白骨精，受到{player_attack}伤害,生命力为{boss_life}')
        if (boss_life <= 0):
            print(f'白骨精，一共受到{boss_attack}伤害,白骨精死了')
            break

'''