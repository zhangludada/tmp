class Solution:
    def merge(self, intervals):
        len_=len(intervals)
        if len_==0:
            return []
        elif len_==1:
            return [intervals[0]]
        else:
            intervals=sorted(intervals,key=lambda x:x[0])
            res=[]
            start=intervals[0][0]
            max_=intervals[0][1]

            for i in range(1,len_):
                now,left=intervals[i],intervals[i-1]
                #连续
                if now[0]<=max_:
                    pass

                #非连续
                else:
                    end=max_
                    res.append([start,end])
                    start=now[0]
                    max_=now[1]
                max_ = max(max_, now[1])
                #遍历到最后
                if i>=len_-1:
                    end=max_
                    res.append([start,end])
        return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
a=Solution()
print(a.merge(intervals))



