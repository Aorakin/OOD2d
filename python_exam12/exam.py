class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs :
            temp = strs[0]
        check = 1
        for i in range(1,len(strs)+1):
            if len(strs[i-1]) == 0:
                return ""
            else:
                for j in range(len(strs[i-1])):  
                    if check > len(strs[i-1]):
                        check = len(strs[i-1])
                    if strs[i-1][:check]!=temp[:check]:
                        if   check !=0:
                            check-=1   
                        else : 
                            break
                    elif check == 0  : 
                            return("")
                    elif strs[i-1][:check]==temp[:check] and strs[i-1][:check+1]!=temp[:check+1]:
                        break
                    elif i != len(strs) : 
                        check +=1
            
        if strs[-1][:2] == strs[-1][-2:] and check >2:
            check = 2
        return strs[-1][:check]

