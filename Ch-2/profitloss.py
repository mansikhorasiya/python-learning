selling_price =int(input("Enter the  selling price: "))
cost_price = int(input("Enter the cost price:"))

# if sp > cp mean ->>profit
if selling_price > cost_price :
    profit = selling_price - cost_price
    print("We have made profit..",profit)

# if sp < cp mean ->>loss
elif selling_price < cost_price :
    loss = cost_price - selling_price
    print("We have made loss..",loss) 

# if sp = cp mean ->>NO profit No loss
else:
    print("We made NO profit No loss...")