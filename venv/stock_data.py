#imported the libraries for the task
import csv
import os

#Created a loop to open the folder with the files
for file in os.listdir('csv files for edit'):
    line_count = 0
    data = []
    #An IF statement, to check only files that have a file format of .csv
    if file.endswith('.csv'):
        filepath='csv files for edit/' + file
        with open(filepath, 'r') as csvreader:
            reader = csv.reader(csvreader)
            #For each row, we perform the following calculations with a loop
            for row in reader:
                if line_count == 0:
                    line_count += 1
                    row.append('Percentage change between Close and Open price')
                    data.append(row)
                    continue
                #The following formula is used to calculate "Change = (Close-Open)/Open x 100" or based on Google "(New Price - Old Price) / Old Price x 100"
                change = (float(row[4]) - float(row[1])) / float(row[1]) * 100
                row.append(change)
                data.append(row)
        #And afterwards, write the following calculation into the file.
        with open(filepath, 'w') as csvwriter:
            writer = csv.writer(csvwriter)
            for row in data:
                writer.writerow(row)