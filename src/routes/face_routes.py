from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from werkzeug.utils import secure_filename
import os
from ..config import UPLOAD_FOLDER
from ..face_recognition_system import FaceRecognitionSystem
from ..models import FaceIDResponse, ErrorResponse, MessageResponse

router = APIRouter()
face_recognition_system = FaceRecognitionSystem()

@router.get('/faces', response_model=list[str])
def get_faces():
    with face_recognition_system.conn.cursor() as cur:
        cur.execute("SELECT id FROM face_embeddings")
        rows = cur.fetchall()
        face_ids = [row[0] for row in rows]
    return face_ids

@router.post('/face/register', response_model=FaceIDResponse)
def register_face(file: UploadFile = File(...)):
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    face_locations = face_recognition_system.detect_faces(file_path)
    if not face_locations:
        raise HTTPException(status_code=400, detail="No face detected")
    
    face_encodings = face_recognition_system.extract_features(file_path, face_locations)
    face_id = face_recognition_system.add_face(face_encodings[0])
    return FaceIDResponse(face_id=face_id)

@router.post('/face/recognize', response_model=FaceIDResponse)
def recognize_face(file: UploadFile = File(...)):
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    face_locations = face_recognition_system.detect_faces(file_path)
    if not face_locations:
        raise HTTPException(status_code=400, detail="No face detected")
    
    face_encodings = face_recognition_system.extract_features(file_path, face_locations)
    face_id = face_recognition_system.recognize_face(face_encodings[0])
    if face_id:
        return FaceIDResponse(face_id=face_id)
    raise HTTPException(status_code=404, detail="Face not recognized")

@router.delete('/face/{face_id}', response_model=MessageResponse)
def delete_face(face_id: str):
    if face_recognition_system.delete_face(face_id):
        return MessageResponse(message="Face deleted")
    raise HTTPException(status_code=404, detail="Face not found")
