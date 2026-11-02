age, consult, tests, treatment, paid = 65, 500, 1200, 3000, 2000

if age < 0 or min(consult, tests, treatment, paid) < 0:
    print("Invalid billing data")

else:
    total = consult * (0.9 if age >= 60 else 1) + tests + treatment

    if paid > total:
        print("Invalid billing data")

    else:
        balance = total - paid

        status = "Paid" if balance == 0 else "Part-paid" if paid > 0 else "Unpaid"

        print("Bill:", total)
        print("Balance:", balance)
        print("Status:", status)