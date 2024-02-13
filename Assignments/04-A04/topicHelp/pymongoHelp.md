## Authentication

When you're facing connection issues with PyMongo using a connection string, while the command line `mongosh` works fine, it usually points to a discrepancy or typo in the connection string or the way the client is initialized in your Python code.

Based on the information you've provided, your PyMongo connection string looks generally correct. However, there are a couple of common issues that might cause trouble:

1. **URI Encoding**: Special characters in the username or password need to be percent-encoded in the URI. In your case, the password `ILoveCandySoMuchIWantToEatYou` doesn't contain any special characters that require encoding, so this shouldn't be an issue. However, it's something to keep in mind if your credentials change.

2. **Authentication Database**: In your `mongosh` command, you're specifying `--authenticationDatabase admin`. This parameter is crucial if your user is not created in the database you're trying to access but in another one (typically the `admin` database). In your PyMongo connection string, the authentication database is not explicitly specified, which might be the cause of the issue.

3. **Database in Connection String**: Your PyMongo URI includes `/candy_store` at the end, which PyMongo will attempt to use as the default database. Ensure that the user `candy_user` has the necessary permissions for this database, and that this is indeed the database you intend to work with.

To address the potential issue with the authentication database, you can modify your PyMongo URI to explicitly specify the authentication database, similar to your `mongosh` command:

```python
url = "mongodb://candy_user:ILoveCandySoMuchIWantToEatYou@localhost:27017/candy_store?authSource=admin"
```

In this revised URI:
- `?authSource=admin` is added to the end of the connection string to explicitly specify the authentication database, which is common practice when the user is defined in the `admin` database but needs access to another database.

Make sure your PyMongo client is using this updated URI when establishing the connection. Here's a simple example of how to use the connection string with PyMongo:

```python
from pymongo import MongoClient

url = "mongodb://candy_user:ILoveCandySoMuchIWantToEatYou@localhost:27017/candy_store?authSource=admin"
client = MongoClient(url)

# Test the connection
db = client['candy_store']
print(db.list_collection_names())
```

This code attempts to connect to the `candy_store` database and lists the collection names, which serves as a simple test to verify the connection.

If you've checked all of the above and the issue persists, consider the following additional troubleshooting steps:
- Double-check the username and password for typos.
- Ensure the MongoDB server is configured to accept connections from your application's host.
- Verify that MongoDB is running on the expected port (`27017` is the default, but it might be different in your setup).
- Review MongoDB server logs for any authentication errors or hints on what might be going wrong.

## Exception Handling

In PyMongo, determining the success of a query can depend on the type of operation you're performing. Unlike some databases that return a success or failure status directly, MongoDB operations typically succeed unless an exception is raised. Here's how you can handle different scenarios:

### For Read Operations (`find`, `find_one`, etc.)

- **Success**: If the query executes without raising an exception, it's considered successful. However, a successful execution does not guarantee that documents are found; it only means the query was valid and executed. For `find`, you'll get a cursor, and for `find_one`, you'll either get a document or `None`.
- **Checking for Results**: To check if a `find` query returned documents, you can iterate over the cursor or convert it to a list and check its length. For `find_one`, you simply check if the result is `None`.
- **Exceptions**: If there's a problem with the query, such as a syntax error or a connectivity issue, PyMongo will raise an exception like `pymongo.errors.PyMongoError`.

### For Write Operations (`insert_one`, `update_one`, `delete_one`, etc.)

- **Success**: These methods return a result object (like `InsertOneResult`, `UpdateResult`, `DeleteResult`). You can check the `acknowledged` attribute of this result to see if the operation was acknowledged by the server. For update and delete operations, you can also check the `matched_count` and `modified_count` to see if any documents were affected.
- **Exceptions**: As with read operations, any issues will raise an exception.

### Example Handling

Here's how you might handle a simple find and insert operation:

```python
from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = MongoClient('mongodb://localhost:27017/')
db = client.your_database

# Read operation
try:
    results = db.your_collection.find({"your_field": "your_value"})
    if results.count() > 0:
        for result in results:
            print(result)
    else:
        print("No documents found")
except PyMongoError as e:
    print(f"An error occurred: {e}")

# Write operation
try:
    result = db.your_collection.insert_one({"your_field": "your_value"})
    if result.acknowledged:
        print(f"Insert successful with ID: {result.inserted_id}")
    else:
        print("Insert not acknowledged")
except PyMongoError as e:
    print(f"An error occurred: {e}")
```

### Important Notes

- Always use try-except blocks to catch exceptions that may be raised due to connectivity issues, configuration errors, or invalid queries.
- Check the documentation of the specific PyMongo method you're using to understand what result object it returns and what attributes you can check to confirm the operation's outcome.
- Remember that an empty result set from a `find` operation does not indicate a failure; it simply means no documents matched the query criteria.

## Pagination

Applying `skip` and `limit` in PyMongo queries is quite straightforward and follows the same logic as in MongoDB queries, but the syntax is adapted for Python. These methods are part of the cursor that's returned by a query, allowing you to control the pagination of your results. Handling exceptions is a separate concern that wraps around the database operation to catch any errors that might occur during the query execution, including issues with `skip` or `limit` parameters.

