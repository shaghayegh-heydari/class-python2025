students = {}

while True :
    name = input("nam dansh amoz ra vared conid :")
    if name.lower() == "exit" :
        break

    subjects = {}
    while True :
        subject = input("nam dars ra vared conid :")
        if subject.lower() == "done" :
            break
        try :
            grade = float(input(f"nomerh dars ra {subject} vared conid :"))
            students[subject] = grade
        except ValueError :
            print("lotfan nimrh adadi ra vared conid :")
            students[name] = subjects


print("\n gozaresh nomarit :\n ")
for subject in students.items() :
    total = sum(subject.values())
    count = len (subject)
    average = total / count if count > 0 else 0
    print (f"danesh amoz : {name}")
    for course, grade in subject.items() :
        print(f"{course} : {grade}")
        print(f"moadel : {average:.2f}\n")
