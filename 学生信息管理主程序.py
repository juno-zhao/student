# main.py 主程序入口
import easygui as g
#导入另外两个文件里的函数
from input_module import input_student
from search_module import search_student


#======密码验证======#
user_word = g.enterbox(msg='请输入密码验证', title='密码验证')
if user_word is None:
    exit()

with open("密码.txt","r",encoding="utf-8") as w:
    password = w.read().strip()

if user_word != password:
    g.msgbox("密码错误，程序退出！")
    exit()


#主while循环菜单
while True:
    select = g.choicebox(msg="请选择功能", title="学生信息管理系统", choices=["录入学生信息","查询学生信息","退出程序"])
    if select is None or select == "退出程序":
        g.msgbox("程序结束")
        break

    if select == "录入学生信息":
        input_student()

    elif select == "查询学生信息":
        search_student()