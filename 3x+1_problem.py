"""
Joseph Whiteaker
November 14th, 2019


SUMMARY

This Python script is validating 6000 numbers for the Collatz Conjecture which states that for any number N,
if you follow the procedures of: if N is even: N/2 or if N is odd: 3N +1, then make that new number the value N and repeat this
same process until you reach 1. If the conjecture is true for digits from 1 to 6000 then the code should work just fine.
In summary, this piece of code is testing to see if the expected outcome of the Collatz Conjecture holds from up from 1 to 6000.



INSTRUCTIONS

Just run the following statement 'python 3x+1_problem.py' in your operating software's commandline application, whether in be
in Apple's Terminal or in Window's Windows Terminal. Or you could run it on a Jupyter Notebook but I am too worried about the
data being too much for Jupyter. Once you have ran the command in your terminal, run the command 'open Collatz.xls' in the
appropriate directry if you have a Mac. If you have a windows, simply type 'Collatz.xls' the appropriate directory and it
should open up the Excel sheet. If you are having issues with any of these methods, just navigate to the file manually through
Apple's Finder app or the Window's File Explorer app.



"""


# Imports
########################################

# Writes Into Excel Sheets
import xlwt

# Reads From Excel Sheets
import xlrd

# Reads and Writes In and From Excel Sheets In A List Format
import pandas as pd

# Plots The Data
import matplotlib.pyplot as plt

# Formats The Data Plotted
from matplotlib import style

# Additional Array Functions
import numpy as np

########################################


# The Number of Numbers Being Tested
BiggestNumber = 6000



# File Name Format
name_of_file = 'N = '
type_of_file = '.png'


# Finds The Value Below The Given Number In The Tree
def down_the_tree(number):

    if number %2 == 0: number /= 2

    else: number = (number*3) + 1

    return number



# Make Excel sheet
wb = xlwt.Workbook()


# Title Excel Sheet
ws = wb.add_sheet("Test Sheet")


# Column 1 Title
ws.write(0,0 , 'Numbers')


# Make Column 1 Row Numbers
for i in range(1,BiggestNumber):
    ws.write(i , 0 , i)


# Saves the Excel Sheet
wb.save('Collatz.xls')


# Reads The New Excel Sheet
excel_file = 'Collatz.xls'
numbers = pd.read_excel(excel_file)
column = numbers['Numbers']


# Find Collatz Number for each row
for i in range(1,BiggestNumber):

    # Create Axis For Plots
    x_axis = []
    y_axis = []

    # The Starting Number
    testing_number = int(column[i-1])


    # Counters Needed For Cell Placement In Excel Sheet
    TimesDone = 0
    ReturnValue = testing_number

    # While The Number Isn't 1
    while ReturnValue != 1:

        # Assign It's New Value Based On Whether It's Even Or Odd
        testing_number = down_the_tree(testing_number)


        # Assigning Return Value To Possibly End Loop
        ReturnValue = testing_number

        # Column Number Counter
        TimesDone+=1

        # Write Into Excel Sheet
        row = i
        col = TimesDone
        FinalNumber = testing_number
        ws.write(row , col , FinalNumber)

        # Append Axis
        x_axis.append(col)
        y_axis.append(FinalNumber)



    # Plot X And Y Axis
    plt.plot(x_axis,y_axis,'r--')

    # Save The Plot As A PNG File
    final_file = name_of_file + str(i) + type_of_file
    plt.savefig(final_file)

    # Clear Figures Of Graph
    plt.clf()

    # Clear Axis Of Graph
    plt.cla()



# Save the Excel Sheet
wb.save('Collatz.xls')
