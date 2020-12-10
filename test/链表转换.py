
class Node:
    def __init__(self,n):
        self.val=n
        self.next=None

class Solution:
    def reorderList(self,head):
        ls=list(range(1,5))
        head=self.ls_node(ls)




        ls=self.node_ls(head)
        len_ = len(ls)
        res = []
        if len_ % 2 == 0:
            mid = len_ // 2
            left = ls[:mid]
            right = ls[mid:]
            right = right[::-1]

            for i in range(len(right)):
                res.append(left[i])
                res.append(right[i])

        if len_ % 2 != 0:
            mid = len_ // 2
            left = ls[:mid]
            right = ls[mid + 1::]
            right = right[::-1]
            mid = ls[mid]

            for i in range(len(right)):
                res.append(left[i])
                res.append(right[i])
            res.append(mid)
        res=self.ls_node(res)
        head.next=res
        return head


    #列表转链表
    def ls_node(self,ls):
        head=Node(None)
        p=head
        for i in ls:
            p.next=Node(i)
            p=p.next
        return head.next

#链表转列表
    def node_ls(self,head):
        ls=[]
        while True:
            v=head.val
            ls.append(v)
            head=head.next
            if head==None:
                return ls

#删除倒数第三个节点
def del_node(head,n):
    p=head
    if p.next==None:
        return None
    while True:
        t=p
        for i in range(n):
            t=t.next
        if t==None:
            break
        p=p.next
    p.next=p.next.next
    return head


a=Solution()
print(a.reorderList(1))



