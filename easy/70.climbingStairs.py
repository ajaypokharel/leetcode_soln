"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        x = self.fib(n, memo)
        
        return x
        
    def fib(self, n, memo):
        
        if n <= 1:
            return 1
        
        if memo.get(f'fib({n})'):
            return memo[f'fib({n})']
        else:
            memo[f'fib({n})'] = self.fib(n-1, memo) + self.fib(n-2, memo)
        
        return memo[f'fib({n})']