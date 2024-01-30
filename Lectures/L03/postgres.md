Installing PostgreSQL on Ubuntu and making sure it's only accessible from localhost is quite simple. By default, PostgreSQL listens on localhost (`127.0.0.1`), which restricts its access to the local machine. Here's a step-by-step guide to get you set up:

## Steps to Install

### 1. Update Local Package Index
Start by updating your package list to make sure you have access to the latest versions of the packages:

```bash
sudo apt update
```

### 2. Install PostgreSQL
Install PostgreSQL along with the `-contrib` package, which adds some additional utilities and functionality:

```bash
sudo apt install postgresql postgresql-contrib
```

### 3. Start and Enable PostgreSQL Service
Once the installation is complete, the PostgreSQL service should start automatically. You can check its status with:

```bash
sudo systemctl status postgresql
```

If for some reason it's not running, you can start it with:

```bash
sudo systemctl start postgresql
```

To ensure PostgreSQL starts up every time your machine boots, enable it with:

```bash
sudo systemctl enable postgresql
```

### 4. Verify Installation
You can verify that PostgreSQL is running and accessible by switching to the default `postgres` user and launching the PostgreSQL command-line interface:

```bash
sudo -i -u postgres
psql
```

This should log you into the PostgreSQL interface. You can exit out of it with `\q`.

### Ensuring Localhost Access Only
PostgreSQL is configured by default to listen on `localhost`. To verify or change this, you can edit the `postgresql.conf` file:

```bash
sudo nano /etc/postgresql/<version>/main/postgresql.conf
```

Make sure to replace `<version>` with the version of PostgreSQL you've installed. Look for the `listen_addresses` line and ensure it's set to `localhost` or `127.0.0.1`:

```
listen_addresses = 'localhost'
```

If you make changes, remember to restart the PostgreSQL service for them to take effect:

```bash
sudo systemctl restart postgresql
```

### 5. Configuring PostgreSQL Users and Databases
By default, PostgreSQL creates a new system user named `postgres` that is associated with the default `postgres` database role. To create a new database and role, you can use the following commands:

First, switch to the `postgres` user:

```bash
sudo -i -u postgres
```

Then, you can create a new role. Replace `myrole` with your desired role name:

```bash
createuser --interactive
```

And create a new database. Replace `mydatabase` with your desired database name:

```bash
createdb mydatabase
```

To access the PostgreSQL prompt with the new role, you can type:

```bash
psql -d mydatabase -U myrole
```

### 6. Additional Security (Optional)
If you want to further secure your PostgreSQL installation, consider:

- Changing the default password for the `postgres` user within the PostgreSQL prompt:

  ```sql
  \password postgres
  ```

- Reviewing and possibly tightening the `pg_hba.conf` file settings, which control client authentication:

  ```bash
  sudo nano /etc/postgresql/<version>/main/pg_hba.conf
  ```

  Ensure that the settings for local connections are set to `peer` or `md5` for IPv4 and IPv6 local connections.

## Postgres Web Admin


### phpPgAdmin

**phpPgAdmin** is a web-based administration tool for PostgreSQL. It allows you to perform tasks such as creating databases, managing tables, executing SQL queries, and much more, all from a web interface.

#### Installing phpPgAdmin on Ubuntu:

1. **Install Apache and PHP:**
   First, ensure that Apache and PHP are installed. phpPgAdmin is written in PHP, so your server must have PHP installed to run it.

   ```bash
   sudo apt update
   sudo apt install apache2 php libapache2-mod-php
   ```

2. **Install PostgreSQL:**
   If PostgreSQL isn't installed yet, you can install it using:

   ```bash
   sudo apt install postgresql postgresql-contrib
   ```

3. **Install phpPgAdmin:**
   You can install phpPgAdmin directly from the default Ubuntu repositories:

   ```bash
   sudo apt install phppgadmin
   ```

4. **Configure Apache to Serve phpPgAdmin:**
   You might need to configure Apache to properly serve phpPgAdmin. This typically involves linking the phpPgAdmin configuration file into Apache's `conf-enabled` directory and possibly adjusting the Apache configuration to allow `.htaccess` overrides.

   - Link phpPgAdmin to Apache:

     ```bash
     sudo ln -s /etc/phppgadmin/apache.conf /etc/apache2/conf-available/phppgadmin.conf
     sudo a2enconf phppgadmin
     ```

   - Allow `.htaccess` Overrides by editing Apache's main configuration file or the virtual host file for your site and setting `AllowOverride All` within the `<Directory>` section for your web root or the phpPgAdmin directory.

