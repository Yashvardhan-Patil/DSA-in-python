class Solution(object):
    def minBitFlips(self, start, goal):
        n=start ^ goal
        count=0
        for i in range (0,32):
            if n & (1<<i)!=0:
                count+=1
        return count

            
        
        