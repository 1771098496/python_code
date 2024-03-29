# 表达式
- 由一个或者几个数字或者变量或者运算符合成的一行代码
- 通常返回一个结果

# 运算符
- 由一个以上的值经过一系列的运算得到新值的过程就叫运算
- 用来操作运算的符号叫运算符
- 运算符分类
    - 算术运算符
        - 用来进行计算数学运算的符号
        - 通常用来表示加减乘除
        - Python没有自增和自减的运算符
    - 比较或关系运算符
        - 对两个内容进行比较的运算符
        - 结果一定是布尔值，即True/False
    - 赋值运算符
        - 把一个值放到变量里边去
    - 逻辑运算符
        - 对布尔类型变量或者值进行运算的符号
        - and：逻辑与
        - or：逻辑或
        - not：逻辑非
        - Python里面的逻辑运算没有异或
        - 运算规则：
            - and看作乘法，or看作加法
            - True看做1，False看做0
            - 则逻辑运算就能转换成数学运算
            - 最后结果如果是0则为False，否则为True
        - 逻辑运算符的短路问题
            - 逻辑运算式，按照运算顺序计算，一旦能够确定整个式子未来的值，则不再进行计算，直接返回
    - 位运算符
    - 成员运算符
        - 用来检测一个值或者变量是否在某个集合里面
        - in：成员运算符
        - not in：不在集合里面的意思
    - 身份运算符
        - 用来确定两个变量是否为同一变量
        - is：身份运算符
        - is not：两个变量不是同一变量
        - 对整数N[-5,256]放进了固定的内存中，不因你每次运行而变化