"""
Python 1 - DAT-119 - Spring 2019
Joe Holleran
05/08/2019
Python 1 - FINAL PROJECT
"""
# Data sources
# http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
# Student created spreadsheet and files uploaded to GitHub
# Data was not manipulated in anyway.  Only organized in order to compute
# statistics in easier formatting and concatenate to move into txt files

# Sources for project code
# Matplot lib
# Textbook Chapter 7
# https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/
# CSV module
# https://pythonprogramming.net/reading-csv-files-python-3/
# Statistics module
# https://docs.python.org/3/library/statistics.html
# Math module
# https://docs.python.org/3/library/math.html

# Import matplot lib, csv, statistics, math
import matplotlib.pyplot as plt
import csv
import statistics as stat
import math

# Welcome user to the project
print("Welcome to Joe Holleran's Python 1 Final Project!")
print("-------------------------------------------------")

# Define main function
def main():
    
    # Start Main Menu loop
    while True:
        
        # Give user option to view each section of the project
        print("*** Main Menu ***")
        print()
        print("1.) Project Description")
        print("2.) S&P 500 Price from 1928 to 2018")
        print("3.) $100 Investment in S&P 500 Compounded from 1928 to 2018")
        print("4.) S&P 500 Distribution of Returns from 1928 to 2018")
        print("5.) Analysis of S&P 500 Returns from 1928 to 2018")
        print("6.) Project Conclusion")
        print("7.) EXIT")
        print()
    
        user_select = int(input("Please choose one of the options above: "))
        print()
        
        # Call functions if user selects from menu; ask again if user selects
        # option outside 1-7
        if user_select < 1 or user_select > 7:
            user_select = int(input("Please choose one of the options above: "))
        elif user_select == 1:
            description()
        elif user_select == 2:
            entire_period_price()
        elif user_select == 3:
            entire_period_100()
        elif user_select == 4:
            entire_period_return()
        elif user_select == 5:
            analysis()
        elif user_select == 6:
            conclusion()
        else:
            print("Thanks for viewing my project!")   
            print("------------EXIT--------------")
            break
         
        # Go back to main function after viewing section by pressing enter
        go_to_main = input("Press enter to continue... ")
        print()
        if go_to_main == " ":
            main()   

# Define project description function
def description():
    
    # Display project title, description of project, equations used in project
    # as well as definition of the S&P 500
    print("An Analysis of S&P 500 Annual Returns from 1928 to 2018")
    print("-------------------------------------------------------")
    print("")
    print("The purpose of this project is to display S&P 500 annual returns from"
          " 1928 to 2018, as well as analyze the difference in the mean annual"
          " return compared to the Compound Annual Growth Rate of the S&P 500.")
    print("")
    print("Equations used in this project:")
    print("")
    print("Mean Annual Return = (Sum of Returns for n Years) / (n Years)")
    print("")
    print("Compound Annual Growth Rate = (((Ending Value)/(Beginning Value))^1/n years) - 1")
    print("")
    print("Estimated Compound Annual Growth Rate: "
          " (1 + mean annual return)^2 - (Standard Deviation)^2 = (1 + CAGR)^2)")
    print("")
    print("*S&P 500: U.S. Stock Market index based on the market capitalization "
          "nof 500 companies listed on the NYSE, NASDAQ, CBOE.")
    
def entire_period_price():
    
    # Use file 1928_2018_price.txt
    
    # Create lists from 1928_2018_price file
    year = []
    price = []
    
    # Open file and loop through the file at each "," to add to lists
    with open("1928_2018_price.csv", "r") as csvfile:
        file = csv.reader(csvfile, delimiter=",")
        for item in file:
            year.append(float(item[0]))
            price.append(float(item[1]))
    
    # Use matplotlib to plot a line graph of the S&P 500 price 1928-2018
    plt.plot(year,price, label="S&P 500", color = "blue")
    plt.xlabel("Year")
    plt.ylabel("S&P 500 Price")
    plt.title("S&P 500 from 1928 to 2018")
    plt.xticks(range(1928, 2019, 10))
    plt.legend()
    plt.show()
    
    # Display year end prices, rate of growth over time period, mean annual return
    # Standard deviation, and stdev definition
    print("")
    print("S&P 500 Year-End Price 1927: $17.66")
    print("S&P 500 Year-End Price 2018: $2,506.85")
    print("The S&P 500 gained 14,095% over the time period 1928-2018.")
    print("")
    print("The mean annual return for the S&P 500 from 1928-2018"
          " is: 11.36%")
    print("The standard deviation for the S&P 500 from 1928-2018"
          " is: 19.47%")
    print("")
    print("* Standard devation of investment returns is used to measure volatility,"
          " i.e. risk")
       
    # NO statistics in this function, please see analysis function

