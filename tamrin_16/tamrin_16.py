people = {}

while True :
    name = input("name ra vared conid :")
    if name.lower() == "done":
        break
    age = input("age ra vared conid :")
    gender = input("gender re vared conid :")
    people[name] = [age , gender]

for name in people :
    age,gender = people[name]
    print(name,age,gender)
