import json

def save_jsoon(input_dict) :
    with open (rf"data\task.json","a") as f:
        json.dump(input_dict , f)
    print("your data save successfully")

data = input("pleas enter data (YYY-MM-DD): ")
tasks = input("pleas input all of your tasks and separat by comma:")

my_taks_dict = {dict:tasks.split(",")}
save_jsoon(my_taks_dict)