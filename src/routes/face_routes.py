from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
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
async def register_face(file: UploadFile = File(...)):
    image_data = await file.read()
    
    face_locations = face_recognition_system.detect_faces(image_data)
    if not face_locations:
        raise HTTPException(status_code=400, detail="No face detected")
    
    face_encodings = face_recognition_system.extract_features(image_data, face_locations)
    face_id = face_recognition_system.add_face(face_encodings[0])
    return FaceIDResponse(face_id=face_id)

@router.post('/face/recognize', response_model=FaceIDResponse)
async def recognize_face(file: UploadFile = File(...)):
    image_data = await file.read()
    
    face_locations = face_recognition_system.detect_faces(image_data)
    if not face_locations:
        raise HTTPException(status_code=400, detail="No face detected")
    
    face_encodings = face_recognition_system.extract_features(image_data, face_locations)
    face_id = face_recognition_system.recognize_face(face_encodings[0])
    if face_id:
        return FaceIDResponse(face_id=face_id)
    raise HTTPException(status_code=404, detail="Face not recognized")

@router.delete('/face/{face_id}', response_model=MessageResponse)
def delete_face(face_id: str):
    if face_recognition_system.delete_face(face_id):
        return MessageResponse(message="Success! Face deleted")
    raise HTTPException(status_code=404, detail="Face not found")