def entire_period_100():
    
    # Use file 1928_2018_100.txt
    
    # Create lists for 1928_2018_100 file
    year = []
    value = []

    # Open file and loop through each row at "," and add to lists
    with open("1928_2018_100.csv", "r") as csvfile:
        file = csv.reader(csvfile, delimiter=",")
        for item in file:
            year.append(float(item[0]))
            value.append(float(item[1]))
    
    # Use matplotlib to plot a line graph to display the growth of a $100
    # investment in the S&P 500 from 1928 to 2018
    plt.plot(year,value, label="$100 Initial Investment", color = "blue")
    plt.xlabel("Year")
    plt.ylabel("$ Dollars")
    plt.title("$100 Invested in S&P 500 compounded 1928 to 2018")
    plt.xticks(range(1928, 2019, 10))
    plt.legend()
    plt.show()
    
    # Display the beginning and ending values, CAGR, and CAGR definition
    print("")
    print("An initial investment of $100 invested in the S&P 500 beginning of year"
          " 1928 would have grown to $382,850 by end of year 2018.")
    print("")
    print("The Compound Annual Growth Rate of the S&P 500 from 1928-2018 is 9.49%")
    print("")
    print("The Compound Annual Growth Rate is defined as the growth rate of an"
          " initial investment to the ending investment value.")

     # NO statistics in this function

def entire_period_return():
    
    # Use file 1928_2018_returns.txt

    
    # Create lists for 1928_2018_returns file
    year = []
    sp500 = []
    threemonth = []
    tenyear = []

    # Open file and loop through each row at "," to add to lists in order
    # to plot a histograph
    with open("1928_2018_returns.csv", "r") as csvfile:
        file = csv.reader(csvfile, delimiter=",")
        for item in file:
            year.append(float(item[0]))
            sp500.append(float(item[1]))
            threemonth.append(float(item[2]))
            tenyear.append(float(item[3]))
            
    # Use matplotlib to plot a histogram using the above lists
    plt.hist(sp500, bins = 10, color = "blue", edgecolor = 'k')
    plt.title("S&P 500 Year-End Returns: 1928-2018")
    plt.xlabel("% Return")
    plt.ylabel("Number of Years")
    plt.yticks(range(0, 20, 2))
    plt.xticks(range(-45, 55, 5))
    plt.show()
    
    # Display the mean annual return, min/max return years, and various
    # other analysis of the histogram
    print("")
    print("The mean annual return of the S&P 500 (1928-2018) is 11.36%")
    print("The max annual returns of the S&P 500 (1928-2018) in one-year are:"
          " 52.56% (1954), 49.98% (1933), 46.74% (1935)")
    print("The min annual returns of the S&P 500 (1928-2018) in one-year are:"
          " -43.84% (1931), -36.55% (2008), -35.33% (1937)")
    print("")
    print("The S&P 500 had a positive return in 73% of years 1928-2018.")
    print("The S&P 500 had a negative return in 27% of years 1928-2018.")
    print("")
    print("The S&P 500 returned above the mean annual return in 54% of years"
          " from 1928-2018.")
    print("The S&P 500 return below the mean annual return in 46% of years"
          " from 1928-2018.")

