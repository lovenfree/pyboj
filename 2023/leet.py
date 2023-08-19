from ast import List


def maxSlidingWindow(nums, k: int):
    res = list()
    
    for i in range(len(nums)-k+1):
        max = 0
        for j in range(i,i+k):
            if nums[j]>max:
                max=nums[j]
        res.append(max)
    print(res)
    return res

if __name__=="__main__":

    a= [1,-1]
    k = 1

    maxSlidingWindow(a,k)

            