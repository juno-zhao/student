# search_module.py 查询模块
import easygui as g

def search_student():
    search_name = g.enterbox(msg="请输入要查找的学生姓名",title="学生信息查询")
    if search_name is None:
        return
    found = False
    try:
        with open("学生信息.txt","r",encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if f"姓名：{search_name}" in line:
                    g.msgbox(msg=line,title="查询到学生信息")
                    found = True
                    break
        if not found:
            g.msgbox(msg="未找到该学生信息！",title="查询结果")
    except FileNotFoundError:
        g.msgbox(msg="学生信息.txt文件不存在，请先录入学生数据！",title="错误")