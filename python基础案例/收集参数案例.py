# 收集参数代码
# 函数模拟一个学生进行自我介绍

def stu(*args):
    print("Hello，大家好，我自我介绍一下：")
    # type函数的作用是检测变量的类型
    print(type(args))
    for item in args:
        print(item)

stu("lingling",18,"广东","single")


# 调用的时候需要使用关键字参数调用

def stu_key(**kwargs):
    print("Hello，大家好，我自我介绍一下：")
    # type函数的作用是检测变量的类型
    print(type(kwargs))
    for i,k in kwargs.items():
        print(i,"----",k)

stu_key(name="lingilng",age=19,add="广东",work="Teacher")
print("-"*20)


# 收集参数混合调用案例

def stu1(name,age,*args,hobby="没有",**kwargs):
    print("Hello，大家好")
    print("我叫{0},我今年{1}岁了。".format(name,age))
    if hobby == "没有":
        print("我没有爱好，so sorry")
    else:
        print("我的爱好是{0}".format(hobby))

    print("-"*20)

    for i in args:
        print(i)

    print("*"*20)

    for k,v in kwargs.items():
        print(k,"----",v)

name = "lingling"
age = 19

stu1(name,age)
stu1(name,age,hobby="游泳")

stu1(name,age,"王慧琪","w",hobby="游泳",hobby1="烹饪",hobby2="不爱聊天")

# 收集参数的解包问题

def stu2(*args):
    print("哈哈哈哈哈")
   # n = 0  # n 用来表示循环次数
    for i in args:
        print(type(i))
       # print(n)
       # n += 1
        print(i)

l = ["ling",2,"nihja",4,5]
stu2(l)
stu2(*l)

# 查看文档
stu2.__doc__