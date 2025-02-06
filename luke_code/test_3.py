a = float(input("enter number: "))
b = int(input("enter range: "))
for num_people in range(1,b):
    print(f"{num_people} people: $ {a / num_people:,.2f} each")
    
    