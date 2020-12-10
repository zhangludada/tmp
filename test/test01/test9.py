class Solution:
    def reversePairs(self, nums):
        len_=len(nums)
        tmp=[]*(len_-1)
        for i in range(len_):
            tmp.append([nums[i],i])
        tmp=sorted(tmp,key=lambda x:x[0])
        count=0
        for i in range(len_):
            for j in range(len_-1,i,-1):
                a,b=tmp[i],tmp[j]
                if b[0]>2*a[0]:
                    for bb in b[1:]:
                        for aa in a[1:]:
                            if bb<aa:
                                count+=1
                else:
                    break

        print(tmp)
        print(count)






a=[-5,-5]
a1=Solution()
b=a1.reversePairs(a)

