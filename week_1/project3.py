P = int(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
n = int(input("Enter the number of times that interest is compounded per year: "))
Fv =P * (1 + R)**(n) - 1 / R
print("Future Value: ", Fv)
