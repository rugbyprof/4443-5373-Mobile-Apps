## Teams & Requirements

### Requirements

#### 1) Firebase / Backend Team

- **Resources:**
    - https://www.firebase.com/docs/web/guide/structuring-data.html
- **Firebase Service:**
- A service that can be injected into any component that gives other teams a consistent way of interacting with firebase.
- This group will determine how data is received and returned.
- **Operation Definitions:**
    - `POST` => Adding additional new data to a collection (adding a new document).
    - `GET` => Requesting existing data from a collection (receiving a document, or array of documents).
    - `PUT` => Updating existing data in a collection (changing a value in a document).
    - `DELETE` => Removing data from a collection (like a document).
- **Specific Operations:**
    - Users Collection Operations:
        - `POST` a new user 
        - `GET` a user
        - `PUT` a user (update)
        - `DELETE` a user (not important right now)

    - Groups Collection Operations:
        - `POST` a new group
        - `GET` all groups
        - `DELETE` a group

    - Friends Collection Operations:
        - `POST` A friend request
        - `DELETE` A friend request
        - `POST` A new friend connection
        - `DELETE` A friend connection

    - Locations Collection Operations:
        - `POST` a location 
        - `GET` a location (e.g. current user location)

    - Images(Assuming FB Storage or FireStore base 64 images) Collection Operations::
        - `GET` a single image
        - `GET` a group of images
        - `POST` tags for an image
        - `GET` tags for an image
        - `PUT` tags for an image
        - `DELETE` an image / with tags

    - Messaging
        - `POST` a new message
        - `GET` a posted message


#### 2) User Locations Team

- **Resources:**
    - GeoLocation: https://ionicframework.com/docs/native/geolocation/
    - GeoFencing: https://ionicframework.com/docs/native/geofence/
    - Location Accuracy: https://ionicframework.com/docs/native/location-accuracy/
- **Location Service:**
    - Run in background or event driven.
    - Events:
        - Tap / Click / Swipe 
        - Enter or leave Geofenced area like a place (home, restaurant, etc), friend (based on distance)
    - Injectable into any component
- **Operations**:
    - `GET` a users location
    - `GET` a groups location
    - `GET` friends (like a group) location
    - `POST` a users location
    - `PUT` update a users latest location
  

#### 3) Routing / Location Based Services Team

- A google geo-location service wrapper that provides basic geo location functionality preferably as a service but the customer will be ok if the geo-location services are not fully decoupled from the views.
- **Resources:**
    - https://github.com/ionic-team/ionic-native-google-maps/tree/master/documents
    - https://codeburst.io/native-google-maps-and-geolocation-ionic-fe635a00249d
- **Map Visualization Service:**
    - Obtain routes between points
    - Show nearby locations (restaurants) (wish list)
    - Calculate Distance and Routes between:
        - user and user
        - user and group
        - user and location
        - Routes are not saved, but are displayed to the user.
    - GeoCoding - (address => lat/lon)
    - Reverse GeoCoding (lat/lon => address)
    - Addresses may be stored in Firebase with locations with Lat/Lon
- **Views / Components:**
    - Use the service previously defined to obtain locations and routes and display them on some map. 
    - Routing (directions) between places can be done by leaving the app and starting the local routing app from the phone (google maps, apple maps, etc.).


#### 4) Camera / Image Editing / Social Media Team

- **Resources:**
    - https://ionicframework.com/docs/native/photo-viewer/
    - https://ionicframework.com/docs/native/photo-library/
    - https://ionicframework.com/docs/native/lastcam/
- This group will use the backend created by the firebase group. 
- Views:
    - One will give the user the ability to take a photo, add tags.
    - Another view will allow the user to get a stored photo, add tags, possibly geotag. 
- Uploads will be taggd with location if possible.
- Uploads also have the possibility to go to instagram and / or facebook as well.

#### 5) UI/UX Team

- App layout and design
- In charge of:
    - page transitions
    - page layouts
    - basic theme 
    - Error message display (toasts etc.)
    - Menu Styles. 

#### 6) IM Component Team

- This gives users ability to instant message thier friends, or other users currently being viewed or nearby.
- Use Cases:
    - Message individual
    - Message group
    - Message location


### Student List

**Tentative:**

| #   | Student              | Group   | 
| --- | -------------------- | ------- |
| 1   | Allard, Brice W.     | 1,2     |
| 2   | Beaver, Sarah A.     | 1,2,3,5 |
| 3   | Callender, Clorissa  | 3, 4    |
| 4   | Conley, Zachary L.   | 4,1     |
| 5   | Cortez, Darien A.    | 2, 5    |
| 6   | Dinh, Luong T.       | 4,1     |
| 7   | Divine, William M.   | 4, 5    |
| 8   | Duhan, Christopher   | 1,2     |
| 9   | Glebe, Jeremy D.     | 1, 5    |
| 10  | Joseph, Jamal J.     | 2, 4    |
| 11  | Lopez, Jakob L.      | 1,2     |
| 12  | McGinn, David N.     | 5,2     |
| 13  | Michener, Cory L.    | 5, 1    |
| 14  | Mullins, Samuel S.   | 1, 2    |
| 15  | Patterson, Jacob W.  | 1,5     |
| 16  | Placencia, Carlos A. | 2, 1    |
| 17  | Rollerson, Keona     | 2,3,4   |
| 18  | Rowe, Travis E.      | 3,4,2   |
| 19  | Smith, Buddy J.      | 1,2,5   |
| 20  | Vijayaraman, Vasudev | 1,2     |
| 21  | Workman, Brett M.    | 1,2     |

### Team Assignments
