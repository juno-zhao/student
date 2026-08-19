#密码设置
a=open("密码.txt","w",encoding="utf-8")
password=input("请设置密码")
a.write(password)
a.close()
while True:
    input("密码设置成功")