# Face Recognition
This Project for Exploration about Face Recognition Lifecycle.
![image](https://github.com/MuhFaridanSutariya/face-recognition/assets/88027268/d9bc4ffc-8291-4bb2-b52a-fcf1321ce69e)

## Project Structure

The directory structure of new project looks like this:

```

│
├── src                                          <- Source code
│   ├── routes                                   <- API route definitions
|      ├── face_routes.py                        <- API routes for face recognition operations
│   ├── config.py                                <- Configuration settings, such as database configuration
│   ├── database.py                              <- Utility scripts for database connections and operations
│   ├── face_recognition_system.py               <- Utility scripts for face recognition logic
│   ├── models.py                                <- Pydantic models for request and response validation

│
├── main.py                                      <- Main Application entry point
│
├── Face_Recognition.postman_collection.json     <- Starter Postman collection for testing APIs
├── create_face_embeddings_table.sql             <- SQL script to create the face_embeddings table
├── .gitignore                                   <- List of files ignored by git
├── requirements.txt                             <- File for installing python dependencies
└── README.md
```

## How to run

### 0. Prerequisites
1. Docker and Docker Compose installed on your machine.
2. Postman or any other API testing tool.

### 1. Clone this repository
To get started, clone this repository onto your local machine. Follow the instructions below:

1. Open a terminal or Command Prompt.
2. Change to the directory where you want to clone the repository.
3. Enter the following command to clone the repository:
   ```bash
   git clone https://github.com/MuhFaridanSutariya/face-recognition.git
   ```
4. Once the cloning process is complete, navigate into the cloned directory using the `cd` command:
   ```bash
   cd face-recognition
   ```

### 2. Build and Run Using Docker Image

1. Open a terminal or Command Prompt.
2. Enter the following command to Build the Docker Image:
   ```bash
   docker-compose build
   ```
3. Once the Building Docker Image process is complete, We can to Run the Docker Image with this command:
   ```bash
   docker-compose up
   ```
This will start both the PostgreSQL and FastAPI containers. The FastAPI application will be accessible at `http://localhost:8000`

### 2. Build and Run Using Manual

1. Open a terminal or Command Prompt.
2. Create a Virtual Environment:
   ```bash
   python -m venv virtualenv_name
   ```
3. Activate the Virtual Environment:
   On Windows:
   ```bash
   virtualenv_name\Scripts\activate
   ```
   On Linux:
   ```bash
   source virtualenv_name/bin/activate
   ```
4. Install CMake with this Tutorial [Click Here](https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f)
5. Install all project requirements:
   ```bash
   pip install -r requirements.txt
   ```
6. You can make new database and then table on PostgreSQL with name `face_embeddings` to store feature extraction from image. to detail you can directly using file at db_init/init.sql
7. Run FastAPI:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
This will start both the PostgreSQL and FastAPI containers. The FastAPI application will be accessible at `http://localhost:8000`

### 3. API Endpoint:

- `GET /api/faces`
   Make a GET request to this endpoint to retrieve a list of all registered face IDs.
   
   <b>Response</b>
   
   - The API will respond with a JSON array containing the face IDs:
   
   `
   [
       "123e4567-e89b-12d3-a456-426614174000",
       "223e4567-e89b-12d3-a456-426614174001"
   ]
   `


- `POST /api/face/register`
   Make a POST request to this endpoint to Registers a new face by uploading an image.

   <b>Request Body</b>
   
   The request body should include the following field:
   
   `file`: The image file containing the face to register.
   
   Example request body (using form-data in Postman):
   
   `file`: type file **select an image file**
   
   <b>Response</b>
   
   - The API will respond with a JSON object containing the face ID:
   
   `
   {
       "face_id": "123e4567-e89b-12d3-a456-426614174000"
   }
   `
  
   - If no face is detected in the image, the response will be:
  
   `
   {
       "detail": "No face detected"
   }
   `
  
- `POST /api/face/recognize`
   Make a POST request to this endpoint to recognize a face by uploading an image.

   <b>Request Body</b>
   
   The request body should include the following field:
   
   `file`: The image file containing the face to register.
   
   Example request body (using form-data in Postman):
   
   `file`: type file **select an image file**
   
   <b>Response</b>
   
   - The API will respond with a JSON object containing the recognized face ID:
   
   `
   {
       "face_id": "123e4567-e89b-12d3-a456-426614174000"
   }
   `
  
   - If no face is detected in the image, the response will be:
  
   `
   {
       "detail": "No face detected"
   }
   `
  
   - If the face is not recognized, the response will be:
  
   `
   {
       "detail": "Face not recognized"
   }
   `



- `DELETE /api/face/{face_id}`
   Make a DELETE request to this endpoint to delete a face by its ID.

   <b>Path Parameter</b>
      
   `face_id`: The ID of the face to delete.
   
   <b>Response</b>
   
   - The API will respond with a JSON object indicating that the face was deleted successfully:
   
   `
   {
       "message": "Success! Face deleted"
   }
  `
  
   - If the face is not found, the response will be:
  
   `
   {
       "detail": "Face not found"
   }
   `
  
   - If the face is not recognized, the response will be:
  
   `
   {
       "detail": "Face not recognized"
   }
   `
#### Postman Collection:
To simplify testing the API, a Postman collection `Face_Recognition.postman_collection.json` is provided. This collection includes predefined requests for all the API endpoints.
How to Use the Postman Collection
1. Import the Collection:
   - Open Postman.
   - Click on the `Import` button.
   - Select the `Face_Recognition.postman_collection.json` file and import it.
2. Run the Requests:
   - The imported collection will appear in your Postman workspace.
   - Expand the collection to see the predefined requests.
   - Click on any request to view and run it.


















   
