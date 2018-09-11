import pandas as pd
# import csv

# read from file
df = pd.DataFrame.from_csv("./la-county-restaurant-inspections.csv")

# question 1
print("The average/mean score of the LA County Resturants Inspections is"+str(df['score'].mean()))

# question 2
count = 0
for index,row in df.iterrows():
    if row['facility_address'] == '17660 CHATSWORTH ST':
        count = count+1
print("17660 CHATSWORTH ST visited" + " " + str(count)+" times.")

# question 3
count1 = 0
for index,row in df.iterrows():
    if row['facility_city'] == 'LANCASTER':
        count1 = count1+1
print("LANCASTER visited" + " " + str(count1)+" times.")

# question 4
countall = 0
countem = 0
for index, row in df.iterrows():
    countall = countall + 1
    if row['employee_id'] == 'EE0000145':
        countem = countem + 1
print("Employee EE0000145 visited" + " " + str((countem/countall)*100) + "% times.")

# question 5
ountall = 0
countf = 0
for index, row in df.iterrows():
    countall = countall + 1
    if row['facility_id'] == 'FA0013858':
        countf = countf +1
print("Facility FA0013858 was visited" + " " + str((countf/countall)*100) + "% times.")

# question 6
countem = 0
countemf = 0
for index, row in df.iterrows():
    if row['employee_id'] == 'EE0000593':
        countem = countem +1
        if row['facility_city']== 'GRANADA HILLS':
            countemf = countemf + 1
print("Employee EE0000593 visited GRANADA HILLS " + str((countemf/countem)*100) + "% times.")
