#             ___|  _ \  |     ____|  ___| ____|  \  |  |   |__ __| |   |
#            |     |   | |     __|   |     __|   |\/ |  |   |   |   |   |
#            |     |   | |     |     |   | |     |   |  |   |   |   ___ |
#           \____|\___/ _____|_____|\____|_____|_|  _| \___/   _|  _|  _|
#
# Date:         5/8/21
# Program Name: dayOfTheWeek.py
# Author:       Cole Wohlgemuth (colewohlge73@gmail.com)
#
###############################################################################
#
# Description: This program will ask for a month, a day, and a year
# in the form mm/dd/yyyy. It will then print the day of the week that this
# particular day falls on. It will do these steps until the user wants to stop

import os

def Instructions():
    """ Prints the title of the program and the instructions for the user
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print('             ___|  _ \  |     ____|  ___| ____|  \  |  |   |__ __| |   |')
    print('            |     |   | |     __|   |     __|   |\/ |  |   |   |   |   |')
    print('            |     |   | |     |     |   | |     |   |  |   |   |   ___ |')
    print('           \____|\___/ _____|_____|\____|_____|_|  _| \___/   _|  _|  _|')
    print()
    print('Program Name: Day of the Week')
    print('This program will accept a date in the form mm/dd/yyyy.')
    print('It will then calculate the day of the week that this particular')
    print('date falls on. Finally it will then display the result for you to see.')
    print()


def Get_Date():
    """ This function first asks the user if it wants to search for a date
    If the answer is yes then it asks for the date, but if no then it exits the function

    answer  - variable for if the user wants to continue
    date    - variable that hold the date the user enters
    The rest of the variables are obvious 
    """

    month = 1
    day = 1
    year = 1700
    answer = input('Would you like to search for a date? (y/n) ')
    
    if answer == 'y':
        date = input('What is the date you would like to search (ie: 01/23/2093)? \n')
    else:
        return answer, month, day, year

    month, day, year = date.split('/')
    month = int(month)
    day = int(day)
    year = int(year)
    
    return answer, month, day, year


def Months(month):
    """ This function get the month adjustment for the particual month that
    was entered by the user

    mon_adjust  - Holds the value of the adjustment
    """

    if (month == 1):
        mon_adjust = 1
    elif (month == 2):
        mon_adjust = 4
    elif (month == 3):
        mon_adjust = 4
    elif (month == 4):
        mon_adjust = 0
    elif (month == 5):
        mon_adjust = 2
    elif (month == 6):
        mon_adjust = 5
    elif (month == 7):
        mon_adjust = 0
    elif (month == 8):
        mon_adjust = 3
    elif (month == 9):
        mon_adjust = 6
    elif (month == 10):
        mon_adjust = 1
    elif (month == 11):
        mon_adjust = 4
    elif (month == 12):
        mon_adjust = 6
    else:
        print('NOT A VALID MONTH')
        mon_adjust = 0
    return mon_adjust


def Century(year):
    """ This function gives you the adjustment of the century"""

    century = year // 100
    if (century == 17):
        value = 4
    elif (century == 18):
        value = 2
    elif (century == 19):
        value = 0
    elif (century == 20):
        value = 6
    elif (century == 21):
        value = 4
    else:
        print('UNABLE TO CALCULATE THIS DATE YET')
        value = 0
    return value


def Leap_Year(month, year):
    """This function gives you the adjustment if it happens to be a leap year
    """

    adjust = 0
    if (month == 1 or month == 2):
        if (year % 400 == 0):
            adjust = 1
        elif (year % 4 == 0 and year % 100 != 0):
            adjust = 1
    return adjust


def Final_Calculation(month, day, year, mon_adjust, leap_adjust, cent_adjust):
    """ This function completes the finaly calculation of the day of the week
    """
    
    result = (year % 100) // 12
    result = ((year % 100) % 12) + result + (((year % 100) % 12) // 4)
    result = result % 7
    result = result + mon_adjust
    result = (result % 7) + day
    result = (result % 7) + cent_adjust
    result = result - leap_adjust
    result = result % 7
    if (result == 1 or result == -6):
        print('Sunday')
    elif (result == 2 or result == -5):
        print('Monday')
    elif (result == 3 or result == -4):
        print('Tuesday')
    elif (result == 4 or result == -3):
        print('Wednesday')
    elif (result == 5 or result == -2):
        print('Thursday')
    elif (result == 6 or result == -1):
        print('Friday')
    elif (result == 0 or result == -7):
        print('Saturday')
    else:
        print('invalid date')
    print()


def Main():
    Instructions()
    answer = 'y'
    while answer == 'y':
        answer, month, day, year = Get_Date()
        if answer == 'y' or 'Y':
            mon_adjust = Months(month)
            leap_adjust = Leap_Year(month, year)
            cent_adjust = Century(year)
            Final_Calculation(month, day, year, mon_adjust, leap_adjust, cent_adjust)
        elif answer == 'n' or 'N':
            print('Thanks for playing!\n')    
        else:
            print('THAT IS AN UNEXCEPTABLE ANSWER')


if __name__ == "__main__":
    Main()