Here's an example of how to use `skip` and `limit` in a PyMongo query, along with exception handling:

```python
from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

try:
    # Adjust the filter, skip, and limit values as needed
    filter = {"category": "gummy-candy"}
    skip_amount = 10  # Number of documents to skip
    limit_amount = 5  # Maximum number of documents to return

    # Applying filter, skip, and limit
    results = collection.find(filter).skip(skip_amount).limit(limit_amount)

    # Iterating through the results
    for document in results:
        print(document)

except PyMongoError as e:
    # Handle any errors that occur during the query
    print(f"An error occurred: {e}")
```

### Key Points:

- **`skip(skip_amount)`**: This method skips the first `n` documents of the result set, where `n` is the value you pass to `skip`. It's useful for pagination, where you want to start displaying results from a certain point.

- **`limit(limit_amount)`**: Limits the number of documents returned by the query to the specified amount, making it useful for controlling the size of your result set, especially for large collections.

- **Exception Handling**: The `try-except` block catches exceptions of type `PyMongoError`, which is a base class for most PyMongo exceptions. This block will catch and handle errors related to the database connection, query execution, and more.

- **Cursor Iteration**: After applying `skip` and `limit`, you iterate over the cursor to access the query results. Cursors in PyMongo are lazy, meaning the query isn't actually executed until you start iterating over the cursor.

### Note on `count()`:
Regarding your attempt to use `results.count()`, it's worth noting that the `count()` method on cursors is deprecated in PyMongo. If you need to count the documents that match your query, you should use the `count_documents()` method on the collection instead:

```python
count = collection.count_documents(filter)
```

This method takes the same filter you use for your query and returns the count of documents matching the filter, without considering the `skip` and `limit` that may be applied to a cursor.

When working with `skip`, `limit`, and exception handling in PyMongo, it's essential to consider the impact on performance and error management in your application, especially when dealing with large datasets or complex queries.

-----

Yes, applying a default sort in PyMongo works similarly to applying `skip` and `limit`, and you can indeed chain it together with the `.find()` method. The default sorting behavior in MongoDB, when no sort is specified, is based on the natural order of documents in the collection, which is generally the order of insertion but is not guaranteed to be consistent across different MongoDB deployments.

To create a "default sort" in PyMongo, you can define a sort order that will be applied every time you query the database unless specified otherwise by a user parameter. For example, you might choose to sort documents by a specific field like `_id` in ascending order, which often approximates insertion order since MongoDB's ObjectId values are increasing over time.

Here's how you can set up a default sort in your queries:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

# Default sort parameter
default_sort_field = "_id"
default_sort_order = 1  # 1 for ascending, -1 for descending

# Function to perform a query with a default sort
def query_with_default_sort(filter, sort_field=default_sort_field, sort_order=default_sort_order):
    try:
        # Applying filter and default sort
        results = collection.find(filter).sort(sort_field, sort_order)

        # Iterating through the results
        for document in results:
            print(document)

    except Exception as e:
        # Handle any errors that occur during the query
        print(f"An error occurred: {e}")

# Example usage
filter = {"category": "gummy-candy"}
query_with_default_sort(filter)
```

### Customizing the Sort Order:

If you have a user parameter that specifies a different sort order, you can modify the function to accept this parameter and apply it instead of the default sort. Here's an example modification to allow custom sorting:

```python
def query_with_custom_sort(filter, custom_sort=None):
    try:
        if custom_sort is None:
            # Apply default sort if no custom sort is provided
            results = collection.find(filter).sort(default_sort_field, default_sort_order)
        else:
            # Apply custom sort
            results = collection.find(filter).sort(custom_sort)

        for document in results:
            print(document)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with custom sort
custom_sort = [("name", 1)]  # Sort by 'name' field in ascending order
query_with_custom_sort(filter, custom_sort)
```

In this function, `custom_sort` is expected to be a list of (key, direction) pairs, just like the argument to `.sort()` in PyMongo. This setup allows you to keep the `.sort()` in the chain after `.find()`, providing a default behavior that can be easily overridden with custom parameters as needed.

When you sort on multiple fields, MongoDB sorts the documents based on the first field specified in your sort query. For documents that have the same value in the first field, MongoDB then sorts them according to the second field specified, and so on. This allows for quite nuanced sorting behaviors based on multiple criteria.

In PyMongo, you can specify multiple fields to sort by using a list of tuples, where each tuple contains the field name and the direction of the sort (1 for ascending, -1 for descending). Here’s how you can do it:

```python
from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Select the database
db = client["your_database_name"]

# Select the collection
collection = db["your_collection_name"]

# Define your sort criteria
sort_criteria = [("field1", 1), ("field2", -1)]

# Perform a query with sorting on multiple fields
results = collection.find().sort(sort_criteria)

# Iterate through the sorted documents
for document in results:
    print(document)
```

In this example, documents will be sorted first by `"field1"` in ascending order. If there are multiple documents with the same value for `"field1"`, those documents will then be sorted by `"field2"` in descending order.

This feature is particularly useful when you need to organize data in a way that prioritizes one attribute over another, like sorting blog posts by date and then by the number of comments if multiple posts have the same date.