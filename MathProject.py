#The goal of this program is to be able to do math equations and conversions

import math

def hello():
    print("\nWelcome to my program!")
    print("\nThe goal of this program is to answer math equations and conversions using Python.\n")

def no():
    print("\nThat Is Not A Valid Number!")

def A_R():
    try:
        l = float(input("\nWhat is the length of the rectangle: "))
        w = float(input("\nWhat is the width of the rectangle: "))
        print(f"\nThe rectangle has an area of {w * l}.")
    except:
        no()

def A_P():
    try:
        b = float(input("\nWhat is the base of the parallelogram: "))
        h = float(input("\nWhat is the height of the parallelogram: "))
        print(f"\nThe parallelogram has an area of {b * h}.")
    except:
        no()

def A_Te():
    try:
        b = float(input("\nWhat is the base of the triangle: "))
        h = float(input("\nWhat is the height of the triangle: "))
        area = float(.5 * (b*h))
        print(f"\nThe triangle has an area of {area}.")
    except:
        no()

def A_Tp():
    try:
        b1 = float(input("\nWhat is the 1st base of the trapizoid: "))
        b2 = float(input("\nWhat is the 2nd base of the trapizoid: "))
        h = float(input("\nWhat is the height of the trapizoid: "))
        area = float(.5 * h * (b1*h))
        print(f"\nThe trapizoid has an area of {area}.")
    except:
        no()

def A_C():
    try:
        deci = int(input("\nUp to how many decimal places do you want? "))
        r = float(input("\nWhat is the radius of the circle: "))
        area = float(math.pi * (r**2))
        area = round(area, deci)
        print(f"\nThe circle has an area of {area}.")
    except:
        no()

def cmc():
    try:
        print("\nYou have selected converting Meters to Centimeters")
        meters = input("\nHow many meters: ")
        result = float(meters) * 100
        print(f"\nYou converted {meters} meters to {result} centimeters.")
    except:
        no()

def ccm():
    try:
        print("\nYou have selected converting Centimeters to Meters")
        centimeters = input("\nHow many centimeters: ")
        result = float(centimeters) / 100
        print(f"\nYou converted {centimeters} centimeters to {result} meters.")
    except:
        no()

def cmk():
    try:
        print("\nYou have selected converting Meters to Kilometers")
        meters = input("\nHow many meters: ")
        result = float(meters) / 1000
        print(f"\nYou converted {meters} meters to {result} kilometers.")
    except:
        no()

def ckm():
    try:
        print("\nYou have selected converting Kilometers to Meters")
        kilometers = input("\nHow many Kilometers: ")
        result = float(kilometers) * 1000
        print(f"\nYou converted {kilometers} Kilometers to {result} Meters.")
    except:
        no()

def cck():
    try:
        print("\nYou have selected converting Centimeters to Kilometers")
        centimeters = input("\nHow many Centimeters: ")
        result = float(centimeters) / 100000
        print(f"\nYou converted {centimeters} centimeters to {result} Kilometers.")
    except:
        no()

def ckc():
    try:
        print("\nYou have selected converting Kilometers to Centimeters")
        kilometers = input("\nHow many Kilometers: ")
        result = float(kilometers) * 100000
        print(f"\nYou converted {kilometers} Kilometers to {result} Centimeters.")
    except:
        no()

def cif():
    try:
        print("\nYou have selected converting Inches to Feet")
        inches = input("\nHow many inches: ")
        result = float(inches) / 12
        print(f"\nYou converted {inches} inches to {result} feet.")
    except:
        no()

def ciy():
    try:
        print("\nYou have selected converting Inches to Yards")
        inches = input("\nHow many inches: ")
        result = float(inches) / 36
        print(f"\nYou converted {inches} Inches to {result} Yards.")
    except:
        no()

def cim():
    try:
        print("\nYou have selected converting Inches to Miles")
        inches = input("\nHow many inches: ")
        result = float(inches) / (12 * 5280)
        print(f"\nYou converted {inches} Inches to {result} Miles.")
    except:
        no()

area = {
    1: 'Area of a Rectangle ',
    2: 'Area of a Parallelogram ',
    3: 'Area of a Triangle ',
    4: 'Area of a Trapizoid ',
    5: 'Area of a circle',
}

disconv = {
    1: 'Meters to Centimeters',
    2: 'Centimeters to Meters',
    3: 'Meters to Kilometers',
    4: 'Kilometers to Meters',
    5: 'Centimeters to Kilometers',
    6: 'Kilometers to Centimeters',
    7: 'Inches to Feet',
    8: 'Inches to Yards',
    9: 'Inches to Miles',
    10: 'Feet to Inches',
    11: 'Feet to Yards',
    12: 'Feet to Miles',
    13: 'Yards to Inches',
    14: 'Yards to Feet',
    15: 'Yards to Miles',
    16: 'Miles to Inches',
    17: 'Miles to Feet',
    18: 'Miles to Yards',
    19: 'Miles to Kilometers',
    20: 'Kilometers to Miles',
}

timeconv = {
    1: 'Seconds to Minutes',
    2: 'Seconds to Hours',
}

Select = {
    1: 'Converting Measurements',
    2: 'Calcuating the Area',
    3: 'Converting Time',
    4: 'Converting Weight',
}

run = 0
while run == 0:

    for x in Select.keys():
        print(f"\nYour choices are {x}: {Select[x]}")    
    sel = input("\nEnter a number: ")
    if sel == "1":

        hello()

        for key1, value1 in disconv.items():
            print(f"Your choices are {key1}: {value1}.\n")
        choice1 = int(input("Please select a number: "))
################# The C in the definitions stands for convert.
################# The letters followed by C stands for what is converted
################# EX: cmc = convert meters to centimeters and so forth
        if choice1 == 1:
            cmc()
        elif choice1 == 2:
            ccm()
        elif choice1 == 3:
            cmk()
        elif choice1 == 4:
            ckm()
        elif choice1 == 5:
            cck()
        elif choice1 == 6:
            ckc()
        elif choice1 == 7:
            cif()
        elif choice1 == 8:
            ciy()
        elif choice1 == 9:
            cim()
        elif choice1 == 10:
            cfi()
        elif choice1 == 11:
            cfy()
        elif choice1 == 12:
            cfm()
        elif choice1 == 13:
            cyi()
        elif choice1 == 14:
            cyf()
        elif choice1 == 15:
            cym()
        elif choice1 == 16:
            cmi()
        elif choice1 == 17:
            cmf()
        elif choice1 == 18:
            cmy()
        elif choice1 == 19:
            cmiki()
        elif choice1 == 20:
            ckimi()
        else:
            program = input("\nWould you like to run it again? (Y/N) ")
            if program.lower() == "n":
                continue
            elif program == "":
                continue

    elif sel == "2":
        
        hello()

        for key2, value2 in area.items():
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

    elif sel == "3":

        hello()

        for key3, value3 in timeconv.items():
            print(f"Your choices are {key3}: {value3}.\n")
        choice3 = input("Please select a number: ")
        choice3 = int(choice3)
        if choice3 == 1:

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