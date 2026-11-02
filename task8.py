qty, rate, waste, labour, machine, units, price, target = 100, 50, 5, 2000, 1500, 100, 75, 20
material = qty*rate; total_cost = material + material*waste/100 + labour + machine
revenue = units*price; profit = revenue-total_cost
print("Cost:", total_cost, "Unit cost:", round(total_cost/units,2), "Profit:", profit, "Target met:", profit >= total_cost*target)