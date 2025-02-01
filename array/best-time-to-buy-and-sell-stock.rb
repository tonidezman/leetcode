# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    return 0 if prices.empty?

    best_buy = prices[0]
    profit = 0
    prices.each do |price|
        profit = [profit, price - best_buy].max
        best_buy = [best_buy, price].min
    end
    profit
end