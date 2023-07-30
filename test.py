class Solution:
    # class stack():
    #     def __init__ (self,ls = None):
    #         if ls == None : self.items = []
    #         else : self.items = ls
    #     def push(self,inp) :self.items.append(inp)
    #     def pop(self) :return self.items.pop()
    #     def peek(self) : return self.items[-1]
    #     def size(self) : return len(self.items)

    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        result = []
        count = 0
        for i in pushed :
            stack.append(i)
            if stack[-1] == popped[count]:
                count+=1
                result.append(stack.pop())
        while stack !=[]:
            result.append(stack.pop())
        if result ==  popped: return True
        else : return False
# test = Solution()
# print(test.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))
a ="  0    "
class stack():
    def __init__(self):
        
# print(a.strip())
# print(len(a))