pi = 3.14
def vol():
    radius = float(input("Enter circle radius: "))
    height = float(input("Enter circle height: "))
    volume = pi*pow(radius,2)*height # gets the result of the value of pi, uses the inbuilt power function to power to 2 for twice the radius and input of height
    return volume
print (vol()) # returns the result of the equation
