'''
question link:
https://leetcode.com/problems/combination-sum-iii/description/
'''

import copy
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        d=defaultdict(list)
        ans=[]
        for i in range(1,10):
            r=copy.deepcopy(d)
            p=list(r.keys())
            for j in p:
                if j+i>n:
                    continue
                for q in d[j]:
                    if len(q)!=k:
                        r[j+i].append(q+[i])
            r[i].append([i])
            d=copy.deepcopy(r)
        for arr in d[n]:
            if len(arr)==k:
                ans.append(arr)
        return ans
