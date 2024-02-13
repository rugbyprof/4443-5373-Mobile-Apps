## API Route Help

This document has a lot of differing info. We will start with querying MongoDB using FastAPI with PyMongo, but also how an overview on `query` vs `path` parameters and `querying with PyMongo`.

1. `PyMongo queries` to get data from our mongo collection.
2. `Query parameters` within FastApi (e.g. ?id=7474&color=red&size=large)
3. `Path parameters` within FastAPI (e.g. /items/7474/red/large) [not necessarily good]

### Query Params

Query params come after the `?` and use `key=value` pairs to put more than one param on the URL you add the delimiter: `&` between key value pairs. Query params can be optional and have a default value. 

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/candies/") # route identifier
async def get_candies_by_category(category: str = None):
    """
    This route would find all the candies, or 
    Example:
       /candies/?category=jelly_beans
    """
    if category:
        # Perform the PyMongo query to filter by category
        # result = collection.find({"category": category})
        pass
    else:
        # Fetch all candies if no category is specified
        # result = collection.find({})
        pass
    # Return the query result as JSON
    return {"candies": "result goes here"}
```

### Path Params

Path parameters are a bit different; they are part of the URL path. Here's how you can define an endpoint that uses a path parameter. When you use this method the `category` is required and will throw an error if it is not present.

```python
@app.get("/candies/{category}")
async def get_candies_by_category(category: str):
    """
    Example: 
        /candies/jelly_beans/
    """
    # Perform the PyMongo query to fetch a candy by its ID
    # Make sure to handle the conversion from string to ObjectId for MongoDB
    # from bson import ObjectId
    # result = collection.find_one({"_id": ObjectId(candy_id)})
    return {"candy": "result goes here"}
```

Also, path params don't work well with `default` parameter values because this line here: `@app.get("/candies/{category}")` EXPECTS a category!

However, you can create another route with the same name (but no parameter syntax), but it's paired with a method of a different name. Dumb example ... 

```python
@app.get("/candies/")
async def get_candies_by_category_default():
    """ However in this case, we can simply return all the category names instead.

    """
    
```
Wait ... stupid names. The concept is valid, but we need to name things better if we use this technique. Based on the url `/candies/` with zero params (path or query) I would expect all the candies.
There are more examples below explaining the difference between:

1. query params 
2. query params with default values
3. path params
4. path params that need default values

The thing is, we can also combine path params with query params. Which I will discuss in class.

### PyMongo Queries

#### Query by Category:

```python
def fetch_candies_by_category(category):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["your_database_name"]
    collection = db["your_collection_name"]
    if category:
        return list(collection.find({"category": category}, {"_id": 0}))  # Excluding '_id' from results
    else:
        return list(collection.find({}, {"_id": 0}))
```

#### Query by ID:

```python
from bson import ObjectId

def fetch_candy_by_id(candy_id):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["your_database_name"]
    collection = db["your_collection_name"]
    return collection.find_one({"_id": ObjectId(candy_id)}, {"_id": 0})
```

For these PyMongo queries:
- Use `find_one()` for getting a single document by `_id`, which requires converting `candy_id` from a string to an `ObjectId`.
- Use `find()` for retrieving multiple documents. When `category` is not specified, it fetches all documents.
- In both examples, `{"_id": 0}` is passed to exclude the `_id` field from the results. Adjust the projection as needed.


## More Route Examples

Using different candy fields to search with.

### Route 1: Get Candy by ID

This route retrieves a candy document based on its unique `id`.

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/candies/{candy_id}")
async def get_candy_by_id(candy_id: str = Path(..., title="The ID of the candy to retrieve")):
    """
    Retrieve a candy by its unique ID.

    Parameters:
    - `candy_id`: str - The unique identifier for the candy.
    
    Returns:
    - The candy document with the specified ID.
    """
    # PyMongo query to find candy by ID would go here
    pass
```

### Route 2: Get Candies by Category

This route lists all candies within a given `category`. Note that categories are likely to have more than one candy, so this route might return multiple documents.

```python
@app.get("/candies/category/{category_name}")
async def get_candies_by_category(category_name: str = Path(..., title="The category of candies to retrieve")):
    """
    Retrieve all candies in a specific category.

    Parameters:
    - `category_name`: str - The name of the category.
    
    Returns:
    - A list of candy documents within the specified category.
    """
    # PyMongo query to find candies by category would go here
    pass
```

