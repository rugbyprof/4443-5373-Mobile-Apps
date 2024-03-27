from rich import print
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install
from rich.traceback import install
import json
import logging
import pymysql
import pymysql.cursors
from pymysql.err import OperationalError


# Database connection parameters
with open("/home/griffin/candyApi/.config.json") as f:
    data = json.load(f)
    db_config = data["db_config"]
db_config["cursorclass"] = pymysql.cursors.DictCursor

# Setup logging
logging.basicConfig(
    level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

logger = logging.getLogger("fastapi")  # Create logger instance

# Customize traceback
install(show_locals=True)  # Show local variables in tracebacks using rich


# Database interaction class
class MysqlDb:
    def __init__(self, **config):
        if not config:
            config = db_config
        self.config = config

    def build_response(self, response, query, data=None):
        """Builds a response dictionary for database queries."""
        return {
            "success": True if response >= 1 else False,
            "query": query,
            "Rows Affected": response,
            "data": data,
        }

    def get_connection(self):
        return pymysql.connect(**self.config)

    def get_connected(self):

        try:
            # Attempt to establish a connection
            connection = pymysql.connect(**self.config)

            # Create a cursor object
            cursor = connection.cursor()

            # Execute a simple SQL query (e.g., select version of the database)
            cursor.execute("SELECT VERSION()")
            cursor.execute("SHOW TABLES")

            # Fetch one result
            version = cursor.fetchall()
            for v in version:
                print(v)

            # Close the cursor and connection
            cursor.close()
            # connection.close()

            # print("Database connection was successful.")
            return connection
        except OperationalError as e:
            print(f"Error: {e}")
            print("Database connection failed.")

    def run_query(self, query, commit=False):
        print("running query: {query}")
        connection = self.get_connection()
        data = None
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                response = cursor.rowcount
                if "select" in query.lower() or "show" in query.lower():
                    data = cursor.fetchall()
                if commit:
                    connection.commit()
                return self.build_response(response, query, data)
        finally:
            connection.close()

    def fetch_all(self, table):
        query = f"SELECT * FROM {table};"
        connection = self.get_connected()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()

    def fetch_one(self, table):
        query = f"SELECT * FROM {table};"
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()

    def fetch_by_id(self, table, key, record_id):
        query = f"SELECT * FROM {table} WHERE {key} = {record_id};"
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                return result
        finally:
            connection.close()

    def exists(self, table, key, value):
        print(f"{table} {key} {value}")
        query = f"SELECT * FROM `{table}` WHERE `{key}` LIKE '{value}';"
        print(query)
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.rowcount > 0
        finally:
            connection.close()

    def get_columns(self, table, field_types=False):
        type_map = {
            "text": "str",
            "var": "str",
            "int": "int",
            "float": "float",
            "double": "float",
            "decimal": "float",
            "json": "json",
        }
        lookup = list(type_map.keys())
        query = f"SHOW COLUMNS FROM {table};"
        connection = self.get_connection()
        try:
            d = {}
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    if field_types:
                        for k in lookup:
                            if k in row["Type"]:
                                d[row["Field"]] = type_map[k]
                    else:
                        d[row["Field"]] = row["Type"]

            return d
        finally:
            connection.close()

    def post_data(self, table, data, acceptable_keys):
        """
        Inserts data into the specified table.

        Parameters:
        - table (str): The table name.
        - data (dict): A dictionary where keys are column names and values are the data to insert.
        """
        if not data:
            logger.error("No data provided in post data!")
            return "No data provided", False

        columns = "`, `".join(data.keys())
        values = "', '".join(str(value) for value in data.values())
        # values = "', '".join(data.values())

        print(f"Columns:\n {columns}")
        print(f"Values:\n {values}")

        # values = list(data.values())
        # val_params = ""
        # for val in values:
        #     val_params += f"'{val}',"
        # val_params = val_params[:-1]

        query = f"INSERT INTO {table} ({columns}) VALUES ({values});"
        print(f"Query: {query}")

        # connection = self.get_connection()
        # try:
        #     with connection.cursor() as cursor:
        #         cursor.execute(query)
        #         connection.commit()
        #         return {
        #             "success": True,
        #             "query": query,
        #             "Rows Affected": cursor.rowcount,
        #         }
        # except pymysql.Error as e:
        #     return f"An error occurred: {e}", False
        # finally:
        #     connection.close()

    def get_max_id(self, table, idFieldKey="id"):
        """
        Fetches the maximum ID from the specified table.

        Parameters:
        - table (str): The table name.

        Returns:
        - int: The maximum ID found in the table. Returns 0 if the table is empty.
        """

        query = f"SELECT MAX({idFieldKey}) AS max_id FROM {table};"
        print(query)
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                if result["max_id"] is not None:
                    return result["max_id"]
                else:
                    return 0
        except pymysql.Error as e:
            print(f"An error occurred while fetching the max ID: {e}")
            return None
        finally:
            connection.close()


if __name__ == "__main__":
    db = MysqlDb(**db_config)
    # print(conn.fetch_all("Album"))
    # print(conn.get_max_id("Album", "AlbumId") + 1)

    candy = {
        "candy_id": "606",
        "old_id": "42688354451643",
        "name": "Smile Pops 3 - 60ct",
        "prod_url": "https://www.candystore.com/products/smile-pops-3-inch",
        "img_url": "https://www.candystore.com/cdn/shop/products/Smile-Pops-3-60ct-CandyStore-com-525_2048x.jpg?v=1677174824",
        "price": 217.99,
        "description": "You won't be able to wipe that smile off of your face once to take a peek at your Smile Pops! That's because these retro inspired 3-inch Smile Pops boast a huge grin that will make your cheeks hurt if you try to match it. If you're having a groovy get together with friends or are hosting a 70's themed party, bring some of these smiley suckers home and watch everyone trip out over their far out cuteness and delicious sugary flavor. All you'll need to complement these smiling treats are some killer bell bottoms and wavy hairdos!",
        "category_ids": ["34"],
        "img_path": "./images/retro/42688354451643.jpg",
        "image_paths": [
            "./images_sized/retro/606_64.jpg",
            "./images_sized/retro/606_96.jpg",
            "./images_sized/retro/606_128.jpg",
            "./images_sized/retro/606_256.jpg",
            "./images_sized/retro/606_512.jpg",
            "./images_sized/retro/606_768.jpg",
        ],
    }

    # db.post_data("Candy", candy)
    candy_cols = db.get_columns("Candy")
    print(candy_cols)
    cat_cols = db.get_columns("Categories")
    print(cat_cols)
