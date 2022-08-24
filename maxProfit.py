# # 1 Solution
# def maxProfit(prices):
#     max_profit = 0
#     min_price = prices[0]
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
#     return max_profit
#
#
# print(maxProfit(prices))

prices = [7, 1, 5, 3, 6, 4]
# 2 Solution
buy = prices[0]
sold = 0
for i in range(len(prices)):
    buy = min(buy, prices[i])
    sold = max(sold, prices[i] - buy)

print(sold)