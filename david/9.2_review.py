#1
food = ["rice", "beans"]
print(food)

#2
food.append("broccoli")
print(food)

#3
food.extend(["bread", "pizza"])
print(food)

#4
print(food[0:2])

#5
print(food[4])

#6
breakfast = "eggs, fruit, orange juice"
breakfast_list = breakfast.split(", ")
print(breakfast_list)

#7
print(len(breakfast_list))

#8
lengths = [len(breakfast_list[0]), len(breakfast_list[1]), len(breakfast_list[2])]
print(lengths)