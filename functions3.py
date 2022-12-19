'''
DATE:19TH DEC 2022
DAY: MONDAY
TOPIC: FUNTION
AUTHOR:RAMA BHARGAvi
''' 
def attach(s1,s2):
    s3=s1+s2
    print('total string: '+s3)
attach('New','York')
s1,s2=[x for x in input().split(',')]
attach(s1,s2)
def sc(name="hd"):
    print(f"my name in school is {name}")
def cn(name="sd"):
    print("my name in college is {name}")
    sc()
def wk(name="hh"):
    print(f"my name at work place is {name}")
    cn()
wk()
a=2
def bm():
    a=4
    b=3;c=5
    print(a)
    print(b)
print(a)
bm()
print(a)
x=int(input("enter your number greater than 18:"))
assert x>=8, "age is less then 18"
print('you are eligible to vote',x)
def n(lm):
    lm.append(7)
    print(lm)

lm=[1,2,3]
n(lm)
