###############This file will contain most of the definitions

import math

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
        result = round(float(seconds) / 60,2)
        print(f"\nYou Converted {seconds} Seconds To {result} Minutes.")
    except:
        no()

def tsh():
    try:
        print("\nYou Have Selected Converting Seconds To Hours.")
        seconds = input("\nHow Many Seconds: ")
        result = round(float(seconds) / 3600,2)
        print(f"\nYou Converted {seconds} Seconds To {result} Hours.")
    except:
        no()

def tms():
    try:
        print("\nYou Have Selected Converting Minutes To Seconds.")
        minutes = input("\nHow Many Minutes: ")
        result = round(float(minutes) * 60,2)
        print(f"\nYou Converted {minutes} Minutes To {result} Seconds.")
    except:
        no()

def tmh():
    try:
        print("\nYou Have Selected Converting Minutes To Hours.")
        minutes = input("\nHow Many Minutes: ")
        result = round(float(minutes) / 60,2)
        print(f"\nYou Converted {minutes} Minutes To {result} Hours.")
    except:
        no()

def ths():
    try:
        print("\nYou Have Selected Converting Hours To Seconds.")
        hours = input("\nHow Many Hours: ")
        result = round(float(hours) * 3600,2)
        print(f"\nYou Converted {hours} Hours To {result} Seconds.")
    except:
        no()

def thm():
    try:
        print("\nYou Have Selected Converting Hours To Minutes.")
        hours = input("\nHow Many Hours: ")
        result = round(float(hours) * 60,2)
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