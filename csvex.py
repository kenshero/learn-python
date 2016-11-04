import csv

ifile  = open('Location Tree DBFIXED_test.csv', "r")
read = csv.reader(ifile)

with open('Location Tree DBFIXED_test_edit.csv', 'w') as testfile:
    csv_writer = csv.writer(testfile)
    for row in read :
        if row[0] == "158" or row[0] == "239" or row[0] == "101" or row[0] == "216":
            print(row)
            csv_writer.writerow(row)
