names = input("pleas enter your names and separate by comma:  ")
with open("name.txt","w") as f:
    for name in names.split(","):
        f. write (f"{name.strip()}/n")

with open ("name.txt","r")as f:
    my_names = f.readlines()
for my_names in my_names:
    print(f"Hello{my_names.strip("\n")}My dear friend")
   
     