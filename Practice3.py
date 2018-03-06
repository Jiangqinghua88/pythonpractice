# Python 练习实例30
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def palin_number(n):
    n= str(n)
    m=n
    return n==m

print palin_number(12321)

# Python 练习实例31
#题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

def Stringday(s):
    m = s[0:1]
    n = s[1:]
    if m == "M":
        print "Monday"
    elif m == "W":
        print "Wednesday"
    elif m== "F":
        print "Friday"
    elif m == "T":
        if n == "u":
            print "Tuesday"
        else:
            print "Thurthday"
    elif m== "S":
        if n== "a":
            print "Saturday"
        else:
            print "Sunday"

#Stringday("W")
#Stringday("Sa")

'''
方法二：

letter = raw_input("please input:")
if letter == "S":
    print ("please input the seconde letter:")
    letter = raw_input("please input:")
    if letter == "a":
        print ("Saturday")
    else:
        print ("Sunday")
elif letter == "M":
    print "Monday"
elif letter == "F":
    print "Friday"
elif letter == "T":
    print ("please input the seconde letter:")
    letter = raw_input("please input:")
    if letter == "u":
        print "Tuesday"
    else:
        print "Thurthday"
'''

#Python 练习实例32
#题目：按相反的顺序输出列表的值。

a=[1,2,3,4,5]
for i in a[::-1]:
    print i,


#Python 练习实例33
#题目：按逗号分隔列表。
L=[1,2,3,4,5]
L1= str(L)
print ','.join(L1)

seq1 = ['hello','good','boy','doiido']
print ' '.join(seq1)

#Python 练习实例37
#题目：对10个数进行排序。冒泡算法
#程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

def sequence(arr):
    long1 = len(arr)
    for i in range(0,long1):
        for j in range(0,i):
            if (arr[i]< arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr

print sequence([8,7,6,10,21,30,2])

#Python 练习实例38
#题目：求一个3*3矩阵主对角线元素之和。
#程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
