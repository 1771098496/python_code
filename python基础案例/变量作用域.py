# 认为a1是全局的

a1 = 100
def fun():
    print(a1)
    print("I am in fun ")
    # a2的作用范围是fun
    # a2 = 99
    global a2  #使用global将a2定义成全局变量
    a2 = 99
    print(a2)

print(a1)
fun()
print(a2)

# globals和locals
# globals和locals是内建函数
a = 1
b = 2
def fun1(c,d):
    e = 111
    print("Locals={0}".format(locals()))
    print("Globals={0}".format(globals()))

fun1(100,200)

# eval()函数

x = 100
y = 200
#执行x+y的字符串
z1 = x + y
z2 = eval("x + y")
print(z1)
print(z2)