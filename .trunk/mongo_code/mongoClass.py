from pymongo import MongoClient, ASCENDING


class MongoDBInterface:
    def __init__(self, db_name=None, collection_name=None):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name] if db_name else None
        self.collection = (
            self.db[collection_name] if self.db and collection_name else None
        )

    def get(self, filter_query={}, pagination=None, sort_order=[]):
        """
        Retrieves documents from the collection based on the provided criteria.

        :param filter_query: Dictionary for filtering documents.
        :param pagination: Tuple or dictionary with 'skip' and 'limit' for pagination.
        :param sort_order: List of tuples specifying field and direction to sort by.
        :return: List of documents matching the criteria.
        """
        if not self.collection:
            raise ValueError("Collection not set.")

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

    def post(self, data):
        # Implement the logic to insert data
        pass

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


# Example usage:
# mongodb_interface = MongoDBInterface('your_db_name', 'your_collection_name')

if __name__ == "__main__":
    mongodb_interface = MongoDBInterface("candy_store", "candies")
    # Example usage
    # Assuming mongodb_interface is an instance of MongoDBInterface with a selected db and collection
    # Filter: Documents where "age" is greater than 25
    # Pagination: Skip the first 5 documents, limit to the next 10 documents
    # Sort Order: Sort by "name" in ascending order
    documents = mongodb_interface.get(
        filter_query={"age": {"$gt": 25}},
        pagination={"skip": 5, "limit": 10},
        sort_order=[("name", ASCENDING)],
    )

    # Example usage
    # Assuming mongodb_interface is an instance of MongoDBInterface with a selected db and collection
    # Filter Query: Documents where "category" is "gummy-candy"
    # Update Data: Change "in_stock" to True for all matching documents
    # Upsert: False (do not insert a new document if no match is found)
    update_result = mongodb_interface.put(
        filter_query={"category": "gummy-candy"},
        update_data={"in_stock": True},
        upsert=False,
    )
