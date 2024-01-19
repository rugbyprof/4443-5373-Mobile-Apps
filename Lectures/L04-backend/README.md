## What is a "Backend"

This overview will give you insight into creating an API using both `Express` (javascript) and `Fast API` (python). 

### Express Backend (Node.js)

1. **Setup**: First, ensure you have Node.js and npm (Node Package Manager) installed.

2. **Create Project**: In a new directory, initialize your Node.js project and install Express.
   ```bash
   npm init -y
   npm install express
   ```

3. **Server Code**: Create a file named `app.js` and paste the following code:

   ```javascript
   const express = require('express');
   const app = express();
   const port = 3000;

   app.get('/example/data', (req, res) => {
       res.json({
           message: "Hello from Express!",
           data: [1, 2, 3, 4, 5]
       });
   });

   app.listen(port, () => {
       console.log(`Server running on http://localhost:${port}`);
   });
   ```

4. **Run the Server**: Execute your server using Node.js.
   ```bash
   node app.js
   ```

5. **Accessing API**: Visit `http://localhost:3000/example/data` in your browser or use a tool like Postman to see the JSON response.

### FastAPI Backend (Python)

1. **Setup**: Make sure you have Python installed. Use a virtual environment for better package management.

2. **Install FastAPI and Uvicorn**: Install FastAPI and Uvicorn, an ASGI server, using pip.
   ```bash
   pip install fastapi uvicorn
   ```

3. **Server Code**: Create a file named `main.py` and add the following code:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/example/data")
   async def read_data():
       return {
           "message": "Hello from FastAPI!",
           "data": [1, 2, 3, 4, 5]
       }
   ```

4. **Run the Server**: Start the FastAPI server using Uvicorn.
   ```bash
   uvicorn main:app --reload
   ```

5. **Accessing API**: The API will be available at `http://localhost:8000/example/data`. You can access it using a browser or a tool like Postman.

Both of these servers will respond to a GET request at the specified endpoint with the example JSON data. The Express server runs on port 3000, and the FastAPI server runs on port 8000. You can test these APIs using tools like Postman, or simply use a web browser. 