def analysis():
    
    # Create lists for the 1928_2018_100 file    
    year_100 = []
    value_100 = []

    # Open file and loop through each row at "," and add to above lists
    with open("1928_2018_100.csv", "r") as csvfile:
        file = csv.reader(csvfile, delimiter=",")
        for item in file:
            year_100.append(float(item[0]))
            value_100.append(float(item[1]))
    
    # Create lists for the 1928_2018_returns file
    year = []
    sp500 = []
    threemonth = []
    tenyear = []
    
    # Open file and loop through each row at "," and add to above lists
    with open("1928_2018_returns.csv", "r") as csvfile:
        file = csv.reader(csvfile, delimiter=",")
        for item in file:
            year.append(float(item[0]))
            sp500.append(float(item[1]))
            threemonth.append(float(item[2]))
            tenyear.append(float(item[3]))
    
    # Return print the histogram from the entire_period_return function            
    plt.hist(sp500, bins = 10, color = "blue", edgecolor = 'k')
    plt.title("S&P 500 Year-End Returns: 1928-2018")
    plt.xlabel("% Return")
    plt.ylabel("Number of Years")
    plt.yticks(range(0, 20, 2))
    plt.xticks(range(-45, 55, 5))
    plt.show()
    
    # Use statistics to compute the following statistics
    # S&P 500 mean, standard deviation
    sp_mean = stat.mean(sp500)
    sp_mean = sp_mean / 100
    sp_stdev = stat.pstdev(sp500)
    sp_stdev = sp_stdev / 100
    # Display S&P mean, standard deviation
    print("The S&P 500 mean return from 1928 to 2018 was:", format(sp_mean, ".2%"))
    print("The S&P 500 standard deviation from 1928 to 2018 was:", format(sp_stdev, ".2%"))
    print()

    # 3 month treasury mean
    threemonth_mean = stat.mean(threemonth)
    threemonth_mean = threemonth_mean / 100
    print("The three-month treasury mean return from 1928 to 2018 was:", format(threemonth_mean, ".2%"))
    # S&P 500 risk premium
    risk_premium = sp_mean - threemonth_mean
    risk_premium = format(risk_premium, ".2%")
    # Display the 3-month treasury mean
    print("The S&P 500 risk premium from 1928 to 2018 was:", risk_premium)
    print("The risk premium is compensation for excess risk above 3-month T-bills.")
    print()

    # 10-year treasury bonds mean, standard deviation
    tenyear_mean = stat.mean(tenyear)
    tenyear_mean = tenyear_mean / 100
    tenyear_stdev = stat.pstdev(tenyear)
    tenyear_stdev = tenyear_stdev / 100
    # Display the mean and standard deviation of 10-year treasury bonds
    print("The mean return for 10-year bonds from 1928 to 2018 was:", format(tenyear_mean, ".2%"))
    print("The standard devation for 10-year bonds from 1928 to 2018 was:", format(tenyear_stdev, ".2%"))
    print()
    # Display the excess return of stocks over bonds for 1928-2018
    stocks_over_bonds = sp_mean - tenyear_mean
    print("The mean return of stocks over bonds from 1928 to 2018 was:", format(stocks_over_bonds, ".2%"))
    print()
 
    # Compute the S&P 500 estimated CAGR using equation in project description
    cagr_mean = sp_mean
    cagr_stdev = sp_stdev
    left_side_mean = ((1 + cagr_mean)**2)
    left_side_stdev = (cagr_stdev)**2
    result_left_side = left_side_mean - left_side_stdev
    sq_rt_left_side = math.sqrt(result_left_side)
    CAGR = sq_rt_left_side - 1
    # Display the estimated CAGR
    print("The estimated Compound Annual Growth Rate for the S&P 500 from 1928 to 2018 was:", 
          format(CAGR, ".2%"))
    print()
 
    # Compute the S&P 500 actual CAGR using equation in project description
    beg_balance = 100
    end_balance = value_100[-1]
    n = len(sp500)
    act_cagr = ((end_balance / beg_balance)**(1/n)) - 1
    # Display the actual CAGR
    print("The actual Compound Annual Growth Rate for the S&P 500 from 1928 to 2018 was:", format(act_cagr, ".2%"))
    print()

def conclusion():
    
    # Print the conclusion of the project and analysis
    print("The mean annual return of an investment does not accurately reflect"
          " the return of the investment.  The Compound Annual Growth Rate will"
          " accurately measure the return of an investment.")
    print("")
    print("Due to the volatility of the investment (Standard Deviation), the mean annual return will"
          " overstate the actual investment return (CAGR).  The estimated Compound"
          " Annual Growth Rate equation can be used to more accurately measure"
          " the return of an investment if both the mean and standard deviation"
          " are known.")
    print("")
    print("Mean annual return of S&P 500 from 1928-2018: 11.36%")
    print("Estimated Compound Annual Return of S&P 500 from 1928-2018: 9.64%")
    print("Actual Compound Annual Return of S&P 500 from 1928-2018: 9.49%")

# From Coral; make the project go
if __name__ == "__main__":
    main()
