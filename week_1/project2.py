P = int(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
n = int(input("Enter the number of times that interest is compounded per year: "))
t = int(input("Enter the time period: "))
CI = P * (1 + R/n)**(n*t)
print("Compound Interest: ", CI)