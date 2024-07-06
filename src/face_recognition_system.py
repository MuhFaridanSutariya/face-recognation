import uuid
import numpy as np
import face_recognition
from .database import get_db_connection
from io import BytesIO

class FaceRecognitionSystem:
    def __init__(self):
        self.conn = get_db_connection()

    def detect_faces(self, image_data):
        image = face_recognition.load_image_file(BytesIO(image_data))
        face_locations = face_recognition.face_locations(image)
        return face_locations

    def extract_features(self, image_data, face_locations):
        image = face_recognition.load_image_file(BytesIO(image_data))
        face_encodings = face_recognition.face_encodings(image, face_locations)
        return face_encodings

    def add_face(self, face_encoding):
        face_id = str(uuid.uuid4())
        self.save_face_to_db(face_id, face_encoding)
        return face_id

    def save_face_to_db(self, face_id, face_encoding):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO face_embeddings (id, embedding) VALUES (%s, %s)",
                (face_id, face_encoding.tolist())
            )
            self.conn.commit()

    def delete_face(self, face_id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM face_embeddings WHERE id = %s", (face_id,))
            self.conn.commit()
            return cur.rowcount > 0

    def recognize_face(self, face_encoding):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, embedding FROM face_embeddings")
            rows = cur.fetchall()
            for row in rows:
                db_face_id, db_face_encoding = row
                match = face_recognition.compare_faces([np.array(db_face_encoding)], face_encoding)
                if match[0]:
                    return db_face_id
        return None
