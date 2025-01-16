prompt1 = "Give me a base: "
prompt2 = "Give me an exponent: "
response1 = input(prompt1)
response2 = input(prompt2)
base = float(response1)
exponent = float(response2)
result = base ** exponent
print(response1 + " to the power of " + response2 + " = " + f"{result:.2f}")