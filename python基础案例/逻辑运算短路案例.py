# 短路问题案例
a = True
b = True
c = False
aa = a or b and (a and b) #转换成算数1 +.... ....
print(aa)