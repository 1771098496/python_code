# 关键字参数案例

def stu(name,age,addr):
    print("I am a student")
    print("我叫{0}，我今年{1}岁了，我住在{2}".format(name,age,addr))

n = "jingjing"
a = 18
addr = "广东"
# 普通参数，只按照位置传递，容易出错
stu(n,a,addr)
# 关键字参数，不用按照位置传递
stu(age=a,addr=addr,name=n)