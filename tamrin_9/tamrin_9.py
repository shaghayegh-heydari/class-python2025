students = {}

while True :
    name = input("nam dansh amoz ra vared conid : ")
    if name.lower() == "exit" :
        break

    subjects = {}
    while True :
        subject = input("nam dars ra vared conid :")
        if subject.lower() == "done" :
            break
        try :
            grade = float(input(f"nomrh dars ra {subject} vared conid : "))
            subjects[subject] = grade
        except ValueError :
            print("lotfan nomre adadi ra vared conid :")
            students[name] = subjects

print("\n gozaresh nomarat : \n")
for subject in subjects.items() :
    total = sum(subject.values())
    count = len(subject)
    average = total/count if count > 0 else 0
    print(f"dansh amoz : {name}")
    for course, grade in subject.items() :
        print(f"{course} : {grade}") 
        print(f"moadel : {average:.2f}\n")