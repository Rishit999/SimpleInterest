def compound_interest(prin, rate, time, n):
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return amount, interest
prin = int(input("Enter the Principle Amount"))
rate = float(input("Enter the Rate of Interest"))
time = int(input("Enter the Time Period"))
n = 12

si = (prin * time * rate)/100

print(f"Simple Interest is {si}")
