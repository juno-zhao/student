# input_module.py 录入模块
import easygui as g

class Student:
    name = ""
    age = 0
    gender = ""
    height = 0.0
    weight = 0.0
    father_name = ""
    father_phone = ""
    mother_name = ""
    mother_phone = ""


def input_student():
    people_num_str = g.enterbox(msg='请输入学生人数', title='学生信息录入')
    if people_num_str is None:
        return

    #校验人数
    while True:
        try:
            people_num = int(people_num_str)
            if people_num > 0:
                break
            else:
                people_num_str = g.enterbox("人数必须大于0！请重新输入学生人数")
                if people_num_str is None:
                    return
        except ValueError:
            people_num_str = g.enterbox("输入不是有效数字！请重新输入学生人数")
            if people_num_str is None:
                return

    f = open("学生信息.txt","a",encoding="utf-8")
    for i in range(people_num):
        student = Student()

        student.name = g.enterbox(msg=f'请输入{i+1}号学生姓名', title='学生信息录入')
        if student.name is None:
            f.close()
            return

        #年龄
        while True:
            age_str = g.enterbox(msg=f'请输入{i+1}号学生年龄', title='学生信息录入')
            if age_str is None:
                f.close()
                return
            try:
                student.age = int(age_str)
                break
            except ValueError:
                g.msgbox("年龄必须输入数字！请重新填写")

        #性别
        student.gender = g.enterbox(msg=f'请输入{i+1}号学生性别', title='学生信息录入')
        if student.gender is None:
            f.close()
            return

        #身高
        while True:
            height_str = g.enterbox(msg=f'请输入{i+1}号学生身高（单位：米）', title='学生信息录入')
            if height_str is None:
                f.close()
                return
            try:
                student.height = float(height_str)
                break
            except ValueError:
                g.msgbox("身高必须输入数字！请重新填写")

        #体重
        while True:
            weight_str = g.enterbox(msg=f'请输入{i+1}号学生体重（单位：千克）', title='学生信息录入')
            if weight_str is None:
                f.close()
                return
            try:
                student.weight = float(weight_str)
                break
            except ValueError:
                g.msgbox("体重必须输入数字！请重新填写")

        student.father_name = g.enterbox(msg=f'请输入{i+1}号学生父亲姓名', title='学生信息录入')
        if student.father_name is None:
            f.close()
            return
        student.father_phone = g.enterbox(msg=f'请输入{i+1}号学生父亲电话', title='学生信息录入')
        if student.father_phone is None:
            f.close()
            return
        student.mother_name = g.enterbox(msg=f'请输入{i+1}号学生母亲姓名', title='学生信息录入')
        if student.mother_name is None:
            f.close()
            return
        student.mother_phone = g.enterbox(msg=f'请输入{i+1}号学生母亲电话', title='学生信息录入')
        if student.mother_phone is None:
            f.close()
            return

        f.write(f'学号：{i+1}，姓名：{student.name}，年龄：{student.age}，性别：{student.gender}，身高：{student.height}米，体重：{student.weight}千克，父亲姓名：{student.father_name}，父亲电话：{student.father_phone}，母亲姓名：{student.mother_name}，母亲电话：{student.mother_phone}\n')

    f.close()
    g.msgbox(msg='学生信息录入成功', title='录入结果')