5. **Restart Apache:**
   After making these changes, you'll need to restart Apache to apply them:

   ```bash
   sudo systemctl restart apache2
   ```

6. **Access phpPgAdmin:**
   Once everything is set up, you can access phpPgAdmin through your web browser by navigating to `http://localhost/phppgadmin`. From here, you can log in using your PostgreSQL credentials and start managing your databases.

### Security Note:
When installing web-based database management tools like phpPgAdmin, it's crucial to ensure they are securely configured, especially if they're accessible from the internet. Consider using `.htaccess` rules to limit access to localhost or specific IP addresses, employing SSL/TLS to encrypt connections, and using strong passwords.


## VSCode Access

### For PostgreSQL:

1. Connect to your server via the SSH plugin in VScode. 

2. Install **PostgreSQL Extension** for VS Code:
   - **Name**: PostgreSQL for Visual Studio Code
   - **Publisher**: Microsoft

   This extension allows you to connect to PostgreSQL databases, run queries, and even manage your database objects directly within VS Code.

   #### How to Use:
   - **Install the Extension**: Search for "PostgreSQL" in the Extensions view (`Ctrl+Shift+X`) and install the PostgreSQL extension by Microsoft.
   - **Connect to Database**: After installation, you can add a new connection by clicking on the "Add Connection" icon in the PostgreSQL explorer view. You'll need to provide your connection details (hostname, port, username, and password).
   - **Query and Manage**: Once connected, you can browse schemas, tables, and run SQL queries directly from the integrated SQL editor.


## Python PostGres

To create a PostgreSQL database and a table schema based on the provided document using Python, you can use the `psycopg2` library, which is a popular PostgreSQL adapter for Python. If you haven't installed `psycopg2`, you can do so by running `pip install psycopg2-binary` in your terminal.

Below is a Python script that demonstrates how to connect to a PostgreSQL server, create a new database, and then define a table with a schema that matches the structure of your provided document:

```python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Database connection parameters
host = 'localhost'
user = 'your_username'
password = 'your_password'

# Connect to the default database (usually 'postgres') to create a new database
conn = psycopg2.connect(host=host, user=user, password=password, dbname='postgres')

# Set the connection to autocommit mode to create a new database
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor object
cur = conn.cursor()

# Name of the new database
new_dbname = 'my_new_database'

# SQL statement to create a new database
create_database_sql = f"CREATE DATABASE {new_dbname};"

# Execute the SQL statement to create a new database
try:
    cur.execute(create_database_sql)
    print(f"Database '{new_dbname}' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print(f"Database '{new_dbname}' already exists.")

# Close the cursor and connection to the default database
cur.close()
conn.close()

# Connect to the newly created database to create a table
conn = psycopg2.connect(host=host, user=user, password=password, dbname=new_dbname)

# Create a cursor object
cur = conn.cursor()

# SQL statement to create a new table with a schema based on the provided document
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE NOT NULL
);
"""

# Execute the SQL statement to create a new table
cur.execute(create_table_sql)
print("Table 'users' created successfully.")

# Commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
```

### Key Points:

- Replace `'your_username'` and `'your_password'` with your actual PostgreSQL username and password.
- The script first connects to the default `postgres` database to issue the `CREATE DATABASE` command. PostgreSQL requires you to connect to an existing database to create a new one.
- The script then connects to the newly created database (`my_new_database`) to create a table named `users`.
- The `users` table schema is designed based on the provided document structure. The `id` field is defined as a `SERIAL` type to auto-increment with each new record, which serves as the primary key.
- The script checks for the existence of the database before attempting to create it to avoid errors if the database already exists.
- Ensure your PostgreSQL server is running, and you have the necessary permissions to create databases and tables.

This script provides a basic example of creating a PostgreSQL database and table using Python. Depending on your specific requirements, you might need to adjust the data types or add additional constraints to the table schema.