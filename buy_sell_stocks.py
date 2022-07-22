def buy_sell_stocks(prices):
    # Write your code here
    maxDiff = 0;
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            currentDiff = (prices[j] - prices[i])
            if currentDiff > maxDiff:
                maxDiff = currentDiff
    return maxDiff