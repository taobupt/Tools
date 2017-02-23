import csv
import os
import os.path
import re
class HomeWork:
    def __init__(self):
        self.directory=input("please input your directory \n ")
        self.keyword=input("please input keywords,split by space \n")
        #self.directory="/Users/tao/Documents/16fall/computerArchitecture/hw2/A_4"
        #self.keyword="sim_IPC sim_CPI"
        self.keywords=[]
        self.writer = csv.writer(open("res.csv", 'w'))
    def getKeywords(self):
        self.keywords=self.keyword.split(" ")
        self.writer.writerow(self.keywords)
        res=[]
        dat=re.compile("\s+")
        for parent, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                filename=os.path.join(parent,filename)
                tmp = [' ']*len(self.keywords)
                with open(filename,'rt') as f:
                    for line in f:
                        for keywd in self.keywords:
                                if line.startswith(keywd):
                                    key=dat.split(line)
                                    index=self.keywords.index(keywd)
                                    tmp[index]=float(key[1])
                res.append(tmp)
        self.writer.writerows(res)

if __name__=="__main__":
    homework=HomeWork()
    homework.getKeywords()
    # with open('some.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["word1","word2"])
    #     writer.writerows([[1,2],[3,4]])

