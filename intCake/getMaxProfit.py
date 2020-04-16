
def get_max_profit(stock_prices):

    list_of_profits = []

    for i in range(len(stock_prices)-2):
        diff = max(stock_prices[i+1:]) - stock_prices[i]
        list_of_profits.append(diff)

    return max(list_of_profits)


p = [9, 7, 4, 1]
# p = [7, 2, 8, 9]
# p = []
# p = [1, 5, 3, 2]
# p = [1, 7, 6, 5, 4, 9, 9]

print(get_max_profit(p))
