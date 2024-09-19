#Import Modules
import serial
import csv
import matplotlib.pyplot as plt
import pandas as pd

def add_data():             #Function to add data
    ser = serial.Serial()
    ser.baudrate = 115200                   #Code to open Serial port Communication
    ser.port = "COM4"
    ser.open()

    file = open("WellbeingData.csv","a",newline="")         #Opens file to write data
    csv_file = csv.writer(file)

    
    bare_data = ser.readline().decode("utf-8").rstrip()         #Reads data
    
    
    dataList = bare_data.split(",")                     #Splits the data where the commas are
    #dataList = ["15:00",10,10]                         #Variable used for unit testing
    
    
    #Start of validation check 
    #First checks to ensure proper data type

    #This assigns each piece of data their own variable so a validation check can be done
    time_val = str(dataList[0])            
    pre_val = int(dataList[1])      
    post_val = int(dataList[2])

    time_split = time_val.split(":")          #This splits the time_val at the collon for validation
    time_num = int(time_split[0])
    
    #Nested if statements for data validation
    if isinstance(time_val, str) and isinstance(pre_val,int) and isinstance(post_val,int):
        if time_num in range(1,25):
            if pre_val in range(1,11) and post_val in range(1,11):
                csv_file.writerow(dataList) 
                #Writes data to list
    else: 
        print("ERROR,Data not valid, Rerun code")
    
    file.flush()
    ser.close()
    file.close()

run_serial = input("Do you want to add data to the file?(Y/N)")
if run_serial == "Y":
    add_data()

data = pd.read_csv("WellbeingData.csv")             #Reads data

#Graph of Post stress and Prestress including the average of each
averagePre = data["Prestress"].mean()
averagePost = data["Poststress"].mean()
plt.plot(data["Prestress"], label="Prestress")
plt.plot(data["Poststress"], label="Poststress")
plt.axhline(y=averagePre, color="r", linestyle="-", label="Average Prestress")
plt.axhline(y=averagePost, color="g", linestyle="-", label="Average Poststress")
plt.xlabel("Day")
plt.ylabel("Stress (1-10)")
plt.title("Daily Stress Data")
plt.xticks(range(0,len(data["Poststress"])))
plt.yticks(range(1,11))
plt.legend() 
plt.show()

# Convert time column to datetime type
data['Time'] = pd.to_datetime(data['Time'], format="%H:%M")

# Extract hour from the time column
data['Hour'] = data['Time'].dt.hour

# Groups data by the hour and calculates the average stress level for each hour
average_stress_by_hour = data.groupby('Hour')['Prestress'].mean()

# Plots average stress level at different times throughout the day
plt.figure(figsize=(10, 6))
plt.plot(average_stress_by_hour.index, average_stress_by_hour.values, marker='o')
plt.title('Average Stress Level by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Stress Level')
plt.xticks(range(24))
plt.yticks(range(1, 11))
plt.ylim(1, 10)
plt.grid(True)
plt.show()