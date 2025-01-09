#1. Create a float object named weight with the value of 0.2, and create a string object with the value "newt".
# Then use these objects to print the following string, "0.2 kg is the weight of the newt"
weight = 0.2
animal = "newt"
print(str(weight) + " kg is the weight of the " + animal)
#2. Display the same string by using .format() and empty {} placeholders
print("{} kg is the weight of the {}".format(weight,animal))

#3. Display the same string using an f-string
print(f"{weight} kg is the weight of the {animal}")