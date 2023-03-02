import bisect


def binary_window(arr):

    count=0
    for i in range(0,len(arr)):
        if arr[i]==1:
            count+=1
    window_size=count
    #sliding window
    start=0
    end=0
    counter=0
    solution=window_size
    while(start<len(nums)):
        if end-start+1<window_size:
            if nums[end]==1:
                counter+=1
            end+=1
        else:
            solution=min(solution,window_size-counter)
            if nums[start]==1:
                counter-=1
            start+=1
            end+=1
            if end==len(nums):
                break
            if nums[end]==1:
                counter+=1

    return solution


def subarray(nums):
    positive_index=None
    negative_index=None
    length=0
    product=1
    for i in range(0,len(nums)):
        if nums[i]==0:
            product=1
            positive_index=None
            negative_index=None
        else:
            product*=nums[i]
            if product>0:
                if positive_index==None:
                    positive_index=i

                length=max(length,i-positive_index+1)
            else:
                if negative_index==None:
                    negative_index=i

                length=max(length,i-negative_index+1)
    return length

if __name__=="__main__":
    # nums=[1,0,1,0,1,0,0,1,1,0,1]
    # print(binary_window(nums))
    arr1=[0,1,-2,-3,-4] #3
    #        1 -2 6 -24

    arr2=[-1,-2,-3,0,1] #2


    print(subarray(arr1))
    print(subarray(arr2))
    arr=[2,3,5,5]
    end=len(arr)-1
    start=0


