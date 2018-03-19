
import re
'''
re.match函数
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
'''
print (re.match("www","www.runoob.com").span())  # span() 返回一个元组包含匹配 (开始,结束) 的位置
print (re.match("com","www.runoob.com"))


line = "Cats are smarter than dogs"
matchObj=re.match( r'(.*) are (.*?) .*', line, re.M|re.I) #(.*) 第一个匹配分组,.* 代表匹配除换行符之外的所有字符 
# (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
#后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中
if matchObj:
    print "matchObj.group():", matchObj.group() #匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    print "matchObj.group(1):", matchObj.group(1) #matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
    print "matchObj.group(2):", matchObj.group(2)#matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的
else:
    print "No match!!"

'''
re.search方法
re.search 扫描整个字符串并返回第一个成功的匹配。匹配成功re.search方法返回一个匹配的对象，否则返回None。

re.search(pattern, string, flags=0)

pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''

print (re.search("www","www.runoob.com").span())

print (re.search('com', 'www.runoob.com').span())    

#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print "search --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"


#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs";
 
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"

'''
\d  匹配任何十进制数；它相当于类 [0-9]。
\D  匹配任何非数字字符；它相当于类 [^0-9]。
\s  匹配任何空白字符；它相当于类  [ \t\n\r\f\v]。
\S  匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
\w  匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
\W  匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。

检索和替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
re.sub(pattern, repl, string, count=0, flags=0)
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''

phone ="2004-959-559 #这是一个国外的电话号码"

#删除字符串中的Python 注释
num = re.sub(r"#.*$","",phone)
print "电话号码是：",num

#删除非数字（-）的字符串
num = re.sub(r'\D',"",phone)
print "电话号码是：",num


'''
re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：
re.compile(pattern[, flags])
'''

pattern = re.compile(r'\d+')     # 用于匹配至少一个数字
m = pattern.match("one12twothree34four",2,10) # 从'e'的位置开始匹配，没有匹配,返回none
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配,返回一个 Match 对象
print m

print m.group(0) #返回被 RE 匹配的字符串

print m.start(0)  #返回匹配开始的位置

print m.end(0)   #返回匹配结束的位置
 
print m.span()  #返回一个元组包含匹配 (开始,结束) 的位置


pattern = re.compile(r"([a-z]+) ([a-z]+)",re.I) # re.I 表示忽略大小写
# + 表示匹配一或更多次。* 匹配零或更多次，所以可以根本就不出现，而 + 则要求至少出现一次。
m = pattern.match("Hello World Wide Web")  # 匹配成功，返回一个 Match 对象

print m
print m.group(0) # 返回匹配成功的整个子串
print m.span()  # 返回匹配成功的整个子串的索引
print m.group(1)# 返回第一个分组匹配成功的子串
print m.span(1)# 返回第一个分组匹配成功的子串的索引
print m.group(2)# 返回第二个分组匹配成功的子串
print m.span(2) # 返回第二个分组匹配成功的子串
print m.groups() # 等价于 (m.group(1), m.group(2), ...)

#print m.group(3) # 不存在第三个分组


'''
findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 findall 匹配所有。

语法格式为：

findall(string[, pos[, endpos]])

string : 待匹配的字符串。
pos : 可选参数，指定字符串的起始位置，默认为 0。
endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
'''

pattern = re.compile(r'\d+')
result1= pattern.findall("runoob 123 google 456")
result2 = pattern.findall("run88oob123google456",0,10)
print (result1)
print (result2)

'''
re.finditer
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
'''
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print(match.group())
