# Write a python program using function to convert Celsius to Fahrenheit.

print("\tTemperature Converter ")

def c_to_f(celsius):
    far = (9/5 * celsius) + 32
    return far

c = int(input("Enter Celsius value to convert in fahrenheit : "))
f = c_to_f(c)
print(f"{c} Celsius = {f} Fahrenheit")