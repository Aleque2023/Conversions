#The goal of this program is to be able to do math equations and conversions

import math

def hello():
    print(f"\nWelcome To {Select[x]}!\n")

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

def wgm():
    try:
        print("\nYou Have Selected Converting Grams To Milligrams.")
        grams = input("\nHow Many Grams: ")
        result = float(grams) * 1000
        print(f"\nYou Converted {grams} Grams To {result} Milligrams.")
    except:
        no()

def wgk():
    try:
        print("\nYou Have Selected Converting Grams To Kilograms.")
        grams = input("\nHow Many Grams: ")
        result = float(grams) /1000
        print(f"\nYou Converted {grams} Grams To {result} Kilograms.")
    except:
        no()

def wmg():
    try:
        print("\nYou Have Selected Converting Milligrams To Grams.")
        milligrams = input("\nHow Many Milligrams: ")
        result = float(milligrams) /1000
        print(f"\nYou Converted {milligrams} Milligrams To {result} Grams.")
    except:
        no()

def wmk():
    try:
        print("\nYou Have Selected Converting Milligrams To Kilograms.")
        milligrams = input("\nHow Many Milligrams: ")
        result = float(milligrams) /1000000
        print(f"\nYou Converted {milligrams} Milligrams To {result} Kilograms.")
    except:
        no()

def wpo():
    try:
        print("\nYou Have Selected Converting Lbs To Oz.")
        pounds = input("\nHow Many Lbs: ")
        result = float(pounds) * 16
        print(f"\nYou Converted {pounds} Lbs To {result} Oz.")
    except:
        no()

def wpt():
    try:
        print("\nYou Have Selected Converting Lbs To Tons.")
        pounds = input("\nHow Many Lbs: ")
        result = float(pounds) / 2000
        print(f"\nYou Converted {pounds} Lbs To {result} Tons.")
    except:
        no()

def wot():
    try:
        print("\nYou Have Selected Converting Oz To Tons.")
        oz = input("\nHow Many Oz: ")
        result = float(oz) / 32000
        print(f"\nYou Converted {oz} Oz To {result} Tons.")
    except:
        no()

def wop():
    try:
        print("\nYou Have Selected Converting Oz To Lbs.")
        oz = input("\nHow Many Oz: ")
        result = float(oz) /16
        print(f"\nYou Converted {oz} Oz To {result} Lbs.")
    except:
        no()

def wtp():
    try:
        print("\nYou Have Selected Converting Tons To Lbs.")
        tons = input("\nHow Many Tons: ")
        result = float(tons) * 2000
        print(f"\nYou Converted {tons} Tons To {result} Lbs.")
    except:
        no()

def wto():
    try:
        print("\nYou Have Selected Converting Tons To Oz.")
        tons = input("\nHow Many Tons: ")
        result = float(tons) * 32000
        print(f"\nYou Converted {tons} Tons To {result} Oz.")
    except:
        no()

def wlc():
    try:
        print("\nYou Have Selected Converting Liters To Cubic Centimeters.")
        liters = input("\nHow Many Liters: ")
        result = float(liters) * 1000
        print(f"\nYou Converted {liters} Liters To {result} Cubic Centimeters.")
    except:
        no()

def wcl():
    try:
        print("\nYou Have Selected Converting Cubic Centimeters To Liters.")
        cubic = input("\nHow Many Cubic Centimeters: ")
        result = float(cubic) / 1000
        print(f"\nYou Converted {cubic} Cubic Centimeters To {result} Liters.")
    except:
        no()

def wfc():
    try:
        print("\nYou Have Selected Converting Fluid Oz To Cups.")
        fluidoz = input("\nHow Many Fluid Oz: ")
        result = float(fluidoz) / 8
        print(f"\nYou Converted {fluidoz} Fluid Oz To {result} Cups.")
    except:
        no()

def wfp():
    try:
        print("\nYou Have Selected Converting Fluid Oz To Pints.")
        fluidoz = input("\nHow Many Fluid Oz: ")
        result = float(fluidoz) / 16
        print(f"\nYou Converted {fluidoz} Fluid Oz To {result} Pints.")
    except:
        no()

