darage = [22,24,21,25,23,20]
bishtarin = [0]
camtarin = [0]

for dama in darage :
    if dama < bishtarin :
        bishtarin=dama
    if dama > camtarin :
        camtarin=dama

print(f"list dama {darage}")
print(f"lotfan {bishtarin}ra bedh")
print(f"lotfan {camtarin}ra bedh")