class Solution:
    def generate(self, numRows):
        if numRows==1:
            return [[1]]
        if numRows<2:
            return [[[1] for i in range(x+1)] for x in range(numRows)]
        ls=[[1],[1,1]]+[[] for x in range(numRows-2)]
        for i in range(2,numRows):
            tmp=[  ls[i-1][j-1]+ls[i-1][j]  for j in range(1,len(ls[i-1]))]
            tmp=[1]+tmp+[1]
            ls[i]+=tmp
        return ls
a=Solution()
b=a.generate(2)
print(b)


