## API's - RESTful and Not so Restful
#### Due: N/A

### What is an API?
An API, or Application Programming Interface, is a set of rules and protocols for building and interacting with software applications. APIs enable different software systems to communicate with each other. In the context of web development, an API typically refers to a web-based interface that allows applications to communicate with a server using HTTP requests and responses. Basically this is how most apps get data or information since it's not possible to store everything locally on someones personal device. 

### RESTful API
`REST`, or `Representational State Transfer`, is an architectural style for designing networked applications. A RESTful API is an API that adheres to the principles of REST. It's a way of designing web services that are stateless, using standard HTTP methods like `GET`, `POST`, `PUT`, `DELETE`, etc. RESTful APIs operate on resources (identified by URLs) and use HTTP's methods to perform operations (`CRUD` operations: `Create`, `Read`, `Update`, `Delete`) on these resources.

While simple "remote procedure calls" using `GET` variables (like `http://mydomain.com/search?id=1234&category=book`) are straightforward, RESTful APIs provide a more structured approach, making them more scalable and maintainable, especially for larger applications.

## Introduction to FastAPI

### What is FastAPI?
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints. It's known for its speed and ease of use and has built-in support for data validation, serialization, and asynchronous request handling.

### Key Features:
- **Fast**: One of the fastest frameworks for building APIs in Python, thanks to Starlette for the web parts and Pydantic for the data parts.
- **Type Checking**: Uses Python type hints for data validation and editor support (autocompletion, error checking).
- **Built for REST**: While it supports other methods of communication, it's designed with RESTful principles in mind.

### Running FastAPI with Uvicorn Programmatically

Instead of running Uvicorn from the command line, you can integrate it into your Python script:

```python
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a main function to run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

This code creates a basic FastAPI application and runs it using Uvicorn when the script is executed directly.

## Testing the API with Postman

1. **Install Postman**: First, ensure Postman is installed on your system.
2. **Run Your FastAPI App**: Execute your script to start the FastAPI server.
3. **Create a Request in Postman**: Open Postman and create a new request.
   - Set the method to `GET`.
   - Use the URL `http://127.0.0.1:8000/`.
   - Hit Send to make a request to your FastAPI server.
4. **View the Response**: Check the response returned by your FastAPI application in Postman.

## Data Format

What data format should we use to store our information? A database would scale much easier and also allow us to do complex queries that filter the data quite nicely. But, JSON is also a great place to start since it translates directly into a Python dictionary. 

### Let's Compare 

The choice between JSON data files and an SQLite database can depend on a few factors:

- **JSON Data Files**: These are simple and don't require understanding of databases, making them a good choice for beginners. They're great for small-scale applications or for learning basic CRUD operations.
- **SQLite Database**: Offers a more realistic approach for applications that require data persistence and complex queries. It's a lightweight SQL database, easier for beginners compared to more complex systems like MySQL or PostgreSQL.

Starting with JSON is simpler and more straightforward. Then we can introduce SQLite (or another DB like mongo or PostGres) to provide a more realistic solution.

## Candy Store

Here a fictional description for a candy store that specializes in a wide range of current and nostalgic candies. I will use this information to create our `Fast Api` routes page / documentation. Let's call our candy store: `KidsInVans.fun`

### Fictional Candy Store Description

**Name**: Sweet Nostalgia Candies

**Description**:
Sweet Nostalgia Candies brings you a delightful journey through time with its extensive collection of candies. From the vibrant, trendy flavors of today to the cherished, classic treats of yesteryear, our store is a haven for candy lovers of all ages. Step into a world where every shelf and corner is adorned with jars and boxes filled with colors and tastes that evoke memories and create new ones. Whether you're seeking a rare, retro candy from your childhood or the latest sugary creation, Sweet Nostalgia Candies is your destination. Indulge in our handpicked selection and experience a sweet escape into the world of confectionery wonders!

**Contact Information**:
- **Address**: 101 Candy Lane, Sweetville, SV 12345
- **Phone**: (123) 456-7890
- **Email**: contact@sweetnostalgiacandies.com
- **Website**: www.sweetnostalgiacandies.com

### Potential API Routes for the Candy Store App

Assuming you're developing a backend API for the candy store app, here are some potential routes you might consider:

1. **List All Candies**
   - Endpoint: `/candies`
   - Method: `GET`
   - Description: Retrieve a list of all candies available in the store.

2. **Search Candies**
   - Endpoint: `/candies/search`
   - Method: `GET`
   - Description: Search for candies based on a query string (e.g., name, category, flavor).

3. **Get Candy Details**
   - Endpoint: `/candies/{candy_id}`
   - Method: `GET`
   - Description: Get detailed information about a specific candy.

4. **Add New Candy**
   - Endpoint: `/candies`
   - Method: `POST`
   - Description: Add a new candy to the store's inventory.

5. **Update Candy Information**
   - Endpoint: `/candies/{candy_id}`
   - Method: `PUT`
   - Description: Update information about an existing candy.

6. **Delete Candy**
   - Endpoint: `/candies/{candy_id}`
   - Method: `DELETE`
   - Description: Remove a candy from the store's inventory.

7. **List Categories**
   - Endpoint: `/categories`
   - Method: `GET`
   - Description: Get a list of candy categories (e.g., chocolates, gummies, hard candies).

8. **Promotions and Deals**
   - Endpoint: `/promotions`
   - Method: `GET`
   - Description: Information about current promotions, deals, or discounts.

9. **Store Information**
   - Endpoint: `/store-info`
   - Method: `GET`
   - Description: Basic information about the candy store, including contact details.

10. **User Reviews**
    - Endpoint: `/reviews`
    - Method: `GET`/`POST`
    - Description: Retrieve or submit customer reviews and ratings for the candies.

These routes cover various functionalities you might want for a candy store app, from viewing and managing the candy inventory to handling customer interactions. The app could also include features like user accounts, shopping carts, and order tracking, each requiring additional routes.