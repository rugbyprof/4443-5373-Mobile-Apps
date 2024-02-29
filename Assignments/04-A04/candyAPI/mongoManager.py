from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import PyMongoError
from rich import print
from rich.console import Console
from rich.traceback import install
import re
import sys
from bson.objectid import ObjectId
from bson.errors import InvalidId
import base64
from PIL import Image
import io

def convert_jpg_to_png(jpg_path, png_path):
    # Open the JPG image
    with Image.open(jpg_path) as img:
        # Convert and save as PNG
        img.save(png_path, 'PNG')




def is_valid_object_id(id_str):
    try:
        # Attempt to convert the string to an ObjectId
        obj_id = ObjectId(id_str)
        # If the above line doesn't raise an exception, the id_str is a valid ObjectId
        return True
    except InvalidId:
        # If an InvalidId exception is caught, the id_str is not a valid ObjectId
        return False


# Set up Rich to pretty-print tracebacks
install()


class MongoManager:
    def __init__(self, **kwargs):
        self.console = Console()

        self.username = kwargs.get("username", None)
        self.password = kwargs.get("password", None)
        self.host = kwargs.get("host", "localhost")
        self.port = kwargs.get("port", "27017")  # Default MongoDB port
        self.db = kwargs.get("db", None)
        self.collection = kwargs.get("collection", None)

        if self.username is None and self.password is None:
            self.connection_url = f"mongodb://{self.host}:{self.port}/"
        else:
            # Need to check that a db name was passed in
            # Create the connection URL
            self.connection_url = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}?authSource=admin"

        try:
            self.client = MongoClient(self.connection_url)
            # The ismaster command is cheap and does not require auth.
            self.client.admin.command("ismaster")
        except ConnectionFailure:
            print("Server not available")

        # if a db is specified then make connection
        if self.db is not None:
            self.setDb(self.db)

            # if db is specified then check for collection as well
            if self.collection is not None:
                self.collection = self.db[self.collection]

    def __str__(self):
        return f"url: {self.connection_url} coll: {self.collection_name}"

    def setDb(self, db_name):
        """Sets the current database."""
        if db_name in self.client.list_database_names():
            self.db = self.client[db_name]
            print(f"Database set to {db_name}")
        else:
            print(f"Database {db_name} does not exist. Creating {db_name}.")
            self.db = self.client[db_name]

    def setCollection(self, collection_name):
        """Sets the current collection."""
        if self.db is not None:  # Corrected the check here
            if collection_name in self.db.list_collection_names():
                self.collection = self.db[collection_name]
                print(f"Collection set to {collection_name}")
            else:
                print(
                    f"Collection {collection_name} does not exist. Creating {collection_name}."
                )
                self.collection = self.db[collection_name]
        else:
            print("No database selected. Use set_database() first.")

    def dropCollection(self, collection_name):
        """Deletes a collection from the current database."""
        if self.db is not None:  # Corrected the check here
            if collection_name in self.db.list_collection_names():
                self.db.drop_collection(collection_name)
                print(f"Collection {collection_name} deleted.")
            else:
                print(f"Collection {collection_name} does not exist.")
        else:
            print("No database selected. Use set_database() first.")

    def dropDb(self, db_name):
        """Deletes a database."""
        if db_name in self.client.list_database_names():
            self.client.drop_database(db_name)
            print(f"Database {db_name} deleted.")
            if (
                self.db is not None and self.db.name == db_name
            ):  # Corrected the check here
                self.db = None
                self.collection = None
        else:
            print(f"Database {db_name} does not exist.")

    def get(self, **kwargs):
        """
        Retrieves documents from the collection based on the provided criteria.

        :param filter_query: Dictionary for filtering documents.
        :param pagination: Tuple or dictionary with 'skip' and 'limit' for pagination.
        :param sort_order: List of tuples specifying field and direction to sort by.
        :return: List of documents matching the criteria.
        """

        query = kwargs.get("query", {})
        filter = kwargs.get("filter", {})
        skip = kwargs.get("skip", 0)
        limit = kwargs.get("limit", 0)
        sort_criteria = kwargs.get("sort_criteria", [("_id,1")])

        result_data = {}

        try:
            #results = self.collection.find(query).sort(sort_criteria).skip(skip).limit(limit)
            results = self.collection.find_one(query)
            print(results)
            if len(list(results)) >= 0:
                kwargs["success"] = True
                kwargs["result_size"] = 0
                kwargs["data"] = results

                return kwargs
        except PyMongoError as e:
            # print(f"An error occurred: {e}")
            kwargs["success"] = False
            kwargs["error"] = e
            return kwargs

    def get2(self, **kwargs):
        """
        Retrieves documents from the collection based on the provided criteria.

        :param query: Dictionary for filtering documents using MongoDB query syntax.
        :param skip: Integer specifying the number of documents to skip.
        :param limit: Integer specifying the maximum number of documents to return.
        :param sort_criteria: List of tuples specifying field and direction to sort by.
        :return: Dictionary with the operation's success status, result size, and data.
        """

        query = kwargs.get("query", {})
        skip = kwargs.get("skip", 0)
        limit = kwargs.get("limit", 10)  # Assuming a default limit might be helpful
        sort_criteria = kwargs.get("sort_criteria", [("_id", 1)])  # Fixed the sort criteria syntax

        try:
            results = self.collection.find(query).sort(sort_criteria).skip(skip).limit(limit)
            
            resultList = list(results)
            return {
                "success": True,
                "result_size": len(resultList),
                "data": resultList
            }
        except PyMongoError as e:
            return {
                "success": False,
                "error": str(e)  # It's often a good idea to convert exceptions to strings for readability
            }

    def post(self, document):
        # Implement the logic to insert data
        if isinstance(document, dict):
            self.collection.insert_one(document)
        elif isinstance(document, list):
            self.collection.insert_many(document)


    def put(self, filter_query, update_data, upsert=False):
        """
        Updates documents in the collection based on the provided criteria.

        :param filter_query: Dictionary specifying the criteria to select documents to update.
        :param update_data: Dictionary specifying the update operations to be applied to the documents.
        :param upsert: If True, a new document is inserted if no document matches the filter_query.
        :return: Result of the update operation.
        """
        if not self.collection:
            raise ValueError("Collection not set.")

        # MongoDB requires update operations to be prefixed with operators like '$set', '$unset', etc.
        # Ensure update_data is structured properly or wrap it with '$set' if it's a direct field update.
        if not any(key.startswith("$") for key in update_data.keys()):
            update_data = {"$set": update_data}

        result = self.collection.update_many(filter_query, update_data, upsert=upsert)
        return result

    def put2(self, id_key, id_val, update_key, update_value):
        """
        Updates the price of a specific item in the collection.

        :param item_id: The unique identifier for the item.
        :param new_price: The new price to set.
        :return: Result of the update operation.
        """
        if id_key == '_id' and is_valid_object_id(id_val):
            # Convert string ID to ObjectId
            id_val = ObjectId(id_val)

        # Perform the update
        result = self.collection.update_one(
            {id_key: id_val},  # Query to match the document
            {"$set": {update_key: update_value}}  # Update operation
        )

        # Check if the update was successful
        if result.matched_count > 0:
            return {"success": True, "updated_count": result.modified_count}
        else:
            return {"success": False, "message": "No matching document found."}

    def delete(self, query):
        # Implement the logic to delete data based on the query
        pass

    def store_image_in_mongodb(self,product_id,png_data):

        self.collection.insert_one({"_id":product_id,"image_data": png_data})

    def get_image_from_mongodb(self,image_id):
        print({"_id": int(image_id)})

        image_document = self.collection.find_one({"_id": int(image_id)})

        if image_document:
            return image_document['image_data']  # Assuming the Base64 data is stored under 'image_data'
        return None



