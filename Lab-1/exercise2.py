name = str(input("Enter user name: "))
b_salary = int(input("Enter user base salary: "))
allowace = int(input("Enter allowace: "))

salary = b_salary + allowace

#print("0% tax" if salary <= 30000 else "5% tax" if 30000 < salary < 50000 else"10% tax" if 50000 < salary < 80000 else "15% tax")
if salary <= 30000:
    tax_rate = 0
elif salary < 50000:
    tax_rate = 5
elif salary < 80000:
    tax_rate = 10
else:
    tax_rate = 15

tax_amount = salary * (tax_rate / 100)
net_salary = salary - tax_amount
print(f"Tax amount {tax_amount}")
print(f"Net salary {net_salary}")