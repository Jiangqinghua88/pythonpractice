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
'''
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(raw_input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print sum
'''

#Python 练习实例39
#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。


def InsertData(arrrr):
    print "原始列表："
    for a in range(len(arrrr)):
        print arrrr[a],
    print 
    letter = 2
    end = arrrr[len(arrrr)-2]
    if (letter > end):
        arrrr[-1]=letter
        print arrrr
    else:
        for i in range(len(arrrr)+2):
            if (arrrr[i]>= letter):
                temp = arrrr[i]
                arrrr[i] = letter
                for j in range(i+1,6):
                    temp2=arrrr[j]
                    arrrr[j]=temp
                    temp=temp2
                break
        print arrrr
InsertData([0,3,5,7,8,9,0])

#Python 练习类的用法   
# 
class Employee:
    empCount = 0 #empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
    def __init__(self,name,salary): # 方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
    def displayEmployee(self): #self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        print "Name:",self.name,",Salary:",self.salary

emp1 = Employee('Zara',2000) #创建 Employee 类的第一个对象
emp2 = Employee('Manni',5000)#创建 Employee 类的第二个对象
emp1.displayEmployee() #您可以使用点号 . 来访问对象的属性。
emp2.displayEmployee() 
print "Total Employee %d" % Employee.empCount
emp1.age =7   # 添加一个 'age' 属性
emp1.age = 8 # 修改 'age' 属性
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值

print "Employee.age:", emp1.age

#Python 练习类的继承

#python中继承中的一些特点：

#1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
#2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数
#3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
#如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
class Parent:
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"
    def parentMethod(self):
        print "调用父类方法"
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print "父类属性 :", Parent.parentAttr
    
class Child(Parent):
    def __init__(self):
        print "调用子类构造方法"
    def childMethod(self):
        print "调用子类方法"


c= Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod() # 调用父类方法
c.setAttr(300) # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值


#Python 练习方法重写

class Parent:   # 定义父类
    def myMethod(self):
        print "调用父类方法"
class Child1(Parent):
    def myMethod(self):  #父类方法重写
        print "调用子类方法"   

c= Child1()
c.myMethod()

#运算符重载
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "Vector(%d,%d)" %(self.a,self.b)
    def __add__(self,other):
        return Vector(self.a+ other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1+v2

#类属性与方法
#类的私有属性
#__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
#类的方法
#在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
#类的私有方法
#__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods

class JustCounter:
    __secretCount = 0
    publicCount = 0
    def count(self):
        self.__secretCount +=1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount

import re
print (re.match(""))

