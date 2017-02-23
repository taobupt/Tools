import numpy as np
import math
a=[1,2,3,4,5]
a=np.array([2,3,4])
print(np.dot([2,3,4],[1,2,3]))
print(np.cross([1,2,3],[4,5,6]))
print(np.linalg.norm(a))

def getMangitiude(a):
    a=[x **2 for x in a]
    return math.sqrt(sum(a))

def getUnitVector(a):
    mang=getMangitiude(a)
    return [x/mang for x in a]

def getCrossProduct(a,b):
    return np.cross(a,b)
def getDotProduct(a,b):
    return np.dot(a,b)
def getAddVector(a,b):
    return np.add(a,b)

def getSubVector(a,b):
    return np.subtract(a,b)
#integer multiply vector
def multiplyVector(a,b):
    return [a*x for x in b]
def solveQuard(A,B,C):
    t1=(-B+math.sqrt(B**2-4*A*C))/(2*A)
    t2=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    return [t1,t2]


def calculateFP(p):
    a=[1,1,1]
    a21=0
    a00=-1
    s=[8,4,3]
    pc=[11,2,5]
    n=[[0.00,0.89,-0.45],[0.96,-0.13,-0.26],[0.29,0.43,0.86]]
    res=0
    for i in range(0,3):
        tmp=getDotProduct(n[i],getSubVector(p,pc))
        res+=a[i]*(tmp**2)/(s[i]**2)
    res+=a21*getDotProduct(n[2],getSubVector(p,pc))/s[2]+a00;
    return res

def getNormalVector(p):
    a = [1, 1, 1]
    a21 = 0
    a00 = -1
    s = [8, 4, 3]
    pc = [11, 2, 5]
    n = [[0.00, 0.89, -0.45], [0.96, -0.13, -0.26], [0.29, 0.43, 0.86]]
    res = []
    for i in range(0,3):
        res.append(2*a[i]*getDotProduct(n[i],getSubVector(p,pc)))
    tmp=getAddVector(multiplyVector(res[0],n[0]),getAddVector(multiplyVector(res[1],n[1]),multiplyVector(res[2],n[2])))
    return getAddVector(tmp,multiplyVector(a21/s[2],n[2]))

def getIntersection(nlh,pr,r):
    ph=[24,18,18]
    b=getDotProduct(nlh,getSubVector(ph,pr))
    c=getDotProduct(getSubVector(ph,pr),getSubVector(ph,pr))-r**2
    delta=b**2-c
    print("delat",delta)
    return [-b+math.sqrt(delta),-b-math.sqrt(delta)]

print(getUnitVector([6,4,12]))
print(getUnitVector(getCrossProduct([6,4,12],[1,0,0])))
print(getAddVector(a,-a))

#quiz 3
print('-----------quiz3---------------')
ph=[24,18,18]
pl=[28,26,26]
print(getUnitVector(getSubVector(pl,ph)))
print(getMangitiude(getSubVector(pl,ph)))
print(solveQuard(12,-576,5460))

ph=[11,9.12,1.4]
print(getUnitVector(getNormalVector(ph)))

#intersection
print(getIntersection([0.33,0.67,0.67],[18,6,6],6))



print('-----------quiz2---------------')

pe=[17,19,11]
pc=[21,25,23]
print(getMangitiude(getSubVector(pe,pc)))