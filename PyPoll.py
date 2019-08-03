import os
import csv
#import Data
election_data = os.path.join("election_data.csv")
total_votes=0
# our counters for each canidate
x1 = 0
x2 = 0
x3 = 0
x4 = 0
with open(election_data, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    reader =csv.reader(csv_file)
    header = next(reader)

    #this finds our names for our canidates s1 = canidate 1
    for row in reader:
        total_votes = total_votes + 1
        #namming function1
        if row[2] != "" and x1 ==0:
            s1 = str(row[2])
            x1 = x1 +1
        #Finds total for 1st canidate 
        elif row[2] == s1:
            x1 = x1 + 1  
        #naming function2 
        elif row[2] != s1 and x2 == 0:
            s2 = str(row[2])
            x2 = x2 +1
        #Finds total for 2st canidate     
        elif row[2] == s2:
            x2 = x2 +1 
        #naming function3
        elif row[2] != s2 and x3==0:
            s3 = str(row[2])
            x3 = x3 +1
        #Finds total for 3rd canidate     
        elif row[2] ==s3:
            x3 = x3 +1   
        #naming function4
        elif row[2] != s2 and x4==0:
            s4 = str(row[2])
            x4 = x4 +1
        #Finds total for 4th canidate      
        elif row[2] == s4:
            x4 = x4 +1           

canidates = (s1,s2,s3,s4)
results = (x1,x2,x3,x4)
t=0
# Finds the winner for the results
for i in range(0,3):
    #gets the first person out
    if results[i]>0 and t==0:
        winner_name=canidates[i]
        winner_value = results[i]
        t=t+1
    #see each new iteration is greater than the first    
    elif results[i]>winner_value:
        winner_name=canidates[i]
        winner_value = results[i]
#print everyThing out. 
print("Election Results")
print("------------------------")
print("Total Votes: "+str(total_votes))
print("------------------------")
print(s1+": "+str(round(x1/total_votes*100)) + "% (" + str(x1)+")")
print(s2+": "+str(round(x2/total_votes*100)) + "% (" + str(x2)+")")
print(s3+": "+str(round(x3/total_votes*100)) + "% (" + str(x3)+")")
print(s4+": "+str(round(x4/total_votes*100)) + "% (" + str(x4)+")")
print("------------------------")
print("Winner: " + winner_name)
print("------------------------")


election_data_output = os.path.join("Election_Data_Results.csv")

#create a file around the data 
with open(election_data_output, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["total Votes:",total_votes])
    writer.writerow(["Candidate", "% of votes"," Votes"])
    writer.writerow([s1, x1/total_votes*100,x1])
    writer.writerow([s2, x2/total_votes*100,x2])
    writer.writerow([s3, x2/total_votes*100,x3])
    writer.writerow([s4, x4/total_votes*100,x4])
    writer.writerow(["Winner :", winner_name])