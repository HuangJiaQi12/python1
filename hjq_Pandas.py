import pandas as pd
import numpy as np


#创建一个列表
# s=pd.Series([1,3,6,np.nan,9])
# print(s)
#
# #创建有标题的矩阵
# data=pd.date_range('20260101',periods=6)
# df=pd.DataFrame(np.random.random((6,4)),index=data,columns=['A','B','C','D'])  #矩阵数据 行标题 列标题
# print(df)
# df1=pd.DataFrame(np.arange(12).reshape(3,4))
# print(df1)
# df2=pd.DataFrame({'A':1,'B':pd.Timestamp('20260920'),
#                   'C':pd.Series(1,index=list(range(5))),
#                   'D':np.array([3]*5,dtype='float32'),
#                   'E':pd.Categorical(['test1','test5','test1','test2','test5']),})
# print(df2)
# print(df2.index)
# print(df2.columns)
# print(df2.values)
#
# #排序
# print(df2.sort_index(axis=1,ascending=False)) #按行标题排序（倒叙）
# print(df2.sort_index(axis=0,ascending=False))
# print((df2.sort_values(by='E')))

#选择数据
# dates=pd.date_range('20260101', periods=6)
# df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
# print(df)
# print(df.A) #选择第A列(按列选择)
# print((df[0:3]),df["20260101":"20260102"]) #选择0-3行 ， 选择20260101-20260102行
# #根据标签选择 loc
# print(df.loc['20260103']) #选择20260103行
# print(df.loc['20260105',['A','B']]) #选择20260105行  A，B列的数
#根据索引选择 iloc
# print(df.iloc[[1,2,4],1:3])
# print(df[df.B<9])

#设置值
# data=pd.date_range('20260101', periods=6)
# df=pd.DataFrame(np.arange(24).reshape(6,4),data,columns=['A','B','C','D'])
# print(df)
# df.loc['20260103','B']=520
# df.iloc[0,0]=1314
# print(df)
# df.loc[df.A<5,'D']=222
# print(df)

#处理丢失数据
# data=pd.date_range('20260101', periods=6)
# df=pd.DataFrame(np.arange(24).reshape(6,4),index=data,columns=list('ABCD'))
# df.iloc[0,1]=np.nan
# df.loc['20260104','C']=np.nan
# print(df)
# print(df.dropna(axis=0,how='any'))
# print(df.fillna(value=222))
# print(df.isnull())
# print(np.any(df.isnull()))

#导入导出文件
# date=pd.read_csv(r'C:\Users\86150\Desktop\studengt.csv')
# print(date)
# date.to_pickle('student.pkl')
# pkl=pd.read_pickle('student.pkl')
# print(pkl)

#表格合并
#111
# df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
# res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
# print(res)
# #222
df1=pd.DataFrame(np.ones((3,4))*0,index=[1,2,3],columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,index=[2,3,4],columns=['e','b','c','d'])
res=pd.concat([df1,df2],axis=0,join='inner',ignore_index=True)
print(res)