def wfq():
    try:
        print("\nYou Have Selected Converting Fluid Oz To Quarts.")
        fluidoz = input("\nHow Many Fluid Oz: ")
        result = float(fluidoz) / 32
        print(f"\nYou Converted {fluidoz} Fluid Oz To {result} Quarts.")
    except:
        no()

def wfg():
    try:
        print("\nYou Have Selected Converting Fluid Oz To Gallons.")
        fluidoz = input("\nHow Many Fluid Oz: ")
        result = float(fluidoz) / 128
        print(f"\nYou Converted {fluidoz} Fluid Oz To {result} Gallons.")
    except:
        no()

def wcf():
    try:
        print("\nYou Have Selected Converting Cups To Fluid Oz.")
        cups = input("\nHow Many Cups: ")
        result = float(cups) * 8
        print(f"\nYou Converted {cups} Cups To {result} Fluid Oz.")
    except:
        no()

def wcp():
    try:
        print("\nYou Have Selected Converting Cups To Pints.")
        cups = input("\nHow Many Cups: ")
        result = float(cups) / 2
        print(f"\nYou Converted {cups} Cups To {result} Pints.")
    except:
        no()

def wcq():
    try:
        print("\nYou Have Selected Converting Cups To Quarts.")
        cups = input("\nHow Many Cups: ")
        result = float(cups) / 4
        print(f"\nYou Converted {cups} Cups To {result} Quarts.")
    except:
        no()

def wcg():
    try:
        print("\nYou Have Selected Converting Cups To Gallons.")
        cups = input("\nHow Many Cups: ")
        result = float(cups) / 16
        print(f"\nYou Converted {cups} Cups To {result} Gallons.")
    except:
        no()

def wpf():
    try:
        print("\nYou Have Selected Converting Pints To Fluid Oz.")
        pints = input("\nHow Many Pints: ")
        result = float(pints) * 16
        print(f"\nYou Converted {pints} Pints To {result} Fluid Oz.")
    except:
        no()

def wpc():
    try:
        print("\nYou Have Selected Converting Pints To Cups.")
        pints = input("\nHow Many Pints: ")
        result = float(pints) * 2
        print(f"\nYou Converted {pints} Pints To {result} Cups.")
    except:
        no()

def wpq():
    try:
        print("\nYou Have Selected Converting Pints To Quarts.")
        pints = input("\nHow Many Pints: ")
        result = float(pints) / 2
        print(f"\nYou Converted {pints} Pints To {result} Quarts.")
    except:
        no()

def wpg():
    try:
        print("\nYou Have Selected Converting Pints To Gallons.")
        pints = input("\nHow Many Pints: ")
        result = float(pints) / 8
        print(f"\nYou Converted {pints} Pints To {result} Gallons.")
    except:
        no()

def wqf():
    try:
        print("\nYou Have Selected Converting Quarts To Fluid Oz.")
        quarts = input("\nHow Many Quarts: ")
        result = float(quarts) * 32
        print(f"\nYou Converted {quarts} Quarts To {result} Fluid Oz.")
    except:
        no()

def wqc():
    try:
        print("\nYou Have Selected Converting Quarts To Cups.")
        quarts = input("\nHow Many Quarts: ")
        result = float(quarts) * 4
        print(f"\nYou Converted {quarts} Quarts To {result} Cups.")
    except:
        no()

def wqp():
    try:
        print("\nYou Have Selected Converting Quarts To Pints.")
        quarts = input("\nHow Many Quarts: ")
        result = float(quarts) * 2
        print(f"\nYou Converted {quarts} Quarts To {result} Pints.")
    except:
        no()

def wqg():
    try:
        print("\nYou Have Selected Converting Quarts To Gallons.")
        quarts = input("\nHow Many Quarts: ")
        result = float(quarts) / 4
        print(f"\nYou Converted {quarts} Quarts To {result} Gallons.")
    except:
        no()

