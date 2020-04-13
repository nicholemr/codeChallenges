
def get_max_profit(stock_prices):

    min_price, max_price = None, None
    min_price_diff = None

    for i, p in enumerate(stock_prices):
        if not min_price:
            min_price = p
        elif not max_price:
            max_price = p
            min_price_diff = max_price-min_price
        elif p < min_price:
            min_price = p
            max_price = None
        elif p > max_price:
            max_price = p

        if 1 < i < len(stock_prices)-1:
            current_diff = stock_prices[i+1]-p
            if current_diff < min_price_diff:
                min_price_diff = current_diff

    if max_price:
        return max(max_price-min_price, min_price_diff)
    return None


p = [9, 7, 4, 1]
p = [7, 2, 8, 9]
# p = []
# p = [1, 5, 3, 2]
# p = [1, 7, 6, 5, 4, 9, 9]

print(get_max_profit(p))
