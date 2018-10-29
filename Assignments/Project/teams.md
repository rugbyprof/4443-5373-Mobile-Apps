## Teams & Requirements

### Requirements

- Firebase / Backend Team
- User Locations / Routing Team
- Camera / Social Media Team
- UI / UX Team


#### Firebase / Backend Team
    - Create a ***firebase service*** that can be injected into any component that gives the following functionality:
    - Users
        - POST a new user 
        - GET a user
        - PUT a user (update)
        - DELETE a user (not important right now)
    - Groups
        - POST a new group
        - GET all groups
        - DELETE a group
    - Locations:
        - POST a location
        - GET a location (e.g. current user location)
    - Images:
        - POST a new image
        - GET a single image
        - GET a group of images
        - POST tags for an image
        - GET tags for an image
        - PUT tags for an image
        - DELET an image / with tags.
    - Example use cases:
        - Get all locations for a single user.
        - Get all locations for a group of users.


#### User Locations / Routing Team
    - Location:
        - GeoLocation: https://ionicframework.com/docs/native/geolocation/
        - GeoFencing: https://ionicframework.com/docs/native/geofence/
        - Location Accuracy: https://ionicframework.com/docs/native/location-accuracy/
        - ***Location Service:***
            - Run in background or event driven.
            - Events:
                - Tap / Click / Swipe 
                - Enter or leave Geofenced area like a place (home, restaurant, etc), friend (based on distance)
            - Injectable into any component
            - GET a users location
            - POST a users location
            - PUT update a users latest location
    - Routing 
        - Routing between two points (users or locations) using some API, most likely Google.
        - Routes are not saved, but are displayed to the user.
        - Best scenario, create a Routing service that any component and call and get a route (json object of points) to be displayed on a map.

    - Locations Visulization
        - Use the Location and Routing services to display one or more users or routes.
        - https://github.com/ionic-team/ionic-native-google-maps/blob/master/documents/README.md
        - Visualizing Routing and Static points using Google Maps Api


#### Camera / Social Media Team
    - https://ionicframework.com/docs/native/photo-viewer/
    - https://ionicframework.com/docs/native/photo-library/
    - https://ionicframework.com/docs/native/lastcam/
    - This group will use the backend created by the firebase group. 
    - Views:
        - One will give the user the ability to take a photo, add tags.
        - Another view will allow the user to get a stored photo, add tags, possibly geotag. 
    - Uploads will be taggd with location if possible.
    - Uploads also have the possibility to go to instagram and / or facebook as well.

#### UI/UX
    - App layout and design
    - In charge of:
        - page transitions
        - page layouts
        - basic theme 
        - Error message display (toasts etc.)
        - Menu Styles. 

### Student List

1	Allard, Brice W.	
2	Beaver, Sarah A.	
3	Callender, Clorissa 
4	Conley, Zachary L.	
5	Cortez, Darien A.	
6	Dinh, Luong T.		
7	Divine, William M.	
8	Duhan, Christopher 	
9	Glebe, Jeremy D.	
10	Joseph, Jamal J.	
11	Lopez, Jakob L.		
12	McGinn, David N.	
13	Michener, Cory L.	
14	Mullins, Samuel S.	
15	Patterson, Jacob W.	
16	Placencia, Carlos A.
17	Rollerson, Keona	
18	Rowe, Travis E.		
19	Smith, Buddy J.		
20	Vijayaraman, Vasudev
21	Workman, Brett M.	

### Team Assignments