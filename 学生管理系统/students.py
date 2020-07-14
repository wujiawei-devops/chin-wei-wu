#!/usr/bin/env python3


'''
字段：学生姓名  班级  linux  php  python
stu1 ={'id':1,'sname':'tom','bj':}

'''
stu_info  = []
id = 0


def menu():
    print(
            '''
           -----------学生成绩系统-------------
           |                                  |
           |===========主功能菜单=============|
           |                                  |
           |                                  |
           |          1、录入学生成绩         |    
           |          2、查询学生成绩         |
           |          3、删除学生成绩         |
           |          4、修改学生成绩         |
           |          5、展示所有学生         |
           |          0、退出系统             |
           |                                  |
           |                                  |
           ------------------------------------
      
'''
            )

#录入学生成绩
def add_info():
    while True:
        sname = input('请输入学生姓名')
        if not sname:
            print('学生姓名不能为空')
            continue
        bj = input('请输入学生班级')
        linux = input('请输入学生linux成绩')
        php = input('请输入学生php成绩')
        python = input('请输入学生python成绩')

        global id
        id += 1
        stu = {'id':id,'sname':sname,'bj':bj,'linux':linux,'php':php,'python':python}
        stu_info.append(stu)
        #print(stu_info)
        key = input('是否继续录入y/n?')
        if key == 'y':
            continue
        else:
            break
#显示所有学生的成绩
def show():
    '''
    遍历列表，获取到每个学生的信息
    '''
    format_title = '{:^6}{:^12}{:^12}{:^12}{:^12}{:^12}'
    format_data = '{:^6}{:^14}{:^15}{:^13}{:^15}{:^14}'
    print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
    for i in stu_info:
        id = i.get('id')
        sname = i.get('sname')
        bj = i.get('bj')
        linux = i.get('linux')
        php = i.get('php')
        python = i.get('python')
        print(format_data.format(id,sname,bj,linux,php,python))

def search():
    '''
    根据名字查询学生成绩
    '''

    format_title = '{:^6}{:^12}{:^12}{:^12}{:^12}{:^12}'
    format_data = '{:^6}{:^14}{:^15}{:^13}{:^15}{:^14}'
    sname = input('输入要查询的学生姓名:')
    print(format_title.format('ID','姓名','班级','linux成绩','php成绩','python成绩'))
    #提取到所有学生的名字
    name_list = [stu_info[i].get('sname') for i in range(len(stu_info))]
    if sname in name_list:
        for i in stu_info:
            if sname == i.get('sname'):
                id = i.get('id')
                sname = i.get('sname')
                bj = i.get('bj')
                linux = i.get('linux')
                php = i.get('php')
                python = i.get('python')
                print(format_data.format(id,sname,bj,linux,php,python))
            else:
                print('学生名字不存在')



#删除学生


def delete():

    global id
    sname = input('请输入要删除的学生名字:')
    if stu_info:
        for i in stu_info:
            if i['sname'] == sname:
                stu_info.remove(i)
                print('删除成功')
        #for i,v in enumerate(stu_info):
        for i in range(len(stu_info)):
            id = i + 1
            stu_info[i]['id'] = id
    #当学生列表为空时,id重置为0
    if not stu_info:
        id = 0
    show()
alist = [show()]
#alist = [{'name':'wwine','success':'18','class':'4','id':'1'},{'name':'tom','success':'18','class':'4','id':'2'}] 

#修改学生的信息，只修改学生的成绩
def modify():
    sname = input('请输入学生名字:')
    global stu_info
    for i in stu_info:
        if i['sanme'] == sname:
            Id = i.get('Id')
            stuId = Id -1
            sname = i.get('sanme')
            bj = i.get('bj')
            stuNum = i.get('stuNum')
            newLinux = input('请输入学生liunx成绩:')
            newPHP = input('请输入学生php成绩:')
            newPython = input('请输入学生python成绩')
            newStudent = {"id":Id,"sname":sname,"stuNum":stuNum,"linux":newlinux,"php":newPHP,"python":newPython}
            stu_info[stuId].update(newStudent)
    num = input('Y/y,继续 N/n,退出：')
    thisFunction = modify
    ifTrue(num,thisFunction)

def main():
    while True:
        menu()
        key = input('请选择功能:')
        if key == '1':
            add_info()

        if key == '2':
            search()

        if key == '3':
            delete()
        
        if key == '4':
            modify()
           
        if key == '5':
            show()

        if key == '0':
            break
main()
