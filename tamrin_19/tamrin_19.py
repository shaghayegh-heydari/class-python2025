import json

with open ("friends.json","r" , encoding = "utf-8") as f :
    my_json = json.load (f)

me = my_json ["me"]

text = f"i am {me["shaghayegh"]}.i have {me["14"]} years old.my hobbies is {"reading".json(me["hobbies"])}."

with open ("about_me.text","w",encoding = "utf-8") as file :
    file.write(text)

print("file'about_me.taxte'created successfully.")