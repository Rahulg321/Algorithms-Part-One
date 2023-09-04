arr = [1,2]


def max_profit(prices):
    profit = 0

    if len(prices) <= 1:
        return 0

    lowest_price, lowest_price_index = get_lowest_price(prices)

    remaining_selling_days = prices[lowest_price_index:]
    print(remaining_selling_days)

    if len(remaining_selling_days) <= 1:
        return profit

    highest_price, highest_price_index = get_highest_price(remaining_selling_days)

    print("lowest_price", lowest_price)
    print("lowest_price_index", lowest_price_index)

    print("highest_price", highest_price)
    print("highest_price_index", highest_price_index)

    if highest_price > lowest_price:
        profit = highest_price - lowest_price

    return profit


def get_lowest_price(prices):
    i = 0
    lowest_price = prices[0]
    lowest_price_index = i

    while i < len(prices):
        if prices[i] < lowest_price:
            lowest_price = prices[i]
            lowest_price_index = i
        i += 1

    return lowest_price, lowest_price_index


def get_highest_price(prices):
    i = 0
    highest_price = prices[0]
    highest_price_index = i

    while i < len(prices):
        if prices[i] > highest_price:
            highest_price = prices[i]
            highest_price_index = i
        i += 1

    return highest_price, highest_price_index


print(max_profit(arr))
