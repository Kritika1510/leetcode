class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in sentences:
            c=i.split()
            if len(c)>ans:
                ans=len(c)
            
        return ans
        

            
            
        