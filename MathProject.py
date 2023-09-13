#The goal of this program is to be able to do math equations and conversions

import math
import Support as s

def hello():
    print(f"\nWelcome To {Select[x]}!\n")

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
################################## Note, I could try to change the longer dictionaries into smaller dictionaries in the future. Dictionary within a dictionary
Select = {
    1: 'Converting Measurements',
    2: 'Calcuating the Area',
    3: 'Converting Time',
    4: 'Converting Weight',
}

print("Thanks for using my program!")

run = 0
while run == 0:

    for x in Select.keys():
        print(f"\nYour choices are {x}: {Select[x]}")    
    sel = input("\nEnter a number: ")
    try:
        sel = int(sel)
    except:
        print("\nThat is not a valid choice!\n\nPlease run this program again!")
    if sel == 1:

        hello()

        for key1, value1 in disconv.items():
            print(f"Your choices are {key1}: {value1}.\n")
################# The C in the definitions stands for convert.
################# The letters followed by C stands for what is converted
################# EX: cmc = convert meters to centimeters and so forth
        try:
            choice1 = input("Please select a number: ")
            if choice1 == "1":
                s.cmc()
            elif choice1 == 2:
                s.ccm()
            elif choice1 == 3:
                s.cmk()
            elif choice1 == 4:
                s.ckm()
            elif choice1 == 5:
                s.cck()
            elif choice1 == 6:
                s.ckc()
            elif choice1 == 7:
                s.cif()
            elif choice1 == 8:
                s.ciy()
            elif choice1 == 9:
                s.cim()
            elif choice1 == 10:
                s.cfi()
            elif choice1 == 11:
                s.cfy()
            elif choice1 == 12:
                s.cfm()
            elif choice1 == 13:
                s.cyi()
            elif choice1 == 14:
                s.cyf()
            elif choice1 == 15:
                s.cym()
            elif choice1 == 16:
                s.cmi()
            elif choice1 == 17:
                s.cmf()
            elif choice1 == 18:
                s.cmy()
            elif choice1 == 19:
                s.cmiki()
            elif choice1 == 20:
                s.ckimi()
        except:
                print("\nNot valid.")

    elif sel == 2:
        
        hello()

        for key2, value2 in area.items():
            print(f"Your choices are {key2}: {value2}.\n")
        choice2 = input("Please select a number: ")
        try:
            choice2 = int(choice2)
            if choice2 == 1:
                s.A_R()
            elif choice2 == 2:
                s.A_P()
            elif choice2 == 3:
                s.A_Te()
            elif choice2 == 4:
                s.A_Tp()
            elif choice2 == 5:
                s.A_C()
        except:
            print("\nNot valid.")

    elif sel == 3:

        hello()

        for key3, value3 in timeconv.items():
            print(f"Your choices are {key3}: {value3}.\n")
        choice3 = input("Please select a number: ")
        try:
            choice3 = int(choice3)
            if choice3 == 1:
                s.tsm()
            elif choice3 == 2:
                s.tsh()
            elif choice3 == 3:
                s.tms()
            elif choice3 == 4:
                s.tmh()
            elif choice3 == 5:
                s.ths()
            elif choice3 == 6:
                s.thm()
        except:
            print("\nNot valid.")

    elif sel == 4:

        hello()

        for key4, value4 in weightconv.items():
            print(f"Your choices are {key4}: {value4}.\n")
        choice4 = input("Please select a number: ")
        try:
            choice4 = int(choice4)
            if choice4 == 1:
                s.wgm()
            elif choice4 == 2:
                s.wgk()
            elif choice4 == 3:
                s.wmg()
            elif choice4 == 4:
                s.wmk()
            elif choice4 == 5:
                s.wpo()
            elif choice4 == 6:
                s.wop()
            elif choice4 == 7:
                s.wpt()
            elif choice4 == 8:
                s.wot()
            elif choice4 == 9:
                s.wtp()
            elif choice4 == 10:
                s.wto()
            elif choice4 == 11:
                s.wlc()
            elif choice4 == 12:
                s.wcl()
            elif choice4 == 13:
                s.wfc()
            elif choice4 == 14:
                s.wfp()
            elif choice4 == 15:
                s.wfq()
            elif choice4 == 16:
                s.wfg()
            elif choice4 == 17:
                s.wcf()
            elif choice4 == 18:
                s.wcp()
            elif choice4 == 19:
                s.wcq()
            elif choice4 == 20:
                s.wcg()
            elif choice4 == 21:
                s.wpf()
            elif choice4 == 22:
                s.wpc()
            elif choice4 == 23:
                s.wpq()
            elif choice4 == 24:
                s.wpg()
            elif choice4 == 25:
                s.wqf()
            elif choice4 == 26:
                s.wqc()
            elif choice4 == 27:
                s.wqp()
            elif choice4 == 28:
                s.wqg()
            elif choice4 == 29:
                s.wgf()
            elif choice4 == 30:
                s.wgc()
            elif choice4 == 31:
                s.wgp()
            elif choice4 == 32:
                s.wgq()
        except:
            print("\nNot valid.")
    
    program = input("\nWould you like to run the entire program again? (Y/N) ")
    if program.lower() == "n":
        run += 1
        break
    elif program == "":
        run += 1
        break
    elif program.lower() == "y":
        run == 0

print("\nIn case I don't see you:\nGood Morning, Good Afternoon, Good Evening, and Good Night!")
print("\nFeel free to add on to this!\n")