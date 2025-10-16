import csv

number = input("enter your name :")

with open (rf"tamrin_25.csv","r") as f:
    reader= csv.reader(f)
    for row in reader :
        print(row)
