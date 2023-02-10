import bisect
import itertools
import math


def gcd(x,y):
    if (x==0):
        return y
    else:
        return gcd(y%x,x)
#Time complexity= O(log(min(x,y))

def prime(x):
    flag=[0]*(x+1)
    flag[0]=1
    flag[1]=1
    for i in range(2,math.ceil(math.sqrt(x))+1):
        for j in range(2*i,x+1,i):
            flag[j]=1
    print(flag)
    for i in range(0,len(flag)):
        if flag[i]==0:
            print(i)

#Time complexity-> O(sqrt(x))\

def fast_power(x,power):
    sol=1
    mod=10**9+7
    while(power>0):
        if power%2==1:
            sol=sol*x%mod


        x=x*x
        power=power//2

    return sol
##O(log(power))

if __name__=="__main__":
    print(gcd(5,7))

    prime(10)
    mapper={1:"a",
            2:"z",
            -3:"j",-5:"j"}

   ## "Important Sorting techniques"
    print(mapper)
    print(dict(sorted(mapper.items())))
    print(dict(sorted(mapper.items() ,key=lambda item:(item[1],item[0]))))
    print(mapper.items())
    arr=["a","b","c"]
  ##"Combinations"
    print(list(itertools.combinations(arr,2)))


    arr=[1,2,3,5,6,8,8,11,15]
   ##      0 1 2 3 4 5 6 7 8
   ##"Binary Search"
    print(bisect.bisect_left(arr,8))


    print(fast_power(7,3))
