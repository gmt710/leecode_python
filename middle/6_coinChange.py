class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 假设dp[i]表示凑够i元所需要的最少硬币数，一共有n种面值硬币，
        # 那么dp[i]=min(dp[i−coins[0]],dp[i−coins[1]],...dp[i−coins[k])+1，其中coins[k]<=i
        
        # dp[i]表示amount=i需要的最少coin数
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                 # 只有当硬币面额不大于要求面额数时，才能取该硬币
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        
        # 硬币数不会超过要求总面额数，如果超过，说明没有方案可凑到目标值
        if dp[amount] <= amount:
            return dp[amount]
        else:
            return -1
        
