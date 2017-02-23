from scipy.optimize import fmin_slsqp
from numpy import array
import math
import random
import matplotlib.pyplot as plt








#search area

width=8
height=8

#  example of find optimal position
# def calcaulateDistance(t,a):
#     x,y=t
#     return (x-a)**2+(y-a)**2
# a=fmin_slsqp(calcaulateDistance,array([1,1]),args=(3,),bounds=((0,2),(0,3)))
# print(type(a))
# print(a[0])

class circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
    def isOverlap(self,cir):
        return math.hypot(self.x-cir.x,self.y-cir.y)<(self.radius+cir.radius)

class minConflict:

    #put all circles into circles arrya
    def __init__(self,M,mr,N,nr):
        self.circiles=[]
        for i in range(1,M+1):
            self.circiles.append(circle(random.random()*(width-2*mr)+mr,random.random()*(height-2*mr)+mr,mr))
        for i in range(1,N+1):
            self.circiles.append(circle(random.random()*(width-2*nr)+nr, random.random()*(height-2*nr)+nr, nr))

    #find the optimal position for each iteration
    def calcaulateDistance(self,t,index):
        x,y=t
        n = len(self.circiles)
        # sum of (r_i+r)
        circleSum=0

        #sum of center distance
        centerDistance=0
        for i in range(0,n):
            if i!=index: #and self.circiles[index].isOverlap(self.circiles[i]):
                circleSum+=self.circiles[index].radius+self.circiles[i].radius
                centerDistance+=math.hypot(x-self.circiles[i].x,y-self.circiles[i].y)
        return circleSum-centerDistance

    #judge whether there are two circles who are overlap
    def isOverLap(self):
        n=len(self.circiles)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if self.circiles[i].isOverlap(self.circiles[j]):
                    return True
        return False

    #return numpy.ndarray
    #index is the randromly seleced circle
    def findOptimalPosition(self,index):
        r=self.circiles[index].radius
        xpos=self.circiles[index].x
        ypos=self.circiles[index].y
        return fmin_slsqp(self.calcaulateDistance, array([xpos,ypos]), args=(index,), bounds=((r, width-r), (r, height-r)))

    #main function
    def exectue(self):
        n = len(self.circiles)

        # if the iteration is larger than 100000, then we return
        cnt=1
        while cnt<1000:
            if not self.isOverLap():
                break
            #pick a randomly circle,randint(a,b)---> [a,b]
            index=random.randint(0,n-1)

            #find the optimal solution and assign it to circles[index]
            optimalPosition=self.findOptimalPosition(index)
            print("circle {0} x: {1} y:{2}".format(index,optimalPosition[0],optimalPosition[1]))
            self.circiles[index].x=optimalPosition[0]
            self.circiles[index].y=optimalPosition[1]
            cnt+=1
        return (self.circiles,cnt)
    def drawCircle(self):
        fig, ax = plt.subplots()  # note we must use plt.subplots, not plt.subplot
        for circle in self.circiles:
            ax.add_artist(plt.Circle((circle.x,circle.y),circle.radius,facecolor='none',edgecolor='r'))
        ax.set_xlim((0, width))
        ax.set_ylim((0, height))
        fig.savefig('plotcircles.png')

if __name__=="__main__":
    project=minConflict(3,2,3,1)
    res=project.exectue()
    #random.seed(321)
    print(res[1])
    project.drawCircle()







