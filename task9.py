expenses = [("Hotel", 200, 83), ("Food", 80, 83), ("Transport", 50, 83)]

converted = [(name, round(amount * rate * 1.02, 2)) for name, amount, rate in expenses]

total, budget = sum(x[1] for x in converted), 30000

print("Expenses:", converted,
      "Total:", total,
      "Largest:", max(converted, key=lambda x: x[1])[0],
      "Status:", "Within Budget" if total <= budget else "Over Budget")