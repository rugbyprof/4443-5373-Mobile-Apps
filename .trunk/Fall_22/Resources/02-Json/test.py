import json                     # need the json lib for `loads` and `dumps`

with open("./squad.json") as f:
    data = f.read()             # read entire json string into variable
    jData = json.loads(data)    # convert json string into python dictionary 

print(jData["formed"])      # prints: 2016
print(jData["homeTown"])    # prints: Metro City

print("")

for item in jData:
    print(item)

print("")

for item in jData:
    print(f"{item} : {jData[item]}")

for hero in jData["members"]:
    print(len(hero["powers"]))


for k,v in jData.items():
    if k == "members":
        for hero in v:
            print(" ")
            for kk,vv in hero.items():
                if kk == "powers":
                    print("\tpowers:")
                    for power in vv:
                        print(f"\t\t{power}")
                    
                else:
                    print(f"\t{kk} : {vv}")
        
    else:
        print(f"{k} : {v}")

# This makes "point" a tuple that holds two items.
point2d = (3,7)

print(point2d[0]) # prints 3
print(point2d[1]) # prints 7

# now the cool part

x , y = point2d

# x now contains 3
# y now contains 7

point3d = [11,13,23]  # a list with 3 items 

x,y,z = point3d

# x now contains 11
# y now contains 13
# z now contains 23

print(x,y,z)

