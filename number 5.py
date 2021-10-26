def fahrenheit():
    f = eval(input("Enter a temperature in Fahrenheit: "))
    c = 5/9 * (f-32)
    print("Temperature in Fahrenheit is: ",f)
    print("Temperature in celsius is: ", c)
    return c
   
def convert_temperature():
    a = fahrenheit()
    k = a + 273.15
    print("The temperature in kelvin is: ", k)

convert_temperature()

# Input temp in fahrenheit
# Convert it to celsius
# Return the Value
# Store the value with variable a
# Convert to kelvin 
# Print the value