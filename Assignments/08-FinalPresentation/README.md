## Final Presentation Checklist

### Broad Overview of Project Grade

- I have been repeating myself all semester long about certain types of behaviors (functionality) that I expect your app to contain even though there have not been a written requirements list for every screen or assignment. 
- Normally I would at least create a fundamental basic requirements doc, but I wanted to leave it open for interpretation and I want to see individual and group efforts without a set of bare bones requirements. Honestly, when I write a minimum viable set of requirements, it makes it very easy for mediocre projects to achieve high grades. This will not be the case this semester. 
- However, we can all honestly say that I have repeated myself many many many times about effort. Yes, I give CS majors a pass on design (css, colors, etc.) but I don't give a pass on effort. 
- Bottom line is grade is highly dependant on perceived effort.
- To see a lot of default expected behaviors: [GO HERE](./expected_defaults.md)
- I added to this formal list at the bottom.
- Not all categories apply, but look at the ones that do.

### Graphics and Design

- 10% of app grade.
- Zero graphics, boring plain colors, lack of pleasant positioning of elements shows little effort.
- Your app should have some graphics (stolen, copied, borrowed, etc.). We are making zero money so its ok. As long as you don't use the content EVER to make money, or act as if it is yours, then again, its ok.
- Colors and theming ... again I will look for perceived effort. I have mentioned in class many times along with links to sites with themes, css frameworks, and more. 
- It is obvious if you didn't put effort into the graphical / colorful / pleasing positioning / fonts. 


### General Presentation Format And Info
- **Time**
  - 10-15 minutes in length
  - 3-5 minutes for questions
- **Format**
  - Pre-made VIDEO.
  - 15% of presentation grade.
  - Your presentation will be a screen recorded video in which you will create before you show up to class.
  - Your video will not have any audio, as you will narrate what is going on as we watch your app load, screens change, database updates shown etc.
  - The reason for this is because there are an unknown number of issues with our apps loading over the local network, and the unknowns of laptop connections to the presentation podium and similar random issues.
  - This also ensures you should practice and have the length of your presentation known as well as who will speak during specific parts.
  - No screen recording = 15% reduction of presentation score.
  
### Group Grading

- Grading is hard.
- Giving everyone an A is easy.
- Giving everyone an F is easy.
- Putting effort is expected, if you don't put in effort, your grade will be reduced.
- If you don't have grades for everyone else in your section, your grade will be reduced. 

#### 4443
- Grading Link 4443 https://forms.office.com/r/GZTYCJacd6

#### 5373
- Grading Link 5373 https://forms.office.com/r/QZvbQtkPha


## Api
    - Fast Api
    - Get Routes
    - Post Routes
    - Put Routes

## DB
    This assumes your doing a candy theme. If your not, you should have similar functionality, amount of data, and number of tables or collections.
    - Mongo or Mysql
    - Collections (or Tables)
      - Users
      - Locations
      - Candy
      - Categories

## Screens

- Not Restricted Menu Links
  - Registration
  - Login
  - Home (or Splash or Landing)
- Restricted Menu Links
  - Location
  - Fake Chat
  - Image Upload

### Splash / Home 

- Some kind of App Title
- Image or logo
- Links to Register or Login
- No links to restricted pages (location, fake chat, image upload)

### Registration

- **Form Fields**
  - First Name
  - Last Name
  - User Id (optional)
  - Email
  - Password
- **Navigation**
  - Non restricted links 

### Login

- Username or Email
- Password
- Password is hashed in database

### Search

- Page should look like a search page with an intuitive interface utilizing icons or instructions 
- Navigation bar or similar

- Multiple levels of search in a variety of implementations
  - Category + item search
  - Keyword + keyword (e.g. chocolate & orange)
  - Price range + keyword (e.g. < 50 & movie theater)

### Location

- Page should have a map view and possibly some map tools provided by the map library.
- Any additional search capabilities or fake store locations or color adaptations / icon adaptations are a welcome addition
- At minimum show user location + additional users who have "given access" to their location. 
- A location table or collection determines who shows up
- Info in location collection should only contain:
  - user_id
  - lon
  - lat
  - timestamp
- Where timestamp is used to timeout current individuals who gave access to their location. This is not required to be implemented but is the kind of functionality that boosts your grade.


### Fake Chat

- A chat page that allows authenticated users ability to chat
- It should have the design and layout of a chat page + the theme of the app.
- It should have a list of "groups" or "users" as well to choose to have a chat with.

### Image Upload

- This page can be accessed from many locations not on the main menu (navigation) but through an image upload button. 
  - For example:
    - chat page to send an image to chat client
    - search page (fake admin page) to replace candy (or similar) image
    - location page to add image of another user
  - This functionality should be accompanied by a post route that saves an image on your server disk.
  - Part of the image page allows uploaded images to be browsed. 
