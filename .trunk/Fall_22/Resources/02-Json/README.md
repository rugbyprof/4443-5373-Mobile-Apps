## JSON - Javascript Object Notation Overview

### Wikipedia Definition

`Json` (JavaScript Object Notation, pronounced `/jaysawn/;`) is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays (or other serializable values). It is a common data format with diverse uses in electronic data interchange, including that of web applications with servers.

`Json` is a language-independent data format. It was derived from JavaScript, but many modern programming languages include code to generate and parse Json-format data. `json` filenames use the extension `.json` .<sup>[[1]](#1)</sup>

### Motivation

Being `language-independant` is very important. Language-independance means that some or all programming languages can interact with (in this case) `json`. The reason this is possible is that `json` follows a set of predefined rules for storage, otherwise known as a `standard`. 

Most contemporary programming languages have a `json` library. This allows you to write out a `json` file in one language, and read it in using another. This is not groundbreaking since there does exist other file formats that allow similar behavior: `csv` and `xml` come to mind. Without getting into a head to head comparison, each have their own upsides and downsides. 

### Json Overview

><sup>Note: I'm going to use Python syntax when showing code examples. Python's data structures fit real well with Json's definitions (even though it started via Javascript).</sup>

Let me cover json using examples. Json really breaks down to `key`:`value` pairs. Where a `key` is a string identifier (like a variable name) that is associated with a value. The value can be:
- integer
- float
- string
- array
- onother json object

**Simple Json Example:**
```json
"key":"value"
```
or
```json
"apples":204
```

**Json w/ Python Example:**
```python
fruits = {
    "apples":204
}
print(fruits["apples"])
# prints 204
```

**Json w/ Python Example:**
```python
person = {
    "first":"Mukul",
    "last":"Sonwalker",
    "age":32,
    "height"1.77
}
print(person["last"])
#prints Sonwalker
```

### Objects (Dictionaries)

You may have gleaned from the previous examples that curly braces are what "define" the json object. The python syntax calls them dictionaries, but when a Python dictionary is written out to a file it perfectly converts to json syntax. Look at the following Python exapmle: 

```python
import json

# create a python dictionary called "person"
person = {
    "first":"Mukul",
    "last":"Sonwalker",
    "age":32,
    "height"1.77
}

# write this to a file:
with open('person.json','w') as f:
    f.write(json.dumps(person))
```

This would result in a json file called "person.json" with the following contents:

```json
{
    "first":"Mukul",
    "last":"Sonwalker",
    "age":32,
    "height"1.77
}
```
The curly braces define an "object". This specific object has 4 `key:value` pairs and is a very generic straightforward example of a json object that shows string keys with a variety of data types as values. However, one of the strengths of json is (like most context free grammars) is it can be stored using any combination of its valid components. For example:

- string:string
- string:int
- string:float
- string:list
- string:object

To strengthen this point, lets go big or go home:


<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/json_superhero_example.png" width="400">

<sup>Source:[[2]](#2)   Actual file with json is [here](squad.json)</sup>

The above example shows multiple combinations of `key:value` data, where all the keys are strings, but the values vary from strings, to ints, to arrays and other objects. This is all fine and dandy, until you have to access the values in the object! So I will give various examples in Python showing you how to access items as well as traverse over the object to visit everything. 

-----

First let us read in the json file into a Python data structure:

```python
import json                     # need the json lib for `loads` and `dumps`

with open("squad.json") as f:
    data = f.read()             # read entire json string into variable
    jData = json.loads(data)    # convert json string into python dictionary 
```

Using our newly read `jData`, to access any top level key (lines 2-7) you simply use the key to do so. 
```python
print(jData["formed"])      # prints: 2016
print(jData["homeTown"])    # prints: Metro City
```

-----

If you looped over this json object (now Python dictionary) and print it out like so:

```python
for item in jData:
    print(item)
```

Outputs:
```txt
squadName
homeTown
formed
secretBase
active
members
```
That's not very helpful. It's only the keys! 

-----

We need to access both key and value, so here's one way:

```python
for item in jData:
    print(f"{item} : {jData[item]}")
```

Outputs:
```txt
squadName : Super hero squad
homeTown : Metro City
formed : 2016
secretBase : Super tower
active : True
members : [{'name': 'Molecule Man', 'age': 29, 'secretIdentity': 'Dan Jukes', 'powers': ['Radiation resistance', 'Turning tiny', 'Radiation blast']}, {'name': 'Madame Uppercut', 'age': 39, 'secretIdentity': 'Jane Wilson', 'powers': ['Million tonne punch', 'Damage resistance', 'Superhuman reflexes']}, {'name': 'Eternal Flame', 'age': 1000000, 'secretIdentity': 'Unknown', 'powers': ['Immortality', 'Heat Immunity', 'Inferno', 'Teleportation', 'Interdimensional travel']}]
```

That's a little better. 

-----

Here's another way to get the same output:

```python
for k,v in jData.items():
    print(f"{k} : {v}")
```

-----

### .items()

What does `.items()` do? Well, first let me show you a couple of other Python-isms. Real quick, a `tuple` is a Python container that is immutable, but can be accessed like an array (or list). Python `lists` and `tuples` are similar but differ by the simple fact that tuples cannot be changed (mutated) and lists can be. 


Back to the example:

```python
# This makes "point" a tuple that holds two items.
point2d = (3,7)

print(point2d[0]) # prints 3
print(point2d[1]) # prints 7

# now the cool part

x , y = point2d

# x now contains 3
# y now contains 7

point3d = (11,13,23)  # a tuple with 3 items 

x,y,z = point3d

# x now contains 11
# y now contains 13
# z now contains 23
```

What does this have to do with `.items()`? Well, the .items function takes a `key:value` pair and returns it as a `tuple`. So the first three times the following loops (over our example json object): 

```python
for k,v in jData.items():
    print(f"{k} : {v}")
```

`jData.items()` turns into: 

```python
("squadName" , "Super hero squad")
("homeTown" , "Metro City")
("formed" , 2016)
```

Which basically turns into:

```python
k,v = ("squadName" , "Super hero squad")
k,v = ("homeTown" , "Metro City")
k,v = ("formed" , "2016")
```
So `k` gets the tuple[0] value and `v` gets the tuple[1] value.

### Lists

You probably noticed and wondered about the following output (I expanded it for readability):

```
members : [
        {
            "name": "Molecule Man",
            "age": 29,
            "secretIdentity": "Dan Jukes",
            "powers": [
                "Radiation resistance",
                "Turning tiny",
                "Radiation blast"
            ]
        },
        {
            "name": "Madame Uppercut",
            "age": 39,
            "secretIdentity": "Jane Wilson",
            "powers": [
                "Million tonne punch",
                "Damage resistance",
                "Superhuman reflexes"
            ]
        },
        {
            "name": "Eternal Flame",
            "age": 1000000,
            "secretIdentity": "Unknown",
            "powers": [
                "Immortality",
                "Heat Immunity",
                "Inferno",
                "Teleportation",
                "Interdimensional travel"
            ]
        }
    ]
```

Where the key: `members` pointed to a list (array) of objects (super heros). So the question is: How do we access those data fields? Well first you need to know that `[]` (square brackets) define "lists" (arrays) and we can access them as such. So to print out the first super hero we simply write:

```python
print(jData["members"][0])
```

This uses the key "members" to "point to" (for lack of a better term) the list of heros, and the uses the index [0] to grab the first hero in the list. 

-----

What of we wanted to print out the age of the second hero?

```python
print(jData["members"][1]["age"])
```

Notice we use one more level of access with the "age" key. 

-----

Ok. What if we wanted to print out the first power for each super hero?

```python
for hero in jData["members"]:
    print(hero["powers"][0])
```

Prints:

```
Radiation resistance
Million tonne punch
Immortality
```

-----

Or print how many powers each hero has:

```python
for hero in jData["members"]:
    print(len(hero["powers"]))
```

Prints:

```
3
3
5
```

-----

Finally, what if we wanted to just print out everything? There are multiple ways to make this happen. One way is to test each "value" to see what type it is. By using `isinstance(object, type)` you can make decisions based on whether a value is a "list", "dictionary", or simply a regular scalar value.

For our example, I will leverage our knowledge of the object. I know that "members" is a list and I know that "powers" is also a list.

```python
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
```

Prints out:

```
squadName : Super hero squad
homeTown : Metro City
formed : 2016
secretBase : Super tower
active : True
 
	name : Molecule Man
	age : 29
	secretIdentity : Dan Jukes
	powers:
		Radiation resistance
		Turning tiny
		Radiation blast
 
	name : Madame Uppercut
	age : 39
	secretIdentity : Jane Wilson
	powers:
		Million tonne punch
		Damage resistance
		Superhuman reflexes
 
	name : Eternal Flame
	age : 1000000
	secretIdentity : Unknown
	powers:
		Immortality
		Heat Immunity
		Inferno
		Teleportation
		Interdimensional travel
```

-----







- <a id="1">[1]</a>  https://en.wikipedia.org/wiki/JSON
- <a id="1">[2]</a>  https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON