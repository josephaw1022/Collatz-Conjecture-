"""
Joseph Allen Whiteaker III
11/26/19

Modifying the code "3x+1_problem.py" code to shorten the number of columns in the excel sheets


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



# Finds The Value Below The Given Number In The Tree
def down_the_tree(number):

    if number %2 == 0: number /= 2

    else: number = ((number*3)+1) / 2

    return number



# Make Excel sheet
wb = xlwt.Workbook()


# Title Excel Sheet
ws = wb.add_sheet("Part 2")


# Column 1 Title
ws.write(0,0 , 'Numbers')


# Make Column 1 Row Numbers
for i in range(1,BiggestNumber):
    ws.write(i , 0 , i)


# Saves the Excel Sheet
wb.save('Collatz2.xls')


# Reads The New Excel Sheet
excel_file = 'Collatz2.xls'
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

        # Assign Its New Value Based On Whether It's Even Or Odd
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



# Save the Excel Sheet
wb.save('Collatz2.xls')
