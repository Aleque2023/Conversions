#The goal of this program is to be able to do math equations and conversions

import math

def hello():
    print("\nWelcome to my program!")
    print("\nThe goal of this program is to answer math equations and conversions using Python.\n")

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

def cmc():
    try:
        print("\nYou have selected converting Meters to Centimeters")
        meters = input("\nHow many meters: ")
        result = float(meters) * 100
        print(f"\nYou converted {meters} meters to {result} centimeters.")
    except:
        print("\nThat is not a valid number!")

def ccm():
    try:
        print("\nYou have selected converting Centimeters to Meters")
        centimeters = input("\nHow many centimeters: ")
        result = float(centimeters) / 100
        print(f"\nYou converted {centimeters} centimeters to {result} meters.")
    except:
        print("\nThat is not a valid number!")

def cif():
    try:
        print("\nYou have selected converting Inches to Feet")
        inches = input("\nHow many inches: ")
        result = float(inches) / 12
        print(f"\nYou converted {inches} inches to {result} feet.")
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
    1: 'Meters to Centimeters',
    2: 'Centimeters to Meters',
    3: 'Inches to Feet',
    4: 'Inches to Yards',
    5: 'Inches to Miles',
    6: 'Feet to Inches',
    7: 'Feet to Yards',
    8: 'Feet to Miles',
    9: 'Yards to Inches',
    10: 'Yards to Feet',
    11: 'Yards to Miles',
    12: 'Miles to Inches',
    13: 'Miles to Feet',
    14: 'Miles to Yards',
} #This dictionary is for converting measurements (wip) for now

Select = {
    1: "Converting Measurements",
    2: "Calcuating the Area",
}

run = 0
while run == 0:

    for x in Select.keys():
        print(f"\nYour choices are {x}: {Select[x]}")    
    sel = input("\nEnter a number: ")
    if sel == "1":

        hello()

        for key1, value1 in conversions.items():
            print(f"Your choices are {key1}: {value1}.\n")
        choice1 = int(input("Please select a number: "))

        if choice1 == 1:
            cmc()
        elif choice1 == 2:
            ccm()
        elif choice1 == 3:
            cif()
        else:
            program = input("\nWould you like to run it again? (Y/N) ")
            if program.lower() == "n":
                continue
            elif program == "":
                continue

    elif sel == "2":
        
        hello()

        for key2, value2 in list_of_math.items():
            print(f"Your choices are {key2}: {value2}.\n")
        choice2 = input("Please select a number: ")
        choice2 = int(choice2)
        if choice2 == 1:
            A_R()
        elif choice2 == 2:
            A_P()
        elif choice2 == 3:
            A_Te()
        elif choice2 == 4:
            A_Tp()
        elif choice2 == 5:
            A_C()
        else:
            program2 = input("\nWould you like to run it again? (Y/N) ")
            if program2.lower() == "n":
                continue
            elif program2 == "":
                continue
    else:
        print("\nThat is not a valid choice!\n\nPlease run this program again!\n")
    
    program = input("\nWould you like to run it again? (Y/N) ")
    if program.lower() == "n":
        run += 1
        break
    elif program == "":
        run += 1
        break
    elif program.lower() == "y":
        run == 0

print("\nThanks for using my program!")
print("\nFeel free to add on to this!\n")