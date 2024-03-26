def calculate_stock_profit(allotment, final_share_price, sell_commission, initial_share_price, buy_commission, capital_gain_tax_rate):
    proceeds = allotment * final_share_price
    total_purchase_price = allotment * initial_share_price
    gross_profit = proceeds - total_purchase_price
    capital_gain_tax = (gross_profit - sell_commission - buy_commission) * (capital_gain_tax_rate / 100)
    cost = total_purchase_price + buy_commission + sell_commission + capital_gain_tax
    net_profit = proceeds - cost
    roi = (net_profit / cost) * 100
    break_even_price = (total_purchase_price + buy_commission + sell_commission) / allotment
    return proceeds, cost, net_profit, roi, break_even_price

ticker_symbol = input("Enter ticker symbol: ")
allotment = int(input("Enter allotment (number of shares): "))
final_share_price = float(input("Enter final share price (in dollars): "))
sell_commission = float(input("Enter sell commission (in dollars): "))
initial_share_price = float(input("Enter initial share price (in dollars): "))
buy_commission = float(input("Enter buy commission (in dollars): "))
capital_gain_tax_rate = float(input("Enter capital gain tax rate (%): "))

proceeds, cost, net_profit, roi, break_even_price = calculate_stock_profit(
    allotment, final_share_price, sell_commission, initial_share_price, buy_commission, capital_gain_tax_rate)

print(f"\nPROFIT REPORT for {ticker_symbol}:")
print(f"Proceeds: ${proceeds:,.2f}")
print(f"Cost: ${cost:,.2f}")
print(f"Net Profit: ${net_profit:,.2f}")
print(f"Return on Investment: {roi:.2f}%")
print(f"Break Even Price: ${break_even_price:.2f}")
