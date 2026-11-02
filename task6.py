distance, multiplier, ages, cancelled = 180, 2.0, [30, 65, 4], False
base = min(distance,100)*1.5 + max(distance-100,0)*1.2
fares = [0 if a < 5 else base*multiplier*(0.8 if a >= 60 else 1)+40 for a in ages]
total = sum(fares); penalty = total*0.25 if cancelled else 0
print("Fares:", fares, "Total:", total, "Penalty:", penalty, "Refund:", total-penalty if cancelled else 0)