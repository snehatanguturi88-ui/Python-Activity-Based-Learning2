import math

venue, equipment, catering, transport, certificate, sponsor, fee, participants = 12000, 5000, 150, 40, 10, 8000, 300, 100

fixed = venue + equipment
variable = catering + transport + certificate
total = fixed + variable * participants

break_even = math.ceil(max(fixed - sponsor, 0) / (fee - variable)) if fee > variable else "Impossible"

print("Fixed Cost:", fixed)
print("Variable Cost per Participant:", variable)
print("Total Event Cost:", total)
print("Break-even Participants:", break_even)
print("Total Revenue:", fee * participants)