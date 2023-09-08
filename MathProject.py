#The goal of this program is to be able to do math equations and conversions

import math

def hello():
    print("\nWelcome To My Program!")
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
        print("\nYou Have Selected Converting Meters To Centimeters.")
        meters = input("\nHow Many Meters: ")
        result = float(meters) * 100
        print(f"\nYou Converted {meters} Meters To {result} Centimeters.")
    except:
        no()

def ccm():
    try:
        print("\nYou Have Selected Converting Centimeters To Meters.")
        centimeters = input("\nHow Many Centimeters: ")
        result = float(centimeters) / 100
        print(f"\nYou Converted {centimeters} Centimeters To {result} Meters.")
    except:
        no()

def cmk():
    try:
        print("\nYou Have Selected Converting Meters To Kilometers.")
        meters = input("\nHow Many Meters: ")
        result = float(meters) / 1000
        print(f"\nYou Converted {meters} Meters To {result} Kilometers.")
    except:
        no()

def ckm():
    try:
        print("\nYou Have Selected Converting Kilometers To Meters.")
        kilometers = input("\nHow Many Kilometers: ")
        result = float(kilometers) * 1000
        print(f"\nYou Converted {kilometers} Kilometers To {result} Meters.")
    except:
        no()

def cck():
    try:
        print("\nYou Have Selected Converting Centimeters To Kilometers.")
        centimeters = input("\nHow Many Centimeters: ")
        result = float(centimeters) / 100000
        print(f"\nYou Converted {centimeters} Centimeters To {result} Kilometers.")
    except:
        no()

def ckc():
    try:
        print("\nYou Have Selected Converting Kilometers To Centimeters.")
        kilometers = input("\nHow Many Kilometers: ")
        result = float(kilometers) * 100000
        print(f"\nYou Converted {kilometers} Kilometers To {result} Centimeters.")
    except:
        no()

def cif():
    try:
        print("\nYou Have Selected Converting Inches To Feet.")
        inches = input("\nHow Many Inches: ")
        result = float(inches) / 12
        print(f"\nYou Converted {inches} Inches To {result} Feet.")
    except:
        no()

def ciy():
    try:
        print("\nYou Have Selected Converting Inches To Yards.")
        inches = input("\nHow Many Inches: ")
        result = float(inches) / 36
        print(f"\nYou Converted {inches} Inches To {result} Yards.")
    except:
        no()

def cim():
    try:
        print("\nYou Have Selected Converting Inches To Miles.")
        inches = input("\nHow Many Inches: ")
        result = float(inches) / (12 * 5280)
        print(f"\nYou Converted {inches} Inches To {result} Miles.")
    except:
        no()

def cfi():
    try:
        print("\nYou Have Selected Converting Feet To Inches.")
        feet = input("\nHow Many Feet: ")
        result = float(feet) * 12
        print(f"\nYou Converted {feet} Feet To {result} Inches.")
    except:
        no()

def cfy():
    try:
        print("\nYou Have Selected Converting Feet To Yards.")
        feet = input("\nHow Many Feet: ")
        result = float(feet) / 3
        print(f"\nYou Converted {feet} Feet To {result} Yards.")
    except:
        no()

def cfm():
    try:
        print("\nYou Have Selected Converting Feet to Miles.")
        feet = input("\nHow Many Feet: ")
        result = float(feet) / 5280
        print(f"\nYou Converted {feet} Feet To {result} Miles.")
    except:
        no()

def cyi():
    try:
        print("\nYou Have Selected Converting Yards To Inches.")
        yard = input("\nHow Many Yards: ")
        result = float(yard) * 36
        print(f"\nYou Converted {yard} Yards To {result} Inches.")
    except:
        no()

def cyf():
    try:
        print("\nYou Have Selected Converting Yards To Feet.")
        yard = input("\nHow Many Yards: ")
        result = float(yard) * 3
        print(f"\nYou Converted {yard} Yards To {result} Feet.")
    except:
        no()

