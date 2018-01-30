#Python 练习实例14

#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：

#(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
#(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
#(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

l=[1]
def primeFactor(n):
    for i in range(1,n):
        for j in range(2,i):
            if (i % j == 0):
                break            
        else:
            l.append(i)

    lenth = len(l)
    h=[]
    for k in range(lenth):
        if (l[k]!=1) & (l[k] != n) & (n%l[k]==0):
            h.append(l[k])
         
    return h

print primeFactor(90)

#Python 练习实例15
#题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
#程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
'''
score = int(raw_input("输入分数：\n"))
if score >=90:
    grade ="A"
elif score >=60:
    grade = "B"
else:
    grade = "C"

print ("%d 属于 %s") % (score, grade)
        
'''    

#Python 练习实例16
#题目：输出指定格式的日期。
#程序分析：使用 datetime 模块。
import datetime

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print (datetime.date.today().strftime("%d/%m/%Y"))
 # 创建日期对象
mBirthdayDate = datetime.date(1986,4,5)
print(mBirthdayDate.strftime("%d/%m/%Y"))

#Python 练习实例17
#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#程序分析：利用while语句,条件为输入的字符不为'\n'。
import string

def Statistic(m):
    letters = 0
    space = 0
    digit = 0
    others = 0
    for i in m:
        if i.isalpha():
            letters = letters+1
        elif i.isdigit():
            digit=digit+1
        elif i.isspace():
            space=space+1
        else:
            others= others+1
    print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)

Statistic("a4566222333 abc78989")

#Python 练习实例18
#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#程序分析：关键是计算出每一项的值。

def sum2(m,n):
    Tn = 0
    for count in range(0,n):
        Tn= Tn+m
        m=m*10
        print Tn
        
print sum2(3,5)


#Python 练习实例20
#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

firsttime = [100]
sum1 =100.0
for count in range(0,10):
    sum1=sum1/2
    firsttime.append(sum1*2)

print firsttime
print('总高度 = {0}'.format(sum(firsttime)))   #对列表各数求和 sum(列表名)
print('第10次反弹高度：= {0}'.format(firsttime[-1]/2))

 




