import numpy as np
from jupyter_server.services.contents.fileio import async_copy2_safe

# a=np.array([10,20,30,40])
# b=np.arange(4)
# print(a,b)
# c=b**2
# d=10*np.sin(a)
# print(d)
# print(c)
# print(b<2)

#向量
# a=np.array([[1,0,5],[4,8,0],[0,3,10]])
# b=np.arange(9).reshape(3,3)
# c=a*b
# c_dot=np.dot(a,b)
# c_dot_2=a.dot(b)
# print(c)
# print(c_dot)
# print(c_dot_2)

#random 找行列最值/求和
# a=np.random.random((3,4))
# print(a)
# print(np.sum(a,axis=1))  #1是行 0是列
# print(np.min(a,axis=0))
# print(np.max(a,axis=0))
# print(np.argmin(a))      #找矩阵a内最小值的索引
# print(np.argmax(a))
# print(np.average(a))     #找平均值
# print(np.median(a))      #找中位数
# print((np.cumsum(a)))    #累加

#
# a=np.arange(15,3,-1).reshape((3,4))
# print(a)
# print(np.sort(a))        #排序
# print((np.transpose(a)) ) #转向
# print(a.T)
# print(np.dot(a,a.T))
# print(np.clip(a,5,10))   #对矩阵a操作，a内小于5的数变成5，大于10的数变成10

#矩阵分割
# a=np.arange(12).reshape(3,4)
# print(a)
# print(np.split(a,2,1)) #平均分割
# print(np.split(a,3,0))
# print(np.array_split(a,3,1))#不平均分割

#copy 和 deep copy
# a=np.array([11,25,33,47])
# b=a   #copy 矩阵b和矩阵a完全相同，改变a的值后b也会改变 反之也相同
# b[0]=1
# print(a)
# c=a.copy() #deep copy 改变b的值后a不变
# c[2]=5
# print(a)
# print(c)

AT=np.array([[200,17]])
w=np.array([[1,-3,5],
            [-2,4,-6]])
b=np.array([[-1,1,2]])
z=np.matmul(AT,w)+b
print(z)

f=np.array([[1,5,7]])
g=np.matmul(AT,f)+b
a=np.array(12).reshape(3,4)
print(g)
print(g+f)
print(f)
