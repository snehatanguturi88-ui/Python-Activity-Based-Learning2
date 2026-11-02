applicants = [("Asha", 88, [80, 75, 90], 92, 250000), ("Ravi", 82, [65, 70, 60], 80, 200000), ("Mina", 79, [90, 90, 90], 95, 150000)]
eligible = [a for a in applicants if a[1] >= 80 and min(a[2]) >= 60 and a[3] >= 75 and a[4] <= 300000]
eligible.sort(key=lambda a: (-a[1], -a[3], a[4]))
print([(a[0], a[1]) for a in eligible] or "No eligible applicants")