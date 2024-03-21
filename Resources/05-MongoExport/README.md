Exporting a MongoDB database on Ubuntu and importing it into another server can be efficiently done using the `mongodump` and `mongorestore` utilities, which are part of the MongoDB database tools. These utilities allow you to dump your database into a directory of BSON files and then restore it on another server. Here's how you can do it:

### Step 1: Export the Database with mongodump

1. **Open your terminal.**
2. **Navigate to the directory where you want to store the dump.** This is where the `mongodump` utility will save the exported database files.

    ```bash
    cd /path/to/your/desired/directory
    ```

3. **Run the `mongodump` command.** Specify the name of the database you want to export with the `--db` option. If MongoDB is running on a different host or port, you will need to specify those as well.

    ```bash
    mongodump --db your_database_name
    ```
   
    - If MongoDB requires authentication, you'll also need to include the `-u` (username), `-p` (password), and `--authenticationDatabase` options.
    - By default, `mongodump` connects to the MongoDB instance running on `localhost` on port `27017`. If your instance is running elsewhere, use the `--host` and `--port` options to specify the correct connection details.

4. **This command will create a `dump/` directory in your current location,** containing the exported data. The data is stored in BSON format, which is a binary representation of MongoDB's JSON-like documents.

### Step 2: Transfer the Dump to the Other Server

1. **Compress the dump directory** to make the transfer easier and to reduce the file size. You can use `tar` with compression, like so:

    ```bash
    tar -czvf your_database_name_dump.tar.gz dump/
    ```

2. **Transfer the compressed dump file to the other server.** You can use `scp`, `rsync`, or any other file transfer method you prefer. Here's an example using `scp`:

    ```bash
    scp your_database_name_dump.tar.gz user@target_server_address:/path/where/you/want/it
    ```

### Step 3: Import the Database with mongorestore on the Other Server

1. **Log in to the other server.**

2. **Navigate to the directory where you transferred the dump file.**

    ```bash
    cd /path/where/you/put/it
    ```

3. **Decompress the dump file.**

    ```bash
    tar -xzvf your_database_name_dump.tar.gz
    ```

4. **Use the `mongorestore` utility to import the database.** Navigate to the directory containing the decompressed dump, and run:

    ```bash
    mongorestore --db your_database_name dump/your_database_name
    ```
   
    - As with `mongodump`, if your MongoDB requires authentication, or if it's running on a non-default host or port, you'll need to provide the appropriate options (`-u`, `-p`, `--authenticationDatabase`, `--host`, `--port`).
    - If you're restoring to a database that already exists and want to replace its contents with the dump, you might need to use the `--drop` option. This will drop each collection from the target database before restoring them from the dump.

By following these steps, you should be able to export a MongoDB database from one Ubuntu server and import it into another server seamlessly.