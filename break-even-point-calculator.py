from tabulate import tabulate

# Declare base number
i = 1
j = 0
number = 1
cost_of_goods = 0

# Set data array
data = [[] for _ in range(number)]
item_database = [["Item Type",
                  "Item Price (Rp)",
                  "Item Amount (Unit)",
                  "Item Total (Rp)"]]
item_output = [["Cost of Goods",
                "Cost of Goods per Unit",
                "Price Amounts",
                "Break Even Point Units"]]
total_data = []
output = []

# Check User
answer = input("Wanna input something? (y/n) ")
print("Input item,price,amount")
while answer == 'y':
    data = [[] for _ in range(number)]
    # Input data (item, price, amount)
    item, price, amount = map(str, input("Item {}: ".format(i)).split(","))
    # Adding data into array
    data[j].append(item)
    data[j].append(price)
    data[j].append(amount)
    data[j].append(int(price) * int(amount))
    total_data.append(int(price) * int(amount))
    # Adding data into main output item data array
    item_database.append(data[j])
    i += 1
    j += 1
    number += 1
    # Check User 2
    answer = input("Wanna add another one? ")

# Set unit and profit amount
unit_amount = int(input("How much Unit you gonna product: "))
profit_amount = int(input("How much Profit you wanna get: "))

# Sum all the total amount
for i in range(len(total_data)):
    cost_of_goods += total_data[i]

# Calculate HPP, HPP per unit, BEP price, and BEP unit
cost_of_goods_per_unit = cost_of_goods / unit_amount
break_even_point_price = cost_of_goods_per_unit * (100 + profit_amount) / 100
break_even_point_per_units = cost_of_goods / break_even_point_price

# Adding data into output array
output.append(cost_of_goods)
output.append(int(cost_of_goods_per_unit))
output.append(int(break_even_point_price))
output.append(int(break_even_point_per_units))
item_output.append(output)

# Print all the data into a table visualization
print(tabulate(item_database, tablefmt="fancy_grid"))
print(tabulate(item_output, tablefmt="fancy_grid"))
