## Terminology 

### Frontend

**Overview**: The frontend refers to the part of an application that users interact with directly. It's everything the user experiences, from the layout and design to the behavior of interactive elements.

**Example**: In a mobile app, the frontend would be the user interface (UI) designed in Swift for iOS or Kotlin/Java for Android or Flutter & React for both platforms. This includes buttons, text fields, images, and animations.

### Backend

**Overview**: The backend is where the application's logic, database interactions, and server-side functions occur. It's the part of the software that users don't see, handling data processing, storage, and security.

**Example**: A Node.js or Python server receiving HTTP requests from the mobile app, processing those requests (e.g., fetching, updating data), and communicating with a database like MySQL or MongoDB.

### Middleware

**Overview**: Middleware is software that acts as a bridge between different parts of an application or between the application and the database or other services. It's used for logging, authentication, error-handling, and other functions that are executed between the initial request and the final response in a server.

**Example**: In an Express.js app (express is a Node library), middleware could be a function that checks if a user is authenticated before allowing them access to certain routes.

### Models

**Overview**: Models are part of the application that represent the data structure and business logic. They often correspond to tables in a database and define the schema of these tables.

**Example**: In a MongoDB-based application (Mongo stores Json documents) a model might match up to a `document` with attributes like username, password, and email. Or in a regular SQL database a model might match up to a table  with columns that include username, password, and email.

### Routes

**Overview**: Routes determine how an application responds to client requests to a particular endpoint, each of which is associated with a URI (path) and an HTTP request method (GET, POST, etc.).

**Example**: In a Fast API script, a route might be defined to handle requests to `GET /users` which would return a list of users. 

### Full Stack

**Overview**: Full stack refers to the development of both frontend and backend aspects of an application. A full-stack developer has the skills to work on the server side, database, and client side.

**Example**: A developer working on both a React Native mobile application (frontend) and its corresponding Node.js backend. Or, a developer that writes the html, css, and javascript (front end stuff) that talks to a Fast API backend in order to get or post data. 

## More Terminology

1. **API (Application Programming Interface)**: Allows different software applications to communicate with each other. In mobile apps, APIs are used to connect the app with the backend server for data exchange.

<img src="https://images2.imgbox.com/2b/39/ESNGCQn8_o.png">

2. **Database**: A structured collection of data. In the context of mobile apps, databases like Firebase or PostgreSQL store user data, app content, settings, etc.

<img src="https://images2.imgbox.com/fc/84/cikNi1YJ_o.png">

3. **Authentication and Authorization**: Authentication is verifying who a user is (e.g., through a login system), while authorization is about what they are allowed to do (e.g., admin access).

4. **Client-Server Model**: In this model, the client (e.g., mobile app) sends requests to the server (backend system), which processes them and returns a response.

<img src="https://images2.imgbox.com/bb/59/yaIx6391_o.png">

5. **JSON (JavaScript Object Notation)**: A lightweight data-interchange format often used for exchanging data between a server and a web/mobile application. It is similar to a python dictionary or STL Map in that it uses key value pairs to store data, but it can also be stored in a file in txt format. 

6. **RESTful Services/APIs**: An architectural style for designing networked applications, where requests are made via HTTP to CRUD (Create, Read, Update, Delete) data. A `RESTful API` vs just an `API` is really a set of guidelines to use when creating routes. (more later)

7. **MVC (Model-View-Controller)**: A pattern used to separate an application into three interconnected components, improving maintainability and scalability.

<img src="https://images2.imgbox.com/e9/48/GHXMrGSa_o.png">

8. **Framework vs Library**

In programming, the distinction between a framework and a library lies in their control flow and the level of abstraction they provide. A library is a collection of reusable functions or classes that a developer can call upon for specific functionality. It's like a toolset; you choose when and where to use its tools. The developer is in control, calling the library's functions whenever they need them in their code. On the other hand, a framework provides a skeleton or blueprint for applications. It dictates the architecture of your project: you fill in the details but follow its structure and rules. In a framework, the control flow is inverted – it calls your code, not the other way around. This is often referred to as the "Hollywood Principle": "Don't call us, we'll call you." Frameworks can enforce a particular way of doing things, guiding the overall design of your project, while libraries offer more flexibility but less guidance.

<img src="https://images2.imgbox.com/8e/88/hZHW5QQb_o.png">

Understanding these terms provides a solid foundation for navigating the landscape of mobile and web application development. They are essential for effective communication within a development team and for understanding the architecture of complex systems. Let me know if you need more detailed explanations on any of these terms or examples!