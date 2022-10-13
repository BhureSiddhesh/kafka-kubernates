from yahoo_fin import stock_info as si

while True:
    data = si.get_live_price("amzn")
    print(data)