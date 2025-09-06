my_grades = [20,19,14,17,13,10,12,13]
summation = 0
passed = []
not_passed = []

my_grades.sort(reverse=True)
moadel = summation / len (my_grades)

for s in my_grades :
    if s < 12 :
        summation += s
        passed.append(s)
    else :
        not_passed.append(s)
        print(f"moadel : {moadel}")
        print(f"ghaboli : {passed}")
        print(f"rad shodeh : {not_passed}")
