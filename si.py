prin = int(input("Enter the Principle Amount"))
rate = float(input("Enter the Rate of Interest"))
time = int(input("Enter the Time Period"))
n = 12

si = (prin * time * rate)/100
ci = p * ((1 + r/100) ** t) - p

print(f"Simple Interest is {si:.2f}")
print(f"Compound Intrest is {ci:.2f}")
