'''
question link:
https://leetcode.com/problems/largest-divisible-subset/description/
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        d={}
        m=1
        answer=[nums[0]]
        for i in nums:
            p=list(d.keys())
            for j in p:
                if i%j==0:
                    if i not in d:
                        d[i]=d[j]+[i]
                        if len(d[i])>m:
                            m=len(d[i])
                            answer=d[i]
                    else:
                        if len(d[i])<len(d[j])+1:
                            d[i]=d[j]+[i]
                            if len(d[i])>m:
                                m=len(d[i])
                                answer=d[i]
            if i not in d:
                d[i]=[i]
        return answer

        
