## FLApp - Awesome Project
#### Due : TBD

### Firebase Structure

Firebase data types:
https://firebase.google.com/docs/firestore/manage-data/data-types

**User Collection:**

There will be a user collection that stores general user information along with a sub-collection of user locations.

**Fields:**
>- first : string
>- last : string 
>- email : string
>- registered : date
>- avatar: reference (cloud firestore reference)
>- locations : sub-collection

___Example Json___:
```json
{
    'first': 'joe',
    'last': 'smith',
    'email': 'joe.smith@gmail.com',
    'registered': 'October 24, 2018 at 12:00:00 AM UTC-5',
    'locations': 'sub-collection of locations',
    'groups' : 'sub-collection of group_ids'
}
```
**User Locations Collection:**

Each user will have their own collection of locations that stores a location along with a category of the type of location.

**Fields:**
>- location : geoPoint
>- stamp : dateTime 
>- type : string

___Example___:
```json
{
    location: [33.93874° N, 122.29837° W],
    stamp: October 24, 2018 at 12:00:00 AM UTC-5,
    type: [geotag, checkin, favorite, home, etc.]
}
```

**Location Types Collection:**

A list of location types with descriptions.

**Fields:**
>- location-type : string
>- description : string 
>- date-created: dateTime
>- creator-id: string

___Example___:
```json
{
    location-type: favorite,
    description: "A favorite location that you frequent often.",
    date-created: October 24, 2018 at 12:00:00 AM UTC-5,
    creator-id : 0239hu23jhv4
}
```

**Locations:**

A list of top level locations of users, showing latest locations. This collection would probably be used to show locations of users to all other users in same group. It should be maintained by some observable cloud based function monitoring the changes in users personal location collections:

**Fields:**
>- location-type : string
>- description : string 
>- date-created: dateTime
>- creator-id: string

___Example___:
```json
{
    location-type: 324kjh34,
    location: [33.93874° N, 122.29837° W],
    last-updated: October 24, 2018 at 12:00:00 AM UTC-5,
    user-id : 0239hu23jhv4
}
```

**Group Types Collection:**

A list of group types with descriptions.

**Fields:**
>- group-type : string
>- description : string 
>- date-created: dateTime
>- creator-id: string

___Example___:
```json
{
    group-type: friends,
    description: "All of Joe's freinds.",
    date-created: October 24, 2018 at 12:00:00 AM UTC-5,
    creator-id : 0239hu23jhv4
}
```

### Complete Example

___Example Json___:
```json
{
    first: joe,
    last: smith,
    email: joe.smith@gmail.com,
    registered: October 24, 2018 at 12:00:00 AM UTC-5,
    locations: [
        0239hu23jhv4: {
            location: [33.93874° N, 122.29837° W],
            stamp: October 24, 2018 at 12:00:00 AM UTC-5,
            type: check-in
        },
        q2341fdqwer: {
            location: [33.93874° N, 122.29837° W],
            stamp: October 24, 2018 at 12:00:00 AM UTC-5,
            type: geotag
        },
        ...
        sdfgar2345: {
            location: [33.93874° N, 122.29837° W],
            stamp: October 24, 2018 at 12:00:00 AM UTC-5,
            type: home
        }
    ]
    groups : [
        12341345dsad,
        adsfwqerf3453
    ]
}
```


### Project Components:

Each component will provide a view with a service that saves / retrieves information from a central firebase project store.

1) Location Service
2) Image Upload Service
3) Login / Registration Service



