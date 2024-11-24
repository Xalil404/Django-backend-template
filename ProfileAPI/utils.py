import firebase_admin
from firebase_admin import auth
from rest_framework.exceptions import AuthenticationFailed

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app()

def verify_firebase_token(id_token):
    try:
        # Verify Firebase ID token
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # This contains user data, including the Firebase UID
    except Exception as e:
        raise AuthenticationFailed('Invalid Firebase token')
