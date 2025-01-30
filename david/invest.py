def invest (amount, rate, years):
    loop = 0
    print(f"Begining amount: {amount}$")
    for year in range(years):
        loop = loop + 1
        amount = round((amount * rate) + amount, 2)
        print(f"year {loop}: {amount}$")

input_amount = round(float(input("Input a starting amount:")), 2)
input_rate = float(input("Input a rate:"))
input_years = int(input("Input years:"))
invest(input_amount, input_rate, input_years)

