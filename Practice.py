
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
'''
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


# python 练习题10
#  暂停一秒输出，并格式化当前时间。
localtime = time.localtime(time.time())  #time.time()返回当前时间的时间戳  time.localtime()接收时间辍(可选),并返回当地时间下的时间元组
print localtime
time.sleep(1)
localtime = time.asctime(time.localtime(time.time())) #time.asctime（）接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"
print "本地时间为：", localtime
time.sleep(1)
print "格式化时间为：", time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) # 	time.strftime(fmt[,tupletime])接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
time.sleep(1)
print "格式化时间为：", time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) 
'''

# python 练习题11
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
#方法1
'''
def rabbit(months):
    a=[1,1]
    for i in range(2,months):
        a.append(a[i-1]+a[i-2])
    return a 

b= rabbit(45)
for j in range(1,(len(b)+1)):
    print "第%d个月兔子总对数为：" % j,b[j-1]
'''
#方法2： # 这种写法是 菜鸟教程提供的
'''
def rabbit1(num):
    f1 = 1
    #第一个月为1
    f2 = 1
    #第二个月为1
    if num == 1 or num == 2:
        return 1
    else:
        for i in range(num-1):
            f1,f2 = f2,f1+f2
    return f1
print rabbit1(36)  # 第三十六月兔子数量
'''
# python 练习题12
# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
'''
for i in range(101,200):
    for j in range(2,i):
        if (i % j == 0):
            break
    else:  #这条else语句对应的是for，不是if，这个是python特有的语句。即在for 循环中，如果没有从任何一个break中退出，则会执行和for对应的else，只要从break中退出了，则else部分不执行。
        print i
'''
# Python 练习实例13
#题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

#程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。

for i in range(100,999):
    a = (i/100)%10 #取百位
    b= (i/10)%10  #取十位
    c= (i/1)%10  #取个位
    if a**3+b**3+c**3 == i:
        print i
    else:
        pass
