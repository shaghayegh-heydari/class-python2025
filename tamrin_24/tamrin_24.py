import csv
import random


def creat_grades_csv (filename) :
    with open (filename,mode="w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow (["student" , "MathGrade"])
        for i in range (1, 51) :
            grade = random.randint (0, 100)
            writer.writerow ([i , grade])

        
def calculat_average_grade (filename) :
    total = 0
    count = 0
    with open (filename , mode="r") as f :
        reader=csv.DictReader (f)
        for s in reader :
            totai += int(s["mathgrade"])
            count += 1
    if count == 0 :
        return 0
    return totai / count

filename = "math_grades.csv"

creat_grades_csv(filename)

average = calculat_average_grade(filename)

print(f"Average math grade for 50 students: {average:.2f}")