# Write a python function which converts inches to cms.

print("\tInch to cm converter")

def i_to_c(i):
    return(2.54 * i)

inch = int(input("Enter inch value : "))
print(f"{i_to_c(inch)} cm")