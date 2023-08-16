class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth=0
        for i in range(len(accounts)):
            totalwealth=sum(accounts[i])
            maxwealth=max(maxwealth,totalwealth)
            
        return maxwealth
        