#The goal of this program is to be able to do math equations and conversions

import math

def hello():
    print("\nWelcome to my program!")
    print("\nThe goal of this program is to answer math equations and conversions using Python.\n")

running = True

def A_R():
    try:
        l = float(input("\nWhat is the length of the rectangle: "))
        w = float(input("\nWhat is the width of the rectangle: "))
        print(f"\nThe rectangle has an area of {w * l}.")
    except:
        print("\nThat is not a valid number!")

def A_P():
    try:
        b = float(input("\nWhat is the base of the parallelogram: "))
        h = float(input("\nWhat is the height of the parallelogram: "))
        print(f"\nThe parallelogram has an area of {b * h}.")
    except:
        print("\nThat is not a valid number!")

def A_Te():
    try:
        b = float(input("\nWhat is the base of the triangle: "))
        h = float(input("\nWhat is the height of the triangle: "))
        area = float(.5 * (b*h))
        print(f"\nThe triangle has an area of {area}.")
    except:
        print("\nThat is not a valid number!")

def A_Tp():
    try:
        b1 = float(input("\nWhat is the 1st base of the trapizoid: "))
        b2 = float(input("\nWhat is the 2nd base of the trapizoid: "))
        h = float(input("\nWhat is the height of the trapizoid: "))
        area = float(.5 * h * (b1*h))
        print(f"\nThe trapizoid has an area of {area}.")
    except:
        print("\nThat is not a valid number!")

def A_C():
    try:
        deci = int(input("\nUp to how many decimal places do you want? "))
        r = float(input("\nWhat is the radius of the circle: "))
        area = float(math.pi * (r**2))
        area = round(area, deci)
        print(f"\nThe circle has an area of {area}.")
    except:
        print("\nThat is not a valid number!")

list_of_math = {
    1: 'Area of a Rectangle ',
    2: 'Area of a Parallelogram ',
    3: 'Area of a Triangle ',
    4: 'Area of a Trapizoid ',
    5: 'Area of a circle',
}

conversions = {
    1: ''
} #This dictionary is for converting measurements (wip) for now

while running:

    hello()

    for key, value in list_of_math.items():
        print(f"Your choices are {key}: {value}.\n")
    choice = float(input("Please select a number: "))
    if choice == 1:
        A_R()
    elif choice == 2:
        A_P()
    elif choice == 3:
        A_Te()
    elif choice == 4:
        A_Tp()
    elif choice == 5:
        A_C()
    






    program = input("\nWould you like to run it again? (Y/N) ")
    if program.lower() == "n":
        break
    elif program == "":
        break

print("\nThanks for using my program!")
print("\nFeel free to add on to this!\n")