cao1 = int(input())
cao2 = int(input())

total_semanal_gramas = (cao1 + cao2) * 7

total_semanal_kg = total_semanal_gramas / 1000

if total_semanal_kg > int(total_semanal_kg):
    saco_kg = int(total_semanal_kg) + 1
else:
    saco_kg = int(total_semanal_kg)

print(f"{saco_kg}kg")