class Solution:
    def reversePairs(self, nums):
        d={}
        l=[]
        for i in range(len(nums)):
            n=nums[i]
            d[n]=d.get(n,l)+[i]
        nums.sort()

        tmp=[]
        for j in nums:
            for i in nums[::-1]:
                if i>j*2:
                    if [i,j] not in tmp:
                        tmp.append([i,j])
                else:
                    break
        count=0
        for ls in tmp:
            i,j=ls[0],ls[1]
            for ii in d[i]:
                for jj in d[j]:
                    if ii<jj:
                        count+=1
        print(count)

a=[1,3,2,3,1]
a1=Solution()
b=a1.reversePairs(a)
