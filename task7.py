items = [("Book", 500, 2, 0.05), ("Bag", 1800, 2, 0.12)]
subtotal = sum(price*qty for name,price,qty,tax in items)
discount = min(subtotal*0.10, 1000) if subtotal >= 5000 else subtotal*0.05 if subtotal >= 2000 else 0
tax_total = sum((price*qty)*(1-discount/subtotal)*tax for name,price,qty,tax in items) if subtotal else 0; print("Subtotal:", subtotal)