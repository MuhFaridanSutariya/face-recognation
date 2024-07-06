from pydantic import BaseModel

class FaceIDResponse(BaseModel):
    face_id: str

class ErrorResponse(BaseModel):
    error: str

class MessageResponse(BaseModel):
    message: str
