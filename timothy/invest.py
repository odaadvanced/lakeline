def invest (amount, rate, years):
    print("Here's what your investment will look like:")
    for n in range(1, years + 1):
        print(f"Year {n}: ${(amount * (1 + rate) ** n):.2f}")
        
amount = float(input("How much would you like to deposit initially?"))
rate = float(input("What is the rate of the interest?"))
years = int(input("How many years will you leave your investment in?"))

invest(amount, rate, years)