def cym():
    try:
        print("\nYou Have Selected Converting Yards To Miles.")
        yard = input("\nHow Many Yards: ")
        result = (float(yard) * 3) / 5280
        print(f"\nYou Converted {yard} Yards To {result} Miles.")
    except:
        no()

def cmi():
    try:
        print("\nYou Have Selected Converting Miles To Inches.")
        mile = input("\nHow Many Miles: ")
        result = float(mile) * 63360
        print(f"\nYou Converted {mile} Miles To {result} Inches.")
    except:
        no()

def cmf():
    try:
        print("\nYou Have Selected Converting Miles To Feet.")
        mile = input("\nHow Many Miles: ")
        result = float(mile) * 5280
        print(f"\nYou Converted {mile} Miles To {result} Feet.")
    except:
        no()

def cmy():
    try:
        print("\nYou Have Selected Converting Miles To Yards.")
        mile = input("\nHow Many Miles: ")
        result = (float(mile) * 5280) / 3
        print(f"\nYou Converted {mile} Miless To {result} Yards.")
    except:
        no()

def cmiki():
    try:
        print("\nYou Have Selected Converting Miles To Kilometers.")
        mile = input("\nHow Many Miles: ")
        result = float(mile) * 1.609
        print(f"\nYou Converted {mile} Miles To {result} Kilometers.")
    except:
        no()

def ckimi():
    try:
        print("\nYou Have Selected Converting Kilometers To Miles.")
        kilometers = input("\nHow Many Kilometers: ")
        result = float(kilometers) / 1.609
        print(f"\nYou Converted {kilometers} Kilometers To {result} Miles.")
    except:
        no()

def tsm():
    try:
        print("\nYou Have Selected Converting Seconds To Minutes.")
        seconds = input("\nHow Many Seconds: ")
        result = float(seconds) / 60
        print(f"\nYou Converted {seconds} Seconds To {result} Minutes.")
    except:
        no()

def tsh():
    try:
        print("\nYou Have Selected Converting Seconds To Hours.")
        seconds = input("\nHow Many Seconds: ")
        result = float(seconds) / 3600
        print(f"\nYou Converted {seconds} Seconds To {result} Hours.")
    except:
        no()

def tms():
    try:
        print("\nYou Have Selected Converting Minutes To Seconds.")
        minutes = input("\nHow Many Minutes: ")
        result = float(minutes) * 60
        print(f"\nYou Converted {minutes} Minutes To {result} Seconds.")
    except:
        no()

def tmh():
    try:
        print("\nYou Have Selected Converting Minutes To Hours.")
        minutes = input("\nHow Many Minutes: ")
        result = float(minutes) / 60
        print(f"\nYou Converted {minutes} Minutes To {result} Hours.")
    except:
        no()

def ths():
    try:
        print("\nYou Have Selected Converting Hours To Seconds.")
        hours = input("\nHow Many Hours: ")
        result = float(hours) * 3600
        print(f"\nYou Converted {hours} Hours To {result} Seconds.")
    except:
        no()

def thm():
    try:
        print("\nYou Have Selected Converting Hours To Minutes.")
        hours = input("\nHow Many Hours: ")
        result = float(hours) * 60
        print(f"\nYou Converted {hours} Hours To {result} Minutes.")
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
    3: 'Minutes to Seconds',
    4: 'Minutes to Hours',
    5: 'Hours to Seconds',
    6: 'Hours to Minutes',
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

    elif sel == "3":

        hello()

        for key3, value3 in timeconv.items():
            print(f"Your choices are {key3}: {value3}.\n")
        choice3 = input("Please select a number: ")
        choice3 = int(choice3)
        if choice3 == 1:
            tsm()
        elif choice3 == 2:
            tsh()
        elif choice3 == 3:
            tms()
        elif choice3 == 4:
            tmh()
        elif choice3 == 5:
            ths()
        elif choice3 == 6:
            thm()
    else:
        print("\nThat is not a valid choice!\n\nPlease run this program again!\n")
    
    program = input("\nWould you like to run the entire program again? (Y/N) ")
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