print('='*20,'welcom to EMS system','='*20)
emps = ['孙悟空\t20\t男\t水帘洞','唐僧\t30\t男\t东土大唐']
while True:
    print('=' * 63)
    print('请选择要做的操作:')
    print('\t1、查询员工')
    print('\t2、添加员工')
    print('\t3、删除员工')
    print('\t4、退出系统')
    print('=' * 63)
    input_num = input('请选择（1-4）:')
    print('=' * 63)
    if input_num =='1':
        # print('\t序号\t姓名\t年龄\t性别\t住址')
        print('\t序号\t姓名\t年龄\t性别\t住址')
        n =1
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
    elif input_num == '2':
        input_name = input('请输入姓名:')
        input_age = input('请输入年龄:')
        input_sex = input('请输入性别:')
        input_address = input('请输入住址:')
        emps.append(f'{input_name}\t{input_age}\t{input_sex}\t{input_address}')
        print('添加员工成功')
    elif input_num == '3':
        input_delete = int(input('请输入需要删除的用户序号:'))
        if 0 < (input_delete) <= len(emps):
            input_index = input_delete - 1
            emps.pop(input_index)
            print('删除员工成功')
        else:
            print('输入的序号不存在')
    elif input_num == '4':
        print('退出系统')
        print('欢迎再次使用本系统！')
        break
    else:
        print('输入有误，请重新输入')
