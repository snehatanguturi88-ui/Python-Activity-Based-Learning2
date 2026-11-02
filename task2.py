units = [80, 120, 260]
energy = [min(u,100)*2 + max(min(u-100,100),0)*3 + max(u-200,0)*5 for u in units]
bills = [round((e+75)*1.05 - (50 if u < 100 else 0), 2) for e,u in zip(energy, units)]
print("Bills:", bills, "Unusual months:", [i+1 for i in range(1,len(bills)) if bills[i] > bills[i-1]*1.30])