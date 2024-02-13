from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import PyMongoError
from rich import print
from rich.console import Console
from rich.traceback import install
import re

# Set up Rich to pretty-print tracebacks
install()


class MongoDBInterface:
    def __init__(self, **kwargs):
        console = Console()

        # Mandatory parameters
        mandatory_params = ["username", "password", "db"]
        missing_params = [param for param in mandatory_params if param not in kwargs]

        if missing_params:
            error_message = (
                f"Mandatory parameter(s) missing: {', '.join(missing_params)}"
            )
            console.print(f"[bold red]Error:[/] [yellow]{error_message}[/]")
            raise ValueError(error_message)

        self.username = kwargs["username"]
        self.password = kwargs["password"]
        self.host = kwargs.get("host", "localhost")
        self.port = kwargs.get("port", "27017")  # Default MongoDB port
        self.db_name = kwargs.get("db", None)
        self.collection_name = kwargs.get("collection", None)

        # Connection String
        # print(f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}?authSource=admin")

        # Create the connection URL
        self.connection_url = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}?authSource=admin"

        # Initialize MongoDB client and select the database and collection
        self.client = MongoClient(self.connection_url)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def __str__(self):
        return f"url: {self.connection_url} coll: {self.collection_name}"

    def dropCollection(self, collection=None):
        if not collection:
            collection = self.collection
        else:
            collection = self.db[collection]

        collection.drop()

    def get(self, **kwargs):
        """
        Retrieves documents from the collection based on the provided criteria.

        :param filter_query: Dictionary for filtering documents.
        :param pagination: Tuple or dictionary with 'skip' and 'limit' for pagination.
        :param sort_order: List of tuples specifying field and direction to sort by.
        :return: List of documents matching the criteria.
        """

        self.query = kwargs.get("query", {})
        self.filter = kwargs.get("filter", {})
        self.skip = kwargs.get("skip", 0)
        self.limit = kwargs.get("limit", 0)
        self.sort_criteria = kwargs.get("sort_criteria", [("_id,1")])

        try:
            results = (
                self.collection.find(self.query, self.filter)
                .sort(self.sort_criteria)
                .skip(self.skip)
                .limit(self.limit)
            )
            resultList = list(results)
            if len(resultList) >= 0:

                kwargs["success"] = True
                kwargs["result_size"] = len(resultList)
                kwargs["data"] = resultList

                return kwargs
        except PyMongoError as e:
            # print(f"An error occurred: {e}")
            kwargs["success"] = False
            kwargs["error"] = e
            return kwargs

    def post(self, document):
        print(type(document))
        # Implement the logic to insert data
        if isinstance(document, dict):
            self.collection.insert_one(document)
        elif isinstance(document, list):
            self.collection.insert_many(document)

        # try:
        #     result = db.your_collection.insert_one({"your_field": "your_value"})
        #     if result.acknowledged:
        #         print(f"Insert successful with ID: {result.inserted_id}")
        #     else:
        #         print("Insert not acknowledged")
        # except PyMongoError as e:
        #     print(f"An error occurred: {e}")

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

    def delete(self, query):
        # Implement the logic to delete data based on the query
        pass


def mongoConnect(**info):
    # Example usage, this will raise and display an error due to missing parameters
    try:
        return MongoDBInterface(**info)
    except ValueError as e:
        pass  # Error message is already handled and displayed by Rich


from rich.console import Console


def check_params_and_show_usage(kwargs):
    console = Console()
    required_params = ["file_name", "base_name", "save_path"]
    missing_params = [param for param in required_params if param not in kwargs]

    if missing_params:
        console.print(
            "[bold red]Error:[/] Missing required parameter(s):",
            ", ".join(missing_params),
            style="yellow",
        )
        console.print("\n[bold]Usage:[/]", style="green")
        console.print(
            "python your_script.py file_name=your_file.jpg base_name=base_name save_path=./path/to/save",
            style="blue",
        )
        return False  # Indicate missing parameters

    return True  # All required parameters are present


if __name__ == "__main__":
    # Process command-line arguments into kwargs...

    if not check_params_and_show_usage(kwargs):
        exit(1)  # Exit if required parameters are missing

    file_name = kwargs["file_name"]
    base_name = kwargs["base_name"]
    save_path = kwargs["save_path"]

    # Continue with your main logic...


if __name__ == "__main__":

    info = {
        "username": "mongomin",
        "password": "horsedonkeyblanketbattery",
        "host": "localhost",
        "port": "27017",
        "db_name": "candy_store",
        "collection_name": "candies",
    }

    db = mongoConnect(**info)

    # doc = {
    #     "id": "44507182999999",
    #     "name": "Luxor Gold Jelly Beans Teenee Beanee - 5lb",
    #     "prod_url": "https://www.candystore.com/products/luxor-licorice-jelly-beans-teenee-beanee",
    #     "img_url": "https://www.candystore.com/cdn/shop/products/luxor-licorice-jelly-beans-teenee-beanee-1q23-wmark_2048x.jpg?v=1677494804",
    #     "price": 200.99,
    #     "desc": "",
    #     "category":"jelly-beans"
    # }

    # db.post(doc)

    # db = MongoDBInterface(**info)
    # print(db)
    # params = {
    #     'query':{"category": "gummy-candy"},
    #     'filter':{"category":1,"name":1,"_id":0},
    #     'skip':0,
    #     'limit':5,
    # }

    # while(1):
    #     result = db.get(**params)
    #     print(result)

    #     if result['result_size'] == 0:
    #         break
    #     params['skip'] += 5
    #     print("="*40)

    # result = db.get(
    #     {"category": "gummy-candy"},
    #     {"skip": 10, "limit": 10},
    # )
    # print(result)

    result = db.get(
        {
            "category": "gummy-candy",
            "name": {"$regex": re.compile("Sour", re.IGNORECASE)},
        }
    )
    print(result)
