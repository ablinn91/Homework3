import os
import csv
#import in the data
budget_data = os.path.join("budget_data.csv")

#Assign needed variables
number_month = 0
total_profit_loss = 0
delta_profit =0
y=0
delta_profit_total =0
greatest_gain=0
greatest_loss=0
z=0
total_delta_profit = 0


with open(budget_data, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    reader =csv.reader(csv_file)
    header = next(reader)
    
    #cretate our loop to go through each row

    for row in reader:
    
        x = int((row[1]))
        #Finds the total profit for the problem
        total_profit_loss = x + total_profit_loss
        #finds total number of months by just ading up all the rows 
        number_month = number_month + 1
        delta_profit = x - y
        #gets rid of the first delta_profit becouse that would just be the first value
        if z==0:
            delta_profit = delta_profit - delta_profit
            z = z+1
        total_delta_profit = delta_profit_total + delta_profit 

        #finds greatest gain and a signs
        if delta_profit > greatest_gain:
            greatest_gain = delta_profit
            greatest_gain_month = row[0]
        #finds greatest loss and signs
        if delta_profit < greatest_loss:
            greatest_loss = delta_profit
            greatest_loss_month = row[0]    
        
        delta_profit_total = delta_profit + delta_profit_total

        #set y to the curent row, which will be the last row in the next integration
        y = x

#print out the data in the analysis.         
print("Financial Analysis")  
print("------------------------------")
print(f"Total Months: {str(number_month)}")
print("Total: $"+str(total_profit_loss))
print("Average Change: $" + str(round(total_delta_profit/(number_month-1),2)))
print("Greatest Increase in Profits: " + greatest_gain_month +" ($" + str(greatest_gain) +")")
print("Greatest Decrease in Profits: " + greatest_loss_month +" ($" + str(greatest_loss) +")")

bank_data_output = os.path.join("Bank_Data_Results.csv")


#export out the data in a spead sheet 
with open(bank_data_output, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Total Months:",number_month])
    writer.writerow(["Total Earnings",total_profit_loss])
    writer.writerow(["Average Change",round(total_delta_profit/(number_month-1),2)])
    writer.writerow(["Greatest Increase in Profits",greatest_gain_month,greatest_gain])
    writer.writerow(["Greatest Decrease in Profits",greatest_loss_month,greatest_loss])

    

    

