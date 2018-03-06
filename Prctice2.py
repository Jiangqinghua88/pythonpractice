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

#Python 练习实例20
#题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

#程序分析：采取逆向思维的方法，从后往前推断。
#第10天：1个， 第9天： x/2 -1 =1 , x= 4 第8天： x/2 -1 = 4. x=10, 依次类推

#设第10天所剩果实为：x2=1, 设第9天所剩果实为X1， (X1/2)-1 = X2， 那么X1= (X2+1)*2

X2 =1
for i in range(9,0,-1):
    X1 =(X2+1)*2
    print "第%d 天所剩果实为：" % i, X1
    X2=X1



#Python 练习实例23
#题目：打印出如下图案（菱形）:
'''
  *
  ***
 *****
*******
 *****
  ***
   *
'''
#程序分析：思路： 先打印一个正三角形，再打印一个倒三角形

for i in range(4):        # 打印正三角形，
    for j in range(2-i+1):
        print " ",
    for k in range (2*i+1):
        print "*",
    print "\n"
    
for i in range(3):
    for j in range(i+1):
        print " ",
    for k in range(4-2*i+1):
        print "*",
    print "\n"


# Python 练习实例24
# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。

a= 2.0
b=1.0
sum1=0.0
for i in range(1,21):
    sum1= sum1+a/b
    t= a
    a= a+b
    b=t
print sum1

# Python 练习实例25
# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。

sum2 = 0
for i in range(1,21):
    t=1
    for j in range(i,1,-1):
        t= t*j
    sum2= sum2+t

print sum2

# Python 练习实例26
# 题目：利用递归方法求5!。
# 程序分析：递归公式：fn=fn_1*4!
s=1
for n in range(5,1,-1):
    s=s*n
print s


# Python 练习实例27
# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
#方法1 自己做的
def output1(s):
    a=[]
    len1= len(s)
    for i in range(len1,0,-1):
        b= s[i-1]
        a.append(b)
    print a

output1("abcdef")
        
#方法2 递归方法实现
def output2(s,l):
    if l==0:
        return
    print(s[l-1]),
    output2(s,l-1)

s="123456789"
l=len(s)
output2(s,l)


# Python 练习实例30
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def palin_number(n):
    n=str(n)
    m=n[::-1]  #将元组或列表反向输出
    return n==m

print palin_number(12321)

#方法二：
'''
def palin_number(n):
    n= str(n)
    m=n
    return n==m

print palin_number(12321)
'''