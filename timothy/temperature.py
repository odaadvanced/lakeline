def convert_cel_to_far():
    '''This function converts temperatures from Celsius to Farenheit.'''
    cel = float(input("Enter a temperature in degrees C: "))
    far = cel * 9 / 5 + 32
    print(f"{cel:.2f} degrees Celsius = {far:.2f} degrees Farenheit.")
    
def convert_far_to_cel():
    '''This function converts temperatures from Farenheit to Celsius'''
    far = float(input("Enter a temperature in degrees F: "))
    cel = (far - 32) * 5 / 9
    print(f"{far:.2f} degrees Farenheit = {cel:.2f} degrees Celsius.")

convert_cel_to_far()
convert_far_to_cel()