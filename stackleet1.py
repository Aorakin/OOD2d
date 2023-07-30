class Solution:
    def buildArray(self, target, n: int):
        tempstack = []
        result = []
        count=0
        for i in range(1,n+1):
            if tempstack == target:
                break
            else :
                tempstack.append(i)
                result.append("Push")
                if target[count] == tempstack[-1] :
                   count +=1
                else:
                     tempstack.pop()
                     result.append("Pop")
        return result
test =Solution()
print(test.buildArray([1,2], 4))