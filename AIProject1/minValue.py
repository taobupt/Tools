from scipy.optimize import fmin_slsqp
from numpy import array

def calcaulateDistance(t,a):
    x,y=t
    return (x-a)**2+(y-a)**2
print(fmin_slsqp(calcaulateDistance,array([1,1]),args=(3,),bounds=((0,2),(0,3))))


import random

random.seed(32)
list1 = [random.randint(1,10) for x in range(5)]

random.seed(321)
list2 = [random.randint(1,10) for x in range(5)]

assert(list1==list2)