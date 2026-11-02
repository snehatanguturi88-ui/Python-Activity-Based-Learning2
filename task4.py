basic, allowances, overtime, incentive = 25000, 5000, 2000, 1000
gross = basic + allowances + overtime + incentive
deduction = min(gross, 20000)*0.05 + max(gross-20000, 0)*0.10
print(f"Gross: n{gross:.2f}\nDeduction: n{deduction:.2f}\nNet salary: n{gross-deduction:.2f}")