if __name__ == "__main__":

    # info = {
    #     "username": "mongomin",
    #     "password": "horsedonkeyblanketbattery",
    #     "host": "localhost",
    #     "port": "27017",
    #     "db_name": "candy_store",
    #     "collection_name": "candies",
    # }

    query = sys.argv[1]

    mm = MongoManager()

    mm.setDb("candy_store")


    if query == '1':
        # Get all categories sorted ascending by name
        mm.setCollection("categories")

        categories = mm.get(sort_criteria=[('name',-1)],filter={"_id":0,"count":1})

        print(categories)
    elif query == '2':
        # Get candies sorted ascending by category and desc by price and filter to only see price, category, and name
        mm.setCollection("candies")

        candies = mm.get(sort_criteria=[('category',1),('price',-1)],filter={'_id':0,'price':1,'category':1})

        print(candies)
    elif query == '3':
        mm.setCollection("candies")
        regex_query = {"name": {"$regex": "crows", "$options": "i"}}  # '$options': 'i' makes it case-insensitive

        sourCandies = mm.get(
            query = regex_query,
            # filter={"_id":0,"name":1},
            sort_criteria=[("name",1)])
        print(sourCandies)
        print(len(sourCandies['data']))
        
    elif query == '4':
        mm.setCollection("candies")
        sourCandies = mm.get(query = {"category_id": 12},filter={'_id':0,'price':1,'category_id':1,'name':1})
        print(sourCandies)
        print(len(sourCandies['data']))

    elif query == '5':
        price_range_query = {
            "price": {"$gte": 100.00, "$lte": 150.00}
        }
        mm.setCollection("candies")
        rangeQuery = mm.get(
            query = price_range_query,
            filter={'_id':0,'price':1,'category_id':1,'name':1},
            sort_criteria={'price':-1}
            )
        print(rangeQuery)
        print(len(rangeQuery['data']))
    elif query == '6':
        # original 49.99
        mm.setCollection("candies")
        print(mm.get(query={'id':'42688432308411'}))
    elif query == '7':
        # original 49.99
        mm.setCollection("candies")
        print(mm.put2('id', '42688432308411', 'price', 9.99))

    elif query == '8':
        # client = MongoClient()
        # db = client['candy_store']
        # collection = db['candies']

        # results = collection.find({'category_id':30},{'_id':0,"name":1,'price':1})
        # print(list(results))

        mm.setCollection("candies")
        for i in range(10):
            result = mm.get(
                sort_criteria=[('name',1)],
                skip=(i * 3), 
                limit=3,
                filter={"_id":0,"name":1})
            print(result)
            print("=" * 30)
    elif query == '9':
        mm.setCollection("candies")
        result = mm.get(
            sort_criteria=[("name",1)],
            filter = {"_id":0,"name":1}
            )
        print(result)
    elif query == '10':
        mm.setCollection('categories')
        doc = { 'count': 23, 'name': 'Dirt Candy' ,'tast':'awesome','color':'pink','price':99999.99}
        mm.post(doc)
