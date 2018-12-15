# Import os mudule and module for reading CSV files 
import os
import csv

# Import the Pandas library
import pandas as pd

# Path to collect data from the Resources folder, read csv and convert dates
pro_loss_df = pd.read_csv('C:\\Users\\maaik\\USCLOS201811DATA3\\03_python\\homework\\Instructions\\PyBank\\Resources\\budget_data.csv',parse_dates=['Date'])

# total number of months in dataset
months = pro_loss_df['Date'].count()

# create new column with difference in profit/losses compared to previous month
pro_loss_df['difference'] = pro_loss_df ['Profit/Losses'] - pro_loss_df['Profit/Losses'].shift(1)

# define average change, greatest increase and greatest decrease
average = pro_loss_df['difference'].mean()
maximum = pro_loss_df['difference'].max()
minimum = pro_loss_df['difference'].min()

# Total net amount of profit/losses
Total = str(pro_loss_df['Profit/Losses'].sum(axis=0))

# corresponding month for greatest increase and decrease in correct format
Increase_month = pro_loss_df.iloc[pro_loss_df['difference'].idxmax(),0].strftime('%b-%Y')
Decrease_month = pro_loss_df.iloc[pro_loss_df['difference'].idxmin(),0].strftime('%b-%Y')

# results, every record on new line, rounded 2 decimals for average and 0 decimals for max in min
results = ("Financial_Analysis \n"
+ "-------------------------------\n"
+ "Total Months:" + str(months) + "\n"
+ "Total: $ " + Total + "\n"
+ "Average Change: $ " + "%.2f" %average +"\n"
+ "Greatest Increase in Profits: " + Increase_month + " ($ %.0f" %maximum + ")\n"
+ "Greatest Decrease in Profits: " + Decrease_month + " ($ %.0f" %minimum + ")")

# print results
print(results)

# export results to text file and close file
text_file = open ("Financial_Analysis_PyBank.txt", "w")
text_file.write(results)
text_file.close()
