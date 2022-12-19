'''
DATE:19TH DEC 2022
DAY: MONDAY
TOPIC: FUNTION
AUTHOR:RAMA BHARGAvi
''' 

def even(x):
    if x%2==0:
        return True
    else:
        return False
z=[int(x) for x in input().split()]
q = list(filter(even,z)) 
print("from the z the even values are:",q) 
def eo(num):
    if num%2==0:
        print(num, "is even")
    else:
        print(num, "is odd")
n=int(input())
eo(n)
eo(12)
eo(13)    
f = lambda x,y,z: x+y+z
s = lambda x,y,z: z*y*z
r = f(3,10,5)
z= s(2,3,5)
print('sum =',r)
print('mul =',z)