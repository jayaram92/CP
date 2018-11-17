import os
import sys
import random
import math
import time

class Bowling:
    def __init__(self):
        self.roll = []
    def input_roll(self,a):
        fin = []
        ar = []
        try:
            for s in a:
                s=s.split(',')
                if s.__len__() == 0:
                    print("Invalid - Please follow the rules")
                    return False
                for x in s:
                    ar.append(int(x))
                fin.append(ar)
                ar = []
            if fin.__len__() != 10:
                print("Invalid - Please follow the rules")
                return False
            else:
                idx=0
                for arr in fin:
                    idx=idx+1
                    if idx==fin.__len__():
                        if arr.__len__() != 3:
                            print("Final not 3-Invalid")
                            return False
                    else:
                        if 10 in arr:
                            continue
                        elif arr.__len__() == 2:
                            continue
                        else:
                            print('invalid')
                            return False
            self.roll = fin
            return True
        except ValueError:
            print('value improper')
            return False


    def bowling(self,a):
       self.findsum(a)
       if a.__len__() != 10:
           print('length')
           print(a.__len__())
       for b in a:
           for c in b:
               if self.validate(c):
                   print(c)
             #  print(c)
    def validate(self,val):
        return val<=10

    def findsum(self):
        output=[]
        b=0
        idx=0
        if self.roll.__len__() != 0:
            for a in self.roll:
                idx=idx+1
                if 10 in a and idx<self.roll.__len__():
                    b+=10+sum(self.roll[idx])
                    if 10 in self.roll[idx] and idx+1<self.roll.__len__():
                        b+=sum(self.roll[idx+1])
                else:
                    b+=sum(a);
                output.append(b)
        else:
            print('invalid-cannot sum')
            print(self.roll)
            return
            #b=0
        print('output')
        print(output)
        for a in output:
            print(a)
        print('end')



if __name__ == '__main__':
    b = Bowling()
    if b.input_roll(sys.argv[1:]):
   # b.input_roll([[5,2],[8,1],[6,4],[10],[0,5],[2,6],[8,1],[5,3],[6,1],[10,2,6]])
        b.findsum()




