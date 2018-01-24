
# python 练习题1
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
sum =0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)&(i!=k)&(j!=k)):
                print i,j,k
                sum=sum+1
                
print "一共可以组成",sum,"个数字"
'''
# python 练习题5
# 输入三个整数x,y,z，请把这三个数由小到大输出。
'''
def abc(mylist):
    for i in range(0,len(mylist)):
        for j in range(0,i+1):
            if mylist[i]< mylist[j]:
                mylist[i],mylist[j] =  mylist[j],mylist[i]
    return mylist

arr =[5,6,9,8,1,2,3,4]
print abc(arr)
'''
'''
l=[]
for i in range(3):
    x=int(input("integer:\n"))
    l=l.append(x)
    print l.sorted()
'''
'''
# python 练习题6
# 斐波那契数列, 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
def fibb(a):
    if a==0:
        return [0]
    if a==1:
        return [0,1]
    if a==2:
        return [0,1,1]
    arr=[0,1,1]

    for j in range(3,a):
        arr.append(arr[j-2]+arr[j-1])
#        arr[j]=arr[j-2]+arr[j-1]
#        arr.append(arr[j])        
    return arr

print fibb(1)


# python 练习题7
# 题目：将一个列表的数据复制到另一个列表中。
# 方法1：
def revert(arr):
    abb=[]
    abb=arr[:]
    return abb

print revert([1,2,3,4])
#方法2：

def revert2(arr):
    abb=[]
    for i in range(len(arr)):
        abb.append(arr[i])
    return abb
print revert2([4,5,6,7,8,9])


# python 练习题8
# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# 方法1：

for i in range(1,10):
    print
    for j in range(1,i+1):
        print "%d * %d = %d" % (i, j, i*j),  #逗号表示不换行， 通配符的使用要注意。
#        print i,"*",j,"==",i*j,

'''
# python 练习题9
#题目：暂停一秒输出。
#程序分析：使用 time 模块的 sleep() 函数。  
import time 
myDictionary = {"a": 123, "b": 456, "c":789 }

for i in myDictionary.keys():
    print i,
    time.sleep(1)
    print myDictionary.get(i)
    time.sleep(1)

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print key, value
    time.sleep(1) # 暂停 1 秒