def wgf():
    try:
        print("\nYou Have Selected Converting Gallons To Fluid Oz.")
        gallons = input("\nHow Many Gallons: ")
        result = float(gallons) * 128
        print(f"\nYou Converted {gallons} Gallons To {result} Fluid Oz.")
    except:
        no()

def wgc():
    try:
        print("\nYou Have Selected Converting Gallons To Cups.")
        gallons = input("\nHow Many Gallons: ")
        result = float(gallons) * 16
        print(f"\nYou Converted {gallons} Gallons To {result} Cups.")
    except:
        no()

def wgp():
    try:
        print("\nYou Have Selected Converting Gallons To Pints.")
        gallons = input("\nHow Many Gallons: ")
        result = float(gallons) * 8
        print(f"\nYou Converted {gallons} Gallons To {result} Pints.")
    except:
        no()

def wgq():
    try:
        print("\nYou Have Selected Converting Gallons To Quarts.")
        gallons = input("\nHow Many Gallons: ")
        result = float(gallons) * 4
        print(f"\nYou Converted {gallons} Gallons To {result} Quarts.")
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

weightconv = {
    1: 'Grams to Milligrams',
    2: 'Grams to Kilograms',
    3: 'Milligrams to Grams',
    4: 'Milligrams to Kilograms',
    5: 'Pounds to Ounces',
    6: 'Ounces to Pounds',
    7: 'Pounds to Tons',
    8: 'Ounces to Tons',
    9: 'Tons to Pounds',
    10: 'Tons to Ounces',
    11: 'Liters to Cubic Centimeters',
    12: 'Cubic Centimeters to Liters',
    13: 'Fluid Oz to Cups',
    14: 'Fluid Oz to Pints',
    15: 'Fluid Oz to Quarts',
    16: 'Fluid Oz to Gallons',
    17: 'Cups to Fluid Oz',
    18: 'Cups to Pints',
    19: 'Cups to Quarts',
    20: 'Cups to Gallons',
    21: 'Pints to Fluid Oz',
    22: 'Pints to Cups',
    23: 'Pints to Quarts',
    24: 'Pints to Gallons',
    25: 'Quarts to Fluid Oz',
    26: 'Quarts to Cups',
    27: 'Quarts to Pints',
    28: 'Quarts to Gallons',
    29: 'Gallons to Fluid Oz',
    30: 'Gallons to Cups',
    31: 'Gallons to Pints',
    32: 'Gallons to Quarts',
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

    elif sel == "4":

        hello()

        for key4, value4 in weightconv.items():
            print(f"Your choices are {key4}: {value4}.\n")
        choice4 = input("Please select a number: ")
        choice4 = int(choice4)
        if choice4 == 1:
            wgm()
        elif choice4 == 2:
            wgk()
        elif choice4 == 3:
            wmg()
        elif choice4 == 4:
            wmk()
        elif choice4 == 5:
            wpo()
        elif choice4 == 6:
            wop()
        elif choice4 == 7:
            wpt()
        elif choice4 == 8:
            wot()
        elif choice4 == 9:
            wtp()
        elif choice4 == 10:
            wto()
        elif choice4 == 11:
            wlc()
        elif choice4 == 12:
            wcl()
        elif choice4 == 13:
            wfc()
        elif choice4 == 14:
            wfp()
        elif choice4 == 15:
            wfq()
        elif choice4 == 16:
            wfg()
        elif choice4 == 17:
            wcf()
        elif choice4 == 18:
            wcp()
        elif choice4 == 19:
            wcq()
        elif choice4 == 20:
            wcg()
        elif choice4 == 21:
            wpf()
        elif choice4 == 22:
            wpc()
        elif choice4 == 23:
            wpq()
        elif choice4 == 24:
            wpg()
        elif choice4 == 25:
            wqf()
        elif choice4 == 26:
            wqc()
        elif choice4 == 27:
            wqp()
        elif choice4 == 28:
            wqg()
        elif choice4 == 29:
            wgf()
        elif choice4 == 30:
            wgc()
        elif choice4 == 31:
            wgp()
        elif choice4 == 32:
            wgq()
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