### Route 3: Get Candy by Name

This route finds a candy by its `name`. Since candy names might not be unique, this could potentially return multiple documents.

```python
@app.get("/candies/name/{candy_name}")
async def get_candy_by_name(candy_name: str = Path(..., title="The name of the candy to retrieve")):
    """
    Retrieve a candy (or candies) by its name.

    Parameters:
    - `candy_name`: str - The name of the candy.
    
    Returns:
    - A candy document (or documents) with the specified name.
    """
    # PyMongo query to find candy by name would go here
    pass
```

### Note on Default Parameters with Path Params:

In FastAPI, path parameters are assumed to be required by default since they are part of the URL's path. Therefore, specifying a default value for a path parameter (in a way that it becomes optional) is not straightforward and typically goes against RESTful design principles. If you need optional parameters, consider using query parameters instead.

### Path Function


The `Path()` function in the FastAPI function definitions is used to provide additional metadata and validation for path parameters in your routes. Path parameters are part of the URL path, and FastAPI uses them to capture specific values from the path. The `Path()` function allows you to define extra information about these parameters, such as their type, default values, title, description, and constraints like minimum or maximum lengths.

In the context of the above function stubs, `Path()` is used to enforce that the path parameter is required (which is the default behavior for path parameters in FastAPI) and to provide a more descriptive title for the OpenAPI documentation generated by FastAPI. Here's a breakdown of how it's used:

```python
candy_id: str = Path(..., title="The ID of the candy to retrieve")
```

- `candy_id: str` declares the path parameter `candy_id` and specifies its type as `str` (string).
- `Path(...)` is the default value for this parameter, using `...` (an Ellipsis) to indicate that the parameter is required and not optional.
- `title="The ID of the candy to retrieve"` provides a human-readable title for the documentation, making the API more understandable.

Using `Path()`, you can also specify other validations and metadata, such as:

- `description`: A string providing more details about the parameter.
- `min_length` and `max_length`: Integer values specifying the minimum and maximum length for the parameter value.
- `regex`: A string defining a regular expression that the parameter value must match.

Here's an example showing some of these additional features:

```python
@app.get("/candies/{candy_id}")
async def get_candy_by_id(candy_id: str = Path(..., title="The ID of the candy to retrieve", description="A unique identifier for each candy in the database", min_length=10, regex="^[a-zA-Z0-9_-]+$")):
    ...
```

In this example, the `candy_id` must be at least 10 characters long and match the specified regex pattern, which allows alphanumeric characters, underscores, and hyphens. These additional validations help ensure that the API receives well-formed and expected data, improving reliability and security.

## Pydantic Models

Using Pydantic with FastAPI is highly recommended. Just go read some of the documentation for FastAP
I. Pydantic is: *a data validation and settings management library that uses Python type annotations.* FastAPI leverages Pydantic models to define data structures, validate incoming data, and serialize outgoing data. This integration makes it easier to ensure that your data conforms to the expected structure and types, improving the reliability and maintainability of your application.

Here's an example of a Pydantic model that defines our candy:

```python
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

class Candy(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    candy_id: str = Field(..., title="Candy ID")
    name: str = Field(..., title="Name of the Candy")
    prod_url: HttpUrl = Field(..., title="Product URL")
    img_url: HttpUrl = Field(..., title="Image URL")
    price: float = Field(..., title="Price")
    desc: Optional[str] = Field(None, title="Description")
    category: str = Field(..., title="Category")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "candy_id": "42690186051771",
                "name": "Unwrapped Twizzlers Strawberry Licorice - 5lb Bulk",
                "prod_url": "https://www.candystore.com/products/twizzlers-unwrapped-strawberry-licorice",
                "img_url": "https://www.candystore.com/cdn/shop/products/Twizzlers-Unwrapped-Strawberry-Licorice-5lb-CandyStore-com-961_2048x.jpg?v=1677183883",
                "price": 21.99,
                "desc": "Twizzlers Unwrapped Strawberry Licorice - 5lb",
                "category": "licorice-candy"
            }
        }
```

### Key Components:

- **`PyObjectId`**: This class is a custom type to handle MongoDB's `ObjectId` fields. It provides validators to ensure incoming `_id` fields are valid `ObjectId` instances and configures Pydantic to treat them as strings in JSON.

