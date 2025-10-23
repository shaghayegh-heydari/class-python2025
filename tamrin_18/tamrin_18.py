import json
moshakhasat= {"name":"shaghayegh",
"age":14,
"grade":"nohom",
"favorite":["book","doll"]}
with open("info.json","w")as f:
    json.dump(moshakhasat,f)                              