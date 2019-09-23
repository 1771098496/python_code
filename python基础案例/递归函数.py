# 递归调用深度限制代码
'''
x = 0
def fun():
    global x
    x += 1
    print(x)
    # 函数自己调用自己
    fun()

# 调用函数
fun()
'''

# 阶乘
def fun_a(n):
    print(n)
    if n == 1:
        return 1
    return n * fun_a(n - 1)

rst = fun_a(5)
print(rst)

# 斐波拉契数列
# 一列数字，第一个值是1，第二个也是1，从第三个开始，每个数字的值等于前两个数字出现的值的和
# 数学公式：f(1)=1,f(2)=1,f(n)=f(n-1)+f(n-2)
def fbl(n):
    if n == 1 or n == 2:
        return 1
    return fbl(n-1) + fbl(n-2)

rst1 = fbl(10)
print(rst1)

# 汉诺塔
a = "A"
b = "B"
c = "C"


def hano(a, b, c, n):
    if n == 1:
        print("{}-->{}".format(a, c))
        return None

    if n == 2:
        print("{}-->{}".format(a, c))
        print("{}-->{}".format(a, b))
        print("{}-->{}".format(b, c))
        return None

    hano(a, c, b, n - 1)
    print("{}-->{}".format(a, c))
    hano(b, a, c, n - 1)


hano(a, b, c, 3)