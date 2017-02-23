import numpy as np
import math
def getDistance(t):
    nlh=[0.33,0.67,0.67]
    nlh=[t*x for x in nlh]
    ph=[24,18,18]
    pr=[18,6,6]
    p=np.add(ph,nlh)
    sum=0
    for i in range(0,3):
        sum+=(p[i]-pr[i])*(p[i]-pr[i])
    return math.sqrt(sum)
print(getDistance(112))