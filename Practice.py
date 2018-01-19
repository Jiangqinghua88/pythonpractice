
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

# python 练习题6
# 斐波那契数列, 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
def fibb(a):
    arr=[0,1,1]
    for j in range(3,a):
        arr.append(arr[j-2]+arr[j-1])
#        arr[j]=arr[j-2]+arr[j-1]
#        arr.append(arr[j])        
    return arr

print fibb(10)


