import pprint as pp
from random import shuffle

names = """| 1| Allard, Brice W.| 1,2| 0 |
| 2   | Beaver, Sarah A.     | 2,3,5 | 1 |
| 3   | Callender, Clorissa  | 3,4| 0 |
| 4   | Conley, Zachary L.   | 4,1| 0 |
| 5   | Cortez, Darien A.    | 2,5| 0 |
| 6   | Dinh, Luong T.       | 4,1| 0 |
| 7   | Divine, William M.   | 4,5| 0 |
| 8   | Duhan, Christopher   | 1,2| 0 |
| 9   | Glebe, Jeremy D.     | 1,5| 0 |
| 10  | Joseph, Jamal J.     | 2,4| 1 |
| 11  | Lopez, Jakob L.      | 1,2| 1 |
| 12  | McGinn, David N.     | 5,2| 0 |
| 13  | Michener, Cory L.    | 5,1| 0 |
| 14  | Mullins, Samuel S.   | 1,2| 1 |
| 15  | Patterson, Jacob W.  | 1,5| 0 |
| 16  | Placencia, Carlos A. | 2,1| 0 |
| 17  | Rollerson, Keona     | 2,3,4| 1 |
| 18  | Rowe, Travis E.      | 3,4,2| 0 |
| 19  | Smith, Buddy J.      | 1,2,5| 1 |
| 20  | Vijayaraman, Vasudev | 1,2| 1 |
| 21  | Workman, Brett M.    | 1,2| 1 |"""

names = names.split("\n")

data = {}
groups = {}
numCount = {}

for line in names:
    line = line.split("|")
    nums = line[3].strip().split(',')
    choice = line[4].strip()
    for num in nums:
        if not num in numCount:
            numCount[num] = 0
        numCount[num] += 1
    nums.append(choice)
    data[line[2].strip()] = nums

for name, nums in data.items():
    #shuffle(nums)
    choice = int(nums[-1])
    group = str(nums[choice])
    print(group)
    if not group in groups:
        groups[group] = []
    groups[group].append(name)
print()
pp.pprint(groups)
pp.pprint(numCount)