- **`BaseModel`**: Each Pydantic model inherits from `BaseModel`, giving it data validation and serialization capabilities.

- **`Field`**: This function is used to provide additional information about the model's fields, such as validation rules, default values, and metadata for OpenAPI documentation.

- **`HttpUrl`**: A Pydantic type that ensures URLs are valid.

- **`Optional`**: Indicates that a field is not required. For fields that might not be included in all documents, such as `desc`, use `Optional`.

- **`Config`**: The inner class where you can provide configuration for the model. Here, it's used to allow arbitrary types (`arbitrary_types_allowed = True`), specify custom JSON encoders (making `ObjectId` serializable as a string), and provide an example structure that helps with API documentation.

Using Pydantic models like this one not only helps with validating and serializing data but also enhances the API documentation and developer experience when using tools like Swagger UI, which FastAPI generates automatically based on Pydantic models and route definitions in the API.


## More Routes

I asked chatGPT if they could create four routes that all did the same thing, but using each of the four "patterns" for lack of a better term: 1) query params 2) query params w/ default params 3) path params 4) path params with an extra route for default values.

It seems like a dumb question, but I really wanted to know how "stuck" you may get when trying to choose your own style of creating routes. I'll discuss that after the next section dealing with the four categories of routes.

### Chat Gpt Response

Creating a single query type that fits all four examples you described (query parameters with and without default values, and path parameters with and without default values) is a bit challenging because FastAPI path parameters are inherently required as part of the URL's structure. However, we can design a flexible API endpoint that can illustrate these concepts using the candy data. A common approach is to use a filter that can optionally accept multiple parameters, like `category` and `price`.

For this example, let's consider a route named `/candies/filter` that can filter candies based on `category` and a `max_price`. This setup will allow us to demonstrate the use of both query parameters and path parameters in different scenarios.

### 1. Query Parameter Route with Passed Values

This route uses query parameters to filter candies by `category` and `max_price`. Both parameters are optional, but if provided, they will filter the candies accordingly.

```python
from typing import Optional

@app.get("/candies/filter")
async def filter_candies(category: Optional[str] = None, max_price: Optional[float] = None):
    """
    Filter candies based on category and max price.
    Both parameters are optional.

    Parameters:
    - `category`: str - Category to filter by (optional).
    - `max_price`: float - Maximum price of candy (optional).
    """
    pass  # Implementation goes here
```

### 2. Query Parameter Route with Default Values

This route is similar to the first one but includes default values for both `category` and `max_price`.

```python
@app.get("/candies/filter/default")
async def filter_candies_default(category: str = "gummy-candy", max_price: float = 10.0):
    """
    Filter candies with default values for category and max price.
    
    Parameters:
    - `category`: str - Category to filter by, default is "gummy-candy".
    - `max_price`: float - Maximum price of candy, default is 10.0.
    """
    pass  # Implementation goes here
```

### 3. Path Parameter Route

This route uses a path parameter for `category` and demonstrates filtering by category. Path parameters are always required, so there's no direct way to set a default value within the route definition.

```python
@app.get("/candies/filter/{category}")
async def filter_candies_by_category(category: str):
    """
    Filter candies by category using a path parameter.
    
    Parameters:
    - `category`: str - Category to filter by.
    """
    pass  # Implementation goes here
```

### 4. Path Parameter Route with a "Default" Handling

While we can't define a default value for path parameters, we can create a separate route that acts as a default by not specifying the category in the path, and internally setting a default category to filter by.

```python
@app.get("/candies/filter/default_category")
async def filter_candies_default_category():
    """
    Filter candies by a default category without specifying it in the path.
    The default category is set internally.
    """
    default_category = "gummy-candy"
    pass  # Use default_category in your implementation
```

For this setup, each route has a distinct purpose but revolves around the same base functionality of filtering candies. It's essential to note that the last route (`filter_candies_default_category`) is a workaround to demonstrate how you might handle a scenario where you want a path-like parameter to have a default behavior without explicitly passing it in the URL.

### Thoughts

I discovered (years ago) that if you try and stick with a single pattern, you will always find instances that don't fit. So `Path Params` vs `Query Params`? Who wins? They both do!! Path params are great for broad queries that line up with fields in your mongo documents, or columns in a database. But when you need to get a little specific, then you can add `Query Params` to a route defined with path parameters. We will come up with examples during discussion in class.