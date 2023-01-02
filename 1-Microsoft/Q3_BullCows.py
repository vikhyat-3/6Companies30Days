'''
question link:
https://leetcode.com/problems/bulls-and-cows/
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull,cow=0,0
        bullSet=set()
        d=defaultdict(int)
        for i in secret:
            d[i]+=1
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
                bullSet.add(i)
                d[secret[i]]-=1
                if d[secret[i]]==0:
                    del d[secret[i]]
        for i in range(len(secret)):
            if i in bullSet:
                continue
            if guess[i] in d:
                cow+=1
                d[guess[i]]-=1
                if d[guess[i]]==0:
                    del d[guess[i]]
        return str(bull)+'A'+str(cow)+'B'
