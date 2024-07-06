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
