'''
question link:
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        def compute(num1,num2,op):
            ans=0
            if op=='/':
                ans=(num1/num2)
                if ans<0:
                    ans=ceil(ans)
                else:
                    ans=floor(ans)
            elif op=='*':
                ans=num1*num2
            elif op=='-':
                ans=num1-num2
            else:
                ans=num1+num2
            return ans
        for i in tokens:
            if i=='/' or i=='+' or i=='-' or i=='*':
                n2=stack.pop()
                n1=stack.pop()
                stack.append(compute(n1,n2,i))
            else:
                stack.append(int(i))
        return stack[0]
