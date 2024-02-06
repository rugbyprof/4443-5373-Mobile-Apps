from pymongo import MongoClient, ASCENDING, DESCENDING
from rich import print
import re


class MongoDBInterface:
    def __init__(self, db_name=None, collection_name=None):
        # Replace the following with your own details
        username = "candy_user"
        password = "ILoveCandySoMuchIWantToEatYou"
        host = "localhost"
        port = "27017"  # Default MongoDB port
        database_name = "candy_store"
        # Create the connection URL
        connection_url = f"mongodb://{username}:{password}@{host}:{port}/{database_name}?authSource=admin"
        self.client = MongoClient(connection_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get(self, filter_query={}, pagination=None, sort_order=[]):
        """
        Retrieves documents from the collection based on the provided criteria.

        :param filter_query: Dictionary for filtering documents.
        :param pagination: Tuple or dictionary with 'skip' and 'limit' for pagination.
        :param sort_order: List of tuples specifying field and direction to sort by.
        :return: List of documents matching the criteria.
        """

        # Apply filtering
        query_result = self.collection.find(filter_query)

        # Apply sorting
        if sort_order:
            query_result = query_result.sort(sort_order)

        # Apply pagination
        if pagination:
            skip = pagination.get("skip", 0)
            limit = pagination.get(
                "limit", 0
            )  # Consider setting a default limit to avoid retrieving massive datasets
            query_result = query_result.skip(skip).limit(limit)

        return list(query_result)

    def post(self, document):
        # Implement the logic to insert data
        self.collection.insert_one(document)

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


if __name__ == "__main__":
    db = MongoDBInterface("candy_store", "candies")
    result = db.get({"category": "gummy-candy"})
    print(result)
    result = db.get(
        {"category": "gummy-candy"},
        {"skip": 10, "limit": 10},
    )
    print(result)

    result = db.get(
        {
            "category": "gummy-candy",
            "name": {"$regex": re.compile("Sour", re.IGNORECASE)},
        }
    )
    print(result)
