plans = [("Basic", 2, 100, 199, 28, 50, 1), ("Plus", 5, 300, 299, 56, 40, 1), ("Max", 10, 500, 499, 84, 20, 0.5)]
data, minutes, days, budget = 4, 250, 28, 400
costs = [(p[0], p[3]+max(data-p[1],0)*p[5]+max(minutes-p[2],0)*p[6]) for p in plans if p[4] >= days]
print(min((x for x in costs if x[1] <= budget), key=lambda x:x[1], default="No eligible plan"))