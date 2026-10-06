temperatures = (30, 32, 28, 31, 33, 29)

print("Weekend Temperatures:")

for temperature in temperatures:
    print(temperature, "°C")

highest = max(temperatures)
lowest = min(temperatures)

print("\nHighest Temperature:", highest, "°C")
print("Lowest Temperature:", lowest, "°C")