## Testing Api Automatically

## Question: 

I would like to write a python script that would run tests on my fastAPI instance. I'm not 100% sure on what to use, but I would like it be simple. For example, I would like to use the `requests` library to access my api, and not a full fledged testing library. My routes are as follows:

1. GET /candies - Get all candies.
2. GET /categories - Get a list of categories.
3. GET /candies/categoory/{category} - Get candies in a specific category.
4. GET /candies/keyword/{keyword} - Get candies with a key word in the description.
5. GET /candies/name/{name} - Get candies with a key word in the name.
6. GET /candies/price/ - Get candies by price range. Uses query params high:float and low:float
7. GET /candy/{id} - Get candy with with a specified ID.
8. GET /image/{id} - Get a candy image.
9. PUT /candy/ - Update a candies information. Uses query parmams. Needs candy ID, key to update, value to update it to.
10. POST /candy/ - Add new candy to the database.
11. DELETE/candy/{id} Delete a candy.

I'm not sure how to automate the process. 

## Answer: 

For a simple approach to test your FastAPI instance using Python's `requests` library, I'll guide you through creating a basic script. This script will execute HTTP requests against your API endpoints and check the responses. This method is straightforward and doesn't require a full-fledged testing framework, but keep in mind it's more of a manual integration test rather than unit tests or more detailed integration tests you might run with libraries designed specifically for testing APIs in Python, like `pytest` and `httpx` with FastAPI's `TestClient`.

First, ensure you have the `requests` library installed:

```sh
pip install requests
```

Then, you can create a Python script, say `test_fastapi.py`, to test your FastAPI application. Below is an example script that covers the endpoints you've described. This script simply makes requests to each endpoint and checks if the HTTP status code is `200` (OK), which indicates a successful response. You can expand these tests to check the response content more thoroughly based on your application's requirements.

```python
import requests

# Base URL of your FastAPI application
BASE_URL = 'http://localhost:8000'

def test_get_candies():
    response = requests.get(f'{BASE_URL}/candies')
    assert response.status_code == 200
    print("GET /candies test passed.")

def test_get_categories():
    response = requests.get(f'{BASE_URL}/categories')
    assert response.status_code == 200
    print("GET /categories test passed.")

def test_get_candies_by_category(category='chocolate'):
    response = requests.get(f'{BASE_URL}/candies/category/{category}')
    assert response.status_code == 200
    print(f"GET /candies/category/{category} test passed.")

def test_get_candies_by_keyword(keyword='sugar'):
    response = requests.get(f'{BASE_URL}/candies/keyword/{keyword}')
    assert response.status_code == 200
    print(f"GET /candies/keyword/{keyword} test passed.")

def test_get_candies_by_name(name='mars'):
    response = requests.get(f'{BASE_URL}/candies/name/{name}')
    assert response.status_code == 200
    print(f"GET /candies/name/{name} test passed.")

def test_get_candies_by_price_range(low=1.0, high=5.0):
    response = requests.get(f'{BASE_URL}/candies/price/', params={'low': low, 'high': high})
    assert response.status_code == 200
    print("GET /candies/price test passed.")

def test_get_candy_by_id(id=1):
    response = requests.get(f'{BASE_URL}/candy/{id}')
    assert response.status_code == 200
    print(f"GET /candy/{id} test passed.")

def test_get_candy_image(id=1):
    response = requests.get(f'{BASE_URL}/image/{id}')
    assert response.status_code == 200
    print(f"GET /image/{id} test passed.")

def test_update_candy():
    candy_id = 1
    key = 'name'
    value = 'New Candy Name'
    response = requests.put(f'{BASE_URL}/candy/', params={'id': candy_id, 'key': key, 'value': value})
    assert response.status_code == 200
    print("PUT /candy/ test passed.")

def test_add_new_candy():
    new_candy = {'name': 'Test Candy', 'category': 'Test Category', 'price': 1.99}
    response = requests.post(f'{BASE_URL}/candy/', json=new_candy)
    assert response.status_code == 200
    print("POST /candy/ test passed.")

def test_delete_candy(id=2):
    response = requests.delete(f'{BASE_URL}/candy/{id}')
    assert response.status_code == 200
    print(f"DELETE /candy/{id} test passed.")

def run_tests():
    test_get_candies()
    test_get_categories()
    # Add other tests here
    # You may want to add a pause or setup/teardown steps for creating/deleting test data
    test_add_new_candy()  # Example: Add a candy to test deletion
    test_delete_candy(id=2)  # Ensure this ID matches the candy added by test_add_new_candy

if __name__ == '__main__':
    run_tests()
```

### Notes:

- You may need to adjust the `BASE_URL` to match your FastAPI server's address and port.
- The `assert` statements are basic checks to see if the HTTP response status is `200`. You might want to add more detailed checks to verify the response data.
- Remember to replace hardcoded values (like category names, keywords, IDs) with your own values.
- I would add a couple of response items as well: 
  - For GET 
    - Count of Items returned.
    - Short sample (first 5 if applicable)
  - PUT
    - Show old and new values ?? (not sure, this may be too much work)
  - DEL
    - Not sure ... Maybe a susequent GET request for this item (using /candy/{id}) and show a result count of 0?