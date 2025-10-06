prin = int(input("Enter the Principle Amount"))
rate = float(input("Enter the Rate of Interest"))
time = int(input("Enter the Time Period"))


si = (prin * time * rate)/100
ci = prin * ((1 + rate/100) ** time) - prin

print(f"Simple Interest is {si:.2f}")
print(f"Compound Intrest is {ci:.2f}")
