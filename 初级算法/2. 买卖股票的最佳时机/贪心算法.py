"""
贪心算法求出局部最优解
"""


def max_profit(prices) -> int:
    sum = 0
    for i in range(len(prices) - 1, 0, -1):
        if prices[i] - prices[i - 1] <= 0:
            continue
        else:
            sum += prices[i] - prices[i - 1]
    return sum
