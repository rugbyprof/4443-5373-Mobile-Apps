## FLApp - Awesome Project
#### Due : TBD

### Firebase Structure

Firebase data types:
https://firebase.google.com/docs/firestore/manage-data/data-types

## User Collection:

There will be a user collection that stores general user information along with a sub-collection of user locations.

#### Fields:
>- first : string
>- last : string 
>- email : string
>- registered : date
>- avatar: reference (cloud firestore reference)
>- locations : sub-collection

___Example Json___:
```json
{
    "first": "joe",
    "last": "smith",
    "email": "joe.smith@gmail.com",
    "registered": "October 24, 2018 at 12:00:00 AM UTC-5",
    "locations": "sub-collection of locations",
    "groups" : "sub-collection of group_ids"
}
```

## User Locations Collection:

Each user will have their own collection of locations that stores a location along with a category of the type of location.

#### Fields:
>- location : geoPoint
>- stamp : dateTime 
>- type : string
>- address : map (optional)

___Example___:
```json
{
    "location": [33.93874, 122.29837],
    "stamp": "October 24, 2018 at 12:00:00 AM UTC-5",
    "type": ["geotag", "checkin", "favorite", "...", "home"],
    "address" : {
        "city":"Wichita Falls",
        "state":"Texas",
        "street": "3410 Taft Blvd",
        "zip": "76308"
    }
}
```

## Location Types Collection:

A list of location types with descriptions.

#### Possible Purpose:
Can be used to populate drop down menus when a user wants to label a saved location.

#### Fields:
>- location-type : string
>- description : string 
>- date-created: dateTime
>- creator-id: string

___Example___:
```json
{
    "location-type": "favorite",
    "description": "A favorite location that you frequent often.",
    "date-created": "October 24, 2018 at 12:00:00 AM UTC-5",
    "creator-id" : "0239hu23jhv4"
}
```

## Locations Collection:

A list of top level locations of users, showing latest locations. 

#### Possible Purpose:
This collection would probably be used to show locations of users to all other users in same group. It should be maintained by some observable cloud based function monitoring the changes in users personal location collections:

#### Fields:
>- user-id : string
>- location-id : string 

___Example___:
```json
{
    "user-id": "Hdla99yfyjf",
    "location-id": "IKj8ekd8d",
}
```

## Groups Collection:

A list of group types with descriptions.

#### Fields:
>- group-type : string
>- description : string 
>- date-created: dateTime
>- creator-id: string

___Example___:
```json
{
    "group-type": "friends",
    "description": "All of Joe's freinds.",
    "date-created": "October 24, 2018 at 12:00:00 AM UTC-5",
    "creator-id" : "0239hu23jhv4"
}
```

## Friends Request Collection:

A collection of friend requests. Could be a sub-collection in a user possibly. 

#### Fields:
>- requestor-id : string - person requesting a friend
>- requestee-id: string  - person receiving the request
>- request-date: dateTime - when request was made
>- status : string - [Accepted, Rejected, None]

___Example___:
```json
{
    "requestor-id ": "0239hu23jhv4",
    "requestee-id": "IJNHhu23jhv2",
    "request-date": "October 24, 2018 at 12:00:00 AM UTC-5",
    "status" : "None"
}
```

### Complete User Example

___Example Json___:
```json
{
	"first": "joe",
	"last": "smith",
	"email": "joe.smith@gmail.com",
	"registered": "October 24, 2018 at 12:00:00 AM UTC-5",
	"locations": [{
		"location": [33.93874, 122.29837],
		"stamp": "October 21, 2018 at 6:23:00 PM UTC-5",
		"type": ["geotag"],
		"address": {
			"city": "Wichita Falls",
			"state": "Texas",
			"street": "123 Main Blvd",
			"zip": "76308"
		}
	}, {
		"location": [33.93874, 122.29837],
		"stamp": "October 30, 2018 at 3:25:12 PM UTC-5",
		"type": ["restaurant"],
		"address": {
			"city": "Wichita Falls",
			"state": "Texas",
			"street": "234 Southwest Pkwy",
			"zip": "76310"
		}
	}, {
		"location": [33.93874, 122.29837],
		"stamp": "October 24, 2018 at 12:00:00 AM UTC-5",
		"type": ["work"],
		"address": {
			"city": "Wichita Falls",
			"state": "Texas",
			"street": "3410 Taft Blvd",
			"zip": "76308"
		}
	}],
	"groups": [
		"12341345dsad",
		"adsfwqerf3453"
